#!/usr/bin/env python3
import pandas as pd
import geopandas as gpd
import json
from pathlib import Path

OUT = Path("data/processed/qa_report.json")
gdf = gpd.read_parquet("data/processed/tract_master.parquet")
report = {
    "rows": len(gdf),
    "unique_geoids": gdf["GEOID"].nunique(),
    "missing_rate": gdf.isna().mean().to_dict()
}
with open(OUT, "w") as f:
    json.dump(report, f, indent=2)
print("QA report saved:", OUT)
