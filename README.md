arlington_base_pack
│
├── data/
│   ├── raw/                # Original downloaded data (ACS, TIGER, OSM)
│   ├── processed/          # Cleaned and merged datasets
│   └── outputs/            # Final exports (CSV, GeoJSON, etc.)
│
├── scripts/
│   ├── 01_fetch_acs_data.py       # Pulls ACS demographic and economic data
│   ├── 02_fetch_tiger_data.py     # Downloads TIGER/Line shapefiles
│   ├── 03_clean_merge_data.py     # Cleans and merges datasets
│   ├── 04_generate_outputs.py     # Produces final data outputs
│
├── .env.example           # Template for API key setup
├── requirements.txt       # Required Python packages
├── README.md              # Project documentation
└── main.py                # Optional: runs all scripts in order
