# Homework

Homework assignments are organized by assignment number.


# Data

This folder contains the spatial (and tabular) datasets used for the
National Park road accessibility analysis.

## National Park Boundaries

### `nps_boundary`

Source: National Park Service (NPS)
https://irma.nps.gov/DataStore/Reference/Profile/2224545?lnv=True

This dataset contains the geographic boundaries of National Park
Service units in the United States. The polygon boundaries will be
used to identify the National Parks included in the analysis. I had to 
download this file as a shapefile and export it as a Geojson through QGIS.

Primary use:
- National Park boundaries
- Clipping the road network
- Calculating park area
- Measuring road accessibility

## U.S. Roads

### `us_roads.geojson`

Source: US Department of Transportation
https://geodata.bts.gov/datasets/usdot::north-american-roads/about

This dataset contains primary roads throughout the United States.
The road network will be used to examine the distribution of roads
within and near National Park boundaries. I had to download this file as a CSV
and use QGIS to export it as a Geojson. 

Primary use:
- Clipping roads to National Park boundaries
- Creating road buffers
- Measuring the proportion of each park located within 1 mile of a road

## U.S. Outline

### `gz_2010_us_outline_500k.json`

Source: GeoJSON and KML data for the United States
https://eric.clst.org/tech/usgeojson/

This GeoJSON dataset contains a generalized outline of the United States.
It may be used as a background layer for national-scale maps.

Primary use:
- Map background/context

## National Park Annual Visitation

### 'Annual Visitation and Record Year by Park...'

Source: US National Park Service (NPS)
https://irma.nps.gov/Stats/Reports/National

This dataset contains data recording the annual visitation totals for each national park by year. 
This data set was downloaded as a csv file. 
