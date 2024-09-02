# RS_Course_20240902


# Welcome to the GitHub Repository

This repository provides resources and code examples to help you learn and work with Google Earth Engine and other associated tools. Below are the steps and links you'll need to begin.

## Setting Up

### Step 1: Create a Google Account

First, ensure you have a Google account. You will need it to access various services including Google Earth Engine and Google Colab.

### Step 2: Explore Datasets

Explore different datasets available on Earth Engine by visiting the [Data Catalog](https://developers.google.com/earth-engine/datasets/catalog).

### Step 3: Learn About Functions

For more detailed information on specific functions, check the following resources:
- [Earth Engine API - Terrain Slope](https://developers.google.com/earth-engine/apidocs/ee-terrain-slope)
- [Leafmap Overview - Extrude Polygons](https://leafmap.org/maplibre/overview/#extrude-polygons-for-3d-indoor-mapping)
- [Geemap Notebooks](https://geemap.org/)

## Earth Engine Access

### Step 4: Gain Access

To get started with Earth Engine, follow the steps outlined [here](https://developers.google.com/earth-engine/guides/access#a-role-in-a-cloud-project_3).

### Step 5: Enable API and Create a Project

Enable APIs and services on Google Cloud, create a project, and note down your project ID. Manage your project at [Google Cloud Console](https://console.cloud.google.com/apis/dashboard?project=automatic-translation-398315).

## Coding in JavaScript

### Step 6: Using the Code Editor

To develop code with JavaScript, use the Earth Engine [Code Editor](https://code.earthengine.google.com/).

**Example Code:** Check out this example on forest change detection [here](https://code.earthengine.google.com/db7653ccca2dbcc270a8b5f05f7eda5e) or from the file `Ex1_forestchange_JS.txt`.

## Working with Python and Google Colab

### Step 7: Setup Colab

Log in to your Google Drive, click '+ New', and from 'More', search for 'Colab'. This will open a new Colab environment.

### Step 8: Authenticate and Initialize

For authentication and initialization, use the following code in your Colab notebook:

``python
import geemap
import ee
from google.colab import auth

# Authenticate and initialize the Earth Engine session
auth.authenticate_user()
ee.Initialize(project='the id of the project you created')
''

**Sample Code:** Access a sample notebook [here](https://colab.research.google.com/drive/1VhstK4uZqQsMttKoKRmHeWcuaZN77sOj?usp=sharing) or use the file `Azar_RS_20240902.ipynb`.

## Using GEE in Non-Colab Environments or QGIS

### Step 9: Installation and Authentication

To use Google Earth Engine in non-Colab environments or with QGIS, execute the following commands in your command line (for Windows):

``shell
pip install earthengine-api
earthengine authenticate

This will store your credentials for future use.

### Step 10: Running Code in QGIS

After installing the Google Earth Engine plugin in QGIS, start the Python console and try the following sample code using the file `forest_change.py`.

## Conclusion

With the steps above, you should be well-prepared to explore and develop with Google Earth Engine. Make sure to review each link and document to understand the tools and codes thoroughly.

