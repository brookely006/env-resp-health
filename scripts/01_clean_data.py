import pandas as pd

# file paths
cdc_path = "data/raw/PLACES__Local_Data_for_Better_Health,_Census_Tract_Data,_2025_release_20260426.csv"
epa_path = "data/raw/annual_aqi_by_county_2025.csv"

cdc = pd.read_csv(cdc_path)
epa = pd.read_csv(epa_path)

# pivot cdc from long to wide
cdc_clean = cdc.pivot_table(
    index=['StateDesc', 'CountyName', 'LocationName', 'TotalPopulation'],
    columns='MeasureId', 
    values='Data_Value'
).reset_index().rename(columns={
    'StateDesc': 'State',
    'CountyName': 'County',
    'LocationName': 'Census_Tract',
    'CASTHMA': 'Asthma_Pct',
    'COPD': 'COPD_Pct'
})

# normalize join keys
for df in [cdc_clean, epa]:
    df['join_state'] = df['State'].str.strip().str.lower()
    df['join_county'] = df['County'].str.strip().str.lower()

# merge and drop redundant columns
merged = pd.merge(cdc_clean, epa, on=['join_state', 'join_county'], how='inner')
merged = merged.drop(columns=['join_state', 'join_county', 'State_y', 'County_y'])
merged = merged.rename(columns={'State_x': 'State', 'County_x': 'County'})

# convert population from comma-string to int
merged['TotalPopulation'] = merged['TotalPopulation'].astype(str).str.replace(',', '').astype(int)

print(f"Final shape: {merged.shape}")

merged.to_csv("data/processed/merged_health_env_data.csv", index=False)