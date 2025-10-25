#!/usr/bin/env python3
import os
from pathlib import Path
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
CENSUS_KEY = os.getenv("CENSUS_API_KEY")
if not CENSUS_KEY:
    raise RuntimeError("Census API key missing")

YEAR = "2023"
STATE_FIPS = "48"
COUNTY_FIPS = "439"
VARS = {
    "B01003_001E": "total_population",
    "B19013_001E": "median_household_income",
    "B17001_002E": "poverty_count",
    "B17001_001E": "poverty_universe",
    "B23025_005E": "unemployed",
    "B23025_003E": "in_labor_force"
}

params = {
    "get": ",".join(VARS.keys()),
    "for": "tract:*",
    "in": f"state:{STATE_FIPS}+county:{COUNTY_FIPS}",
    "key": CENSUS_KEY
}
url = f"https://api.census.gov/data/{YEAR}/acs/acs5"
r = requests.get(url, params=params)
r.raise_for_status()
data = r.json()
cols = data[0]
rows = data[1:]
df = pd.DataFrame(rows, columns=cols).rename(columns=VARS)
df["GEOID"] = df["state"] + df["county"] + df["tract"]
out = Path("data/raw/acs_tracts_2023_tarrant_48439.csv")
out.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out, index=False)
print("Saved:", out)
