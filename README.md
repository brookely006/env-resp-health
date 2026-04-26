# Socioeconomic Confounders in Spatial Epidemiology: PM2.5 vs. Respiratory Health

## Project Objective
This repository contains a data science pipeline designed to evaluate whether the standard correlation between fine particulate matter (PM2.5) and chronic respiratory illness holds up when controlling for neighborhood level median household income. 

By merging systems level environmental data from the EPA with granular, tract level health and socioeconomic metrics, this project investigates the true localized drivers of asthma and Chronic Obstructive Pulmonary Disease (COPD) across 58,183 U.S. census tracts.

## Data Sources
This analysis integrates three primary datasets:

* **CDC PLACES (2025 Release):** Local Data for Better Health. Used to extract model-based estimates for Chronic Asthma and COPD prevalence across 58,000+ Census Tracts. 
    * [CDC Data Portal](https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh/about_data)
* **EPA Air Quality System (AQS):** Daily PM2.5 monitoring data. Used to calculate the annual "High-Pollution Day" count per county to represent environmental exposure.
    * [EPA AirData Download](https://aqs.epa.gov/aqsweb/airdata/download_files.html)
* **U.S. Census Bureau API (ACS 5-Year):** Used to programmatically fetch Table B19013 (Median Household Income in the Past 12 Months) for every census tract in the study.
    * [Census Bureau Data API](https://www.census.gov/data/developers/data-sets.html)
    
## Tech Stack
* **Language:** Python
* **Data Processing:** `pandas`, `numpy`
* **Statistical Modeling:** `statsmodels` (Multivariate OLS Regression)
* **Data Ingestion:** `requests` (US Census Bureau ACS API)
* **Visualization:** `matplotlib`, `seaborn`

## Key Findings
* **The Income Effect:** Median household income is a vastly superior predictor of respiratory health than raw county level air quality metrics. Both asthma and COPD exhibit strong, statistically significant inverse relationships with neighborhood income.
* **Asthma and PM2.5:** When holding population and income constant, the number of days with high PM2.5 is **not** a statistically significant predictor of asthma prevalence (p = 0.264).
* **Model Strength:** The multivariate OLS model for COPD explained nearly 25% of the total nationwide variance (R-squared = 0.247), with socioeconomic status acting as the primary driver. 

*(For the complete methodology, visualizations, and statistical breakdowns, please read the full research paper located in the `paper/` directory).*

## Repository Structure
* `data/` 
  * `raw/` : Unprocessed CDC PLACES and EPA AQS CSV files.
  * `processed/` : Cleaned datasets and the final merged outputs.
* `paper/` : Contains the final research PDF and raw regression text outputs.
* `scripts/`
  * `01_data_cleaning.py` : Cleans and standardizes geographic FIPS codes.
  * `02_exploratory_analysis.py` : Generates bivariate scatterplots and correlation heatmaps.
  * `03_fetch_census_api.py` : Hits the American Community Survey API to pull median income.
  * `04_statistical_analysis.py` : Runs the final OLS regression models and exports the summary tables.

## How to Run the Pipeline
To replicate this analysis on your local machine, follow these steps:

**Step 1:** Clone the repository and install the required dependencies:
```bash
pip install -r requirements.txt
```

**Step 2:** Execute the data pipeline sequentially from the root directory:
```bash
python scripts/01_data_cleaning.py
python scripts/02_exploratory_analysis.py
python scripts/03_fetch_census_api.py
python scripts/04_statistical_analysis.py
```
**Step 3:** The final regression output will be automatically saved to `paper/regression_results.txt`
