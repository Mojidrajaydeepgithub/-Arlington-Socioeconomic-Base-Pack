#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import geopandas as gpd
import numpy as np
import re

RAW_DIR = Path("data/raw")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)

acs = pd.read_csv(RAW_DIR / "acs_tracts_2023_tarrant_48439.csv", dtype=str)
acs_cols = [c for c in acs.columns if c not in ["state", "county", "tract", "GEOID"]]
for c in acs_cols:
    acs[c] = pd.to_numeric(acs[c], errors="coerce")

acs["poverty_rate"] = acs["poverty_count"] / acs["poverty_universe"]
acs["unemployment_rate"] = acs["unemployed"] / acs["in_labor_force"]

tiger = gpd.read_file(RAW_DIR / "tarrant_tracts_2023_48439.geojson")
gdf = tiger.merge(acs, on="GEOID", how="left")
gdf.to_parquet(OUT_DIR / "tract_master.parquet")
print("Wrote:", OUT_DIR / "tract_master.parquet")
