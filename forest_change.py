import ee
from ee_plugin import Map

# Initialize the Earth Engine API
ee.Initialize()

# Define the area of interest (replace with your specific coordinates)
aoi = ee.Geometry.Rectangle([100.0, 1.0, 101.0, 2.0])

# Load the Hansen Global Forest Change dataset
gfc = ee.Image('UMD/hansen/global_forest_change_2019_v1_7')

# Extract the forest cover for the year 2000
forestCover2000 = gfc.select(['treecover2000'])

# Extract the forest loss year band
lossYear = gfc.select(['lossyear'])

# Create a mask for changes between 2013 and 2019
changeMask = lossYear.gte(13).And(lossYear.lte(19))

# Apply the mask to the loss year band
changes = lossYear.updateMask(changeMask)

# Remap the years to make them more intuitive (2013 = 13, 2014 = 14, etc.)
changesRemapped = changes.remap(
    [13, 14, 15, 16, 17, 18, 19],
    [2013, 2014, 2015, 2016, 2017, 2018, 2019],
    0
).rename('year')

# Calculate the total area of change
areaImage = changesRemapped.gt(0).multiply(ee.Image.pixelArea())
totalChange = areaImage.reduceRegion(
    reducer=ee.Reducer.sum(),
    geometry=aoi,
    scale=30,
    maxPixels=1e9
)

print('Total area of change (sq m):', totalChange.getInfo()['year'])

# Calculate change per year
years = ee.List.sequence(2013, 2019)
yearlyChange = years.map(lambda year: {
    'year': year,
    'area': changesRemapped.eq(ee.Number(year)).multiply(ee.Image.pixelArea()).reduceRegion(
        reducer=ee.Reducer.sum(),
        geometry=aoi,
        scale=30,
        maxPixels=1e9
    ).get('year')
})

print('Yearly change:', yearlyChange.getInfo())

# Visualization setup for forest loss
visParams = {
    'min': 2013,
    'max': 2019,
    'palette': ['ff0000', 'ff3300', 'ff6600', 'ff9900', 'ffcc00', 'ffff00', 'ccff00']
}

# Add the forest cover layer (year 2000)
Map.addLayer(forestCover2000.clip(aoi), {'palette': ['000000', '00FF00'], 'max': 100}, 'Forest Cover 2000')

# Add the changes layer (2013-2019)
Map.addLayer(changesRemapped.clip(aoi), visParams, 'Forest Loss Year')

# Load a Sentinel-2 image collection for RGB visualization
sentinel2 = ee.ImageCollection('COPERNICUS/S2') \
    .filterBounds(aoi) \
    .filterDate('2023-01-01', '2023-12-31') \
    .sort('CLOUDY_PIXEL_PERCENTAGE') \
    .first()  # Get the least cloudy image

# Define visualization parameters for RGB
rgb_vis_params = {
    'bands': ['B4', 'B3', 'B2'],  # Red, Green, Blue bands for true color
    'min': 0,
    'max': 3000,
    'gamma': 1.4
}

# Add the RGB image to the QGIS map, ensuring it aligns with the AOI
Map.addLayer(sentinel2.clip(aoi), rgb_vis_params, 'Sentinel-2 RGB')

# Center the map on the area of interest
Map.centerObject(aoi, 8)
