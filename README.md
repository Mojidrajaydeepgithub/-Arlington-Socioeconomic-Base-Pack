# instructions for ACS & TIGER 

#  Census Data Pipeline — ACS & TIGER Integration



There are a few things I’d like you to include moving forward to make the project more accessible and user-friendly for the entire team:

- **Clear execution instructions:** Document the exact order in which each script should be run and include any setup steps or required commands.  
- **File structure overview:** Provide a clearly organized folder structure showing where each file and output is located for better clarity and reusability.  
- **API key setup instructions:** Explain how users can obtain a Census API key, with step-by-step instructions, and include an example `.env` file.

---

## Requirements

Before running the scripts, ensure you have:

### 1. Python 3.9+
### 2. Install dependencies
```bash
pip install pandas geopandas requests numpy python-dotenv
```

### 3. Folder Setup
Make sure your project structure looks like this before running any scripts:

```plaintext
project_root/
│
├── fetch_tiger_tracts.py
├── standardize_and_join.py
├── qa_and_docs.py
│
├── .env
│
├── data/
│   ├── raw/
│   │   ├── acs_tracts_2023_tarrant_48439.csv
│   │   └── (TIGER shapefiles downloaded automatically)
│   └── processed/
│
└── README.md
```

---

##  API Key Setup (Required)

The U.S. Census Bureau requires an API key to access ACS data programmatically.

### **Step 1 – Obtain your key**
Go to the official Census API signup page:  
 [https://api.census.gov/data/key_signup.html](https://api.census.gov/data/key_signup.html)

Fill out the form and you’ll receive your API key by email.

---

### **Step 2 – Create a `.env` file**
In your project’s root directory, create a file named `.env` containing your key:

```bash
CENSUS_API_KEY=your_api_key_here
```

>  **Important:** Never share or commit this `.env` file to GitHub.  
> Each team member should create their own locally.

---

### **Step 3 – Load the key in Python**
Example code snippet (already supported by most scripts):

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("CENSUS_API_KEY")
```

---

##  Script Execution Guide

Below are detailed instructions for each script:  
**Run them in this exact order.**

---

###  **1. fetch_tiger_tracts.py**

#### Purpose:
Fetches TIGER tract shapefiles from the U.S. Census Bureau for Tarrant County, TX (FIPS 48439).

#### Command:
```bash
python fetch_tiger_tracts.py
```

#### What It Does:
- Downloads TIGER tract shapefile for 2023.  
- Filters data for Tarrant County.  
- Saves as a GeoJSON file.

#### Output:
```
data/raw/tarrant_tracts_2023_48439.geojson
```

#### Console Output:
```
Saved: data/raw/tarrant_tracts_2023_48439.geojson
```

---

###  **2. standardize_and_join.py**

#### Purpose:
Combines ACS CSV data with TIGER shapefiles and calculates indicators.

#### Prerequisite:
Place this file in `data/raw/`:
```
acs_tracts_2023_tarrant_48439.csv
```

#### Command:
```bash
python standardize_and_join.py
```

#### What It Does:
- Reads ACS and TIGER data.  
- Converts numeric fields.  
- Calculates:
  - `poverty_rate = poverty_count / poverty_universe`
  - `unemployment_rate = unemployed / in_labor_force`
- Joins datasets on `GEOID`.  
- Exports final dataset to Parquet format.

#### Output:
```
data/processed/tract_master.parquet
```

#### Console Output:
```
Wrote: data/processed/tract_master.parquet
```

---

###  **3. qa_and_docs.py**

#### Purpose:
Performs QA on the processed dataset to ensure completeness and consistency.

#### Command:
```bash
python qa_and_docs.py
```

#### What It Does:
- Reads `tract_master.parquet`.  
- Computes:
  - Total number of rows.  
  - Unique GEOIDs.  
  - Missing value rates per column.  
- Exports a JSON QA report.

#### Output:
```
data/processed/qa_report.json
```

#### Console Output:
```
QA report saved: data/processed/qa_report.json
```

---

##  Folder Structure Overview

```plaintext
project_root/
│
├── fetch_tiger_tracts.py
├── standardize_and_join.py
├── qa_and_docs.py
│
├── .env
│
├── data/
│   ├── raw/
│   │   ├── acs_tracts_2023_tarrant_48439.csv
│   │   └── tarrant_tracts_2023_48439.geojson
│   └── processed/
│       ├── tract_master.parquet
│       └── qa_report.json
│
└── README.md
```

---

##  Summary Workflow

| Step | Script | Description | Output |
|------|---------|-------------|---------|
| 1️ | `fetch_tiger_tracts.py` | Fetch and filter TIGER tract shapefiles | `tarrant_tracts_2023_48439.geojson` |
| 2️ | `standardize_and_join.py` | Merge ACS + TIGER datasets, compute metrics | `tract_master.parquet` |
| 3️ | `qa_and_docs.py` | Validate and document dataset | `qa_report.json` |

---

##  Notes

- The pipeline is reproducible and designed for reuse by any team member.  
- All file paths are relative and compatible across systems.  
- Existing files will be safely overwritten when re-running scripts.  
- `.env` is required for API access but excluded from version control.

---

**Maintainer:** *Data Engineering Team*  
**Last Updated:** October 2025


