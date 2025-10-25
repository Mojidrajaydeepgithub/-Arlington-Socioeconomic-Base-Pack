#!/usr/bin/env python3
import os
from pathlib import Path
import requests
import geopandas as gpd

OUT_DIR = Path("data/raw")
OUT_DIR.mkdir(parents=True, exist_ok=True)
STATE_FIPS = "48"
COUNTY_FIPS = "439"
YEAR = "2023"
TIGER_URL = f"https://www2.census.gov/geo/tiger/TIGER{YEAR}/TRACT/tl_{YEAR}_{STATE_FIPS}_tract.zip"

out_zip = OUT_DIR / f"tl_{YEAR}_{STATE_FIPS}_tract.zip"
out_geojson = OUT_DIR / f"tarrant_tracts_{YEAR}_48439.geojson"

r = requests.get(TIGER_URL, stream=True, timeout=60)
r.raise_for_status()
with open(out_zip, "wb") as fh:
    for chunk in r.iter_content(chunk_size=8192):
        fh.write(chunk)

gdf = gpd.read_file(out_zip)
gdf_tarrant = gdf[gdf["COUNTYFP"] == COUNTY_FIPS].copy()
gdf_tarrant.to_file(out_geojson, driver="GeoJSON")
print("Saved:", out_geojson)
