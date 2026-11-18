# SDS210 – Programming with Spatial Data: course data

Datasets used in the lessons and practicals of **SDS210 Programming with Spatial Data**,
Department of Geography, University of Zurich. The course book is online at
<https://hendrikwulf.github.io/sds210-jb/>.

All files are small, ready-to-use subsets or derivatives of open datasets, prepared for teaching.
Each lesson has its own folder; a file shared by several lessons is stored once, in the first
lesson that uses it.

```text
giuz/sds210/
├── README.md       this file
├── SHA256SUMS      checksums of all files
├── L06/            Data frames (pandas): MeteoSwiss weather tables
├── L07/            Vector data (GeoPandas): Swiss boundaries, points of interest, networks
├── L08/            Visualization: Natural Earth, Eurostat NUTS, Zurich open data, HydroSHEDS
├── L09/            Raster data (rasterio, NumPy): Landsat, Sentinel-2, DEMs, glaciers
└── L10/            Time series and data cubes (xarray): Alpine snow cover, DEM, lakes
```

## Using the data

Every file has a public URL of the form
`https://data.source.coop/giuz/sds210/<lesson>/<file>`. Python reads them directly, without a
separate download step:

```python
import pandas as pd
import geopandas as gpd
import rasterio

base = "https://data.source.coop/giuz/sds210"

weather = pd.read_csv(f"{base}/L06/kloten_daily_19800101_20260101.csv")
cantons = gpd.read_file(f"{base}/L07/swissBoundaries3D_cantons.gpkg")
with rasterio.open(f"{base}/L09/Copernicus_DEM_NZ_subset.tif") as src:
    dem = src.read(1)
```

To download a whole lesson folder, use the AWS command line tool (no account needed):

```bash
aws s3 sync s3://giuz/sds210/L07/ ./data --endpoint-url https://data.source.coop --no-sign-request
```

or open the folder on <https://source.coop/giuz/sds210> and download individual files.

## Files

**L06 – Data frames.** Daily and hourly weather tables, processed from MeteoSwiss
SwissMetNet Open Government Data.

| File | Content |
|---|---|
| `kloten_summer_2022.txt` | Kloten, daily temperatures, June–August 2022 (fixed-width text with header) |
| `kloten_summer_2022_extended.txt` | Kloten, daily temperature, humidity, wind, radiation, summer 2022 |
| `kloten_summer_2022_rain_sun.csv` | Kloten, daily precipitation and sunshine, summer 2022 |
| `Lugano_summer_2022_extended.txt` | Lugano, daily weather variables, summer 2022 |
| `kloten_daily_19800101_20260101.csv` | Kloten, daily temperature, precipitation, sunshine, 1980–2025 |
| `kloten_spring_2024_hourly.csv` | Kloten, hourly weather, spring 2024 |
| `saentis_hourly_temp_precip_20200101_20260101.csv` | Säntis, hourly temperature and precipitation, 2020–2025 |
| `magic_mountain_weather.csv` | Daily weather since 1972 for Practical L6., station: concealed and source: confidential |

**L07 – Vector data.**

| File | Content | Source |
|---|---|---|
| `swissBoundaries3D_switzerland.gpkg` / `.geojson` / `.zip` | National territory (same data in three formats) | swisstopo, swissBOUNDARIES3D 1.5 |
| `swissBoundaries3D_cantons.gpkg` | Cantons | swisstopo, swissBOUNDARIES3D 1.5 |
| `swissBoundaries3D_grisons.gpkg` | Canton of Grisons | swisstopo, swissBOUNDARIES3D 1.5 |
| `swissBoundaries3D_municipalities.gpkg` | Municipalities | swisstopo, swissBOUNDARIES3D 1.5 |
| `ne_50m_admin_0_countries.zip` | World countries, 1:50m (shapefile) | Natural Earth |
| `country_in_europe.gpkg` | One European country, for a guessing exercise | Natural Earth |
| `alpine_huts.gpkg` | Alpine huts in Switzerland | © OpenStreetMap contributors |
| `swissHighways.gpkg` | National road axes. Note: the CRS is stored as undefined; set it with `.set_crs(2056)` | Federal Roads Office FEDRO |
| `wohnungsinventar.gpkg` | Second-home share per municipality, 2023 | Federal Office for Spatial Development ARE |
| `wolf_tracks_switzerland.gpkg` | Snowshoe trails (layer `Schneeschuhwanderwege`), used as stand-in wolf tracks | swisstopo |
| `swiss_parks.shp.zip` | Parks of national importance (shapefile) | Federal Office for the Environment FOEN |
| `hospital_landing_sites.geojson` | Hospital helicopter landing sites |swisstopo |
| `NuclearPowerPlant.csv` | Swiss nuclear power plants with LV95 coordinates | swisstopo |
| `meteoswiss_pollen_network.csv` | Pollen monitoring stations | MeteoSwiss |
| `kloten_test_data.csv` | Kloten daily mean temperature since 1980 | MeteoSwiss |

**L08 – Visualization.**

| File | Content | Source |
|---|---|---|
| `ne_10m_land.zip`, `ne_10m_ocean.zip`, `ne_10m_lakes.zip`, `ne_10m_rivers_lake_centerlines.zip`, `ne_10m_glaciated_areas.zip` | Physical base layers, 1:10m (shapefiles) | Natural Earth |
| `worldcities.csv` | World cities with population | simplemaps World Cities Basic |
| `nuts_rg_03m_2024_3035_pop_wm_eu.gpkg` | NUTS 2024 regions with population | Eurostat GISCO, © EuroGeographics for the administrative boundaries |
| `total_solar_eclipse_03-09-2081_center_line.gpkg`, `..._core_shadow.gpkg` | Path of the total solar eclipse of 3 September 2081 | NASA eclipse predictions |
| `EV_charging_stations.gpkg` | Electric vehicle charging stations | Swiss Federal Office of Energy SFOE |
| `Zurich_quarters.gpkg`, `Zurich_bike_lanes_masterplan.gpkg`, `Zurich_bike_parking.gpkg` | City quarters, cycling masterplan, bike parking | Stadt Zürich Open Data |
| `hydrosheds_basins_level_01.gpkg`, `hydrosheds_basins_level_02.gpkg` | River basins, Pfafstetter levels 1 and 2 | HydroSHEDS (Lehner & Grill 2013) |
| `hydrorivers_100.gpkg` | River network (filtered, about 830 MB) | HydroRIVERS (Lehner & Grill 2013) |

**L09 – Raster data.**

| File | Content | Source |
|---|---|---|
| `LC09_L1TP_075090_20230224_20230308_02_T1_subset.tif` | Landsat 9 subset, New Zealand, 7 bands, 40 m | USGS Landsat |
| `Copernicus_DEM_NZ_subset.tif` | Elevation model, New Zealand, 30 m (also used in L10) | Copernicus DEM GLO-30 |
| `ETOPO1_bedrock_subset_2000m_3857.tif` | Global topography and bathymetry, 2 km | NOAA NCEI ETOPO1 |
| `GLIMS_glaciers_NZ_subset.zip`, `GLIMS_haupapa_tasman.gpkg` | Glacier outlines, New Zealand | GLIMS Glacier Database |
| `JRC_lake_mapourika.gpkg` | Outline of Lake Mapourika | JRC Global Surface Water |
| `LC08_121061_20190904_subset.tif`, `LC08_121061_20230814_subset.tif` | Landsat 8 surface reflectance, Indonesia, 2019 and 2023 | USGS Landsat |
| `GERD_before_composite_SWIR1_NIR_Green.tif`, `GERD_after_...` | Landsat 8 composites before and after filling the Grand Ethiopian Renaissance Dam | USGS Landsat |
| `S2_composite_2017.tif`, `S2_composite_2025.tif` | Sentinel-2 summer median composites, 6 bands, 10 m (Practical L9) | Contains modified Copernicus Sentinel data 2017 and 2025 |

**L10 – Time series and data cubes.**

| File | Content | Source |
|---|---|---|
| `LC09_L1TP_075090_20230224_20230308_02_T1_subset_30m.tif` | Landsat 9 subset, 5 bands, 30 m, on the grid of `L09/Copernicus_DEM_NZ_subset.tif` | USGS Landsat |
| `MODIS_Annual_SCF_2001-2025_1000m_epsg3035.tif` | Annual snow cover frequency in the Alps, 2001–2025, 1 km (Practical L10) | Derived from NASA MODIS snow cover products |
| `Copernicus_DEM_Alps_1000m_epsg3035.tif` | Elevation model of the Alps, 1 km | Copernicus DEM |
| `mod44w_lake_mask_min100px_1000m_epsg3035.tif` | Lake mask of the Alps, 1 km | NASA MODIS MOD44W |
| `AlpineConventionPerimeter_epsg3035.zip` | Perimeter of the Alpine Convention | Permanent Secretariat of the Alpine Convention |
| `bahnen-winter_epsg2056.gpkg` | Ski lifts and cable cars | swisstopo, Bahnen Winter |

## Licences and attribution

The files keep the licence of their original source; please credit the sources above when you
reuse them. In particular:

- **swisstopo, FEDRO, ARE, FOEN, SFOE, MeteoSwiss:** Swiss Open Government Data, free use with
  attribution (for example "Source: swisstopo").
- **OpenStreetMap:** Open Database Licence (ODbL) 1.0, "© OpenStreetMap contributors".
- **Natural Earth, NOAA ETOPO1, USGS Landsat, NASA MODIS and eclipse data:** public domain.
- **Copernicus DEM and Sentinel-2:** free and open Copernicus data; credit "Copernicus DEM" and
  "Contains modified Copernicus Sentinel data".
- **Eurostat GISCO:** © EuroGeographics for the administrative boundaries.
- **simplemaps World Cities Basic:** CC BY 4.0.
- **Stadt Zürich Open Data, GLIMS, JRC Global Surface Water:** free with attribution or citation.
- **HydroSHEDS / HydroRIVERS:** the HydroSHEDS licence allows redistribution (CC-BY 4.0 license);
  cite Lehner, B., Grill G. (2013), Hydrological Processes, 27(15), 2171–2186.

Checksums of all files are in `SHA256SUMS` (`shasum -a 256 -c SHA256SUMS` verifies a download).
