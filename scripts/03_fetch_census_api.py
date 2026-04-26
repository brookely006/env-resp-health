import pandas as pd
import requests

url = "https://api.census.gov/data/2022/acs/acs5?get=NAME,B19013_001E&for=county:*&in=state:*"
resp = requests.get(url)
resp.raise_for_status()

data = resp.json()
census = pd.DataFrame(data[1:], columns=data[0])

# clean numeric data
census = census.rename(columns={'B19013_001E': 'Median_Income', 'NAME': 'Full_Name'})
census['Median_Income'] = pd.to_numeric(census['Median_Income'], errors='coerce')
census = census[census['Median_Income'] > 0]

# split "County Name, State Name" into mergeable keys
splits = census['Full_Name'].str.split(', ', expand=True)
census['County'] = splits[0].str.replace(' County', '', regex=False).str.replace(' Parish', '', regex=False).str.strip().str.lower()
census['State'] = splits[1].str.strip().str.lower()

census = census[['State', 'County', 'Median_Income']]

# load the existing data
df = pd.read_csv("data/processed/merged_health_env_data.csv")
df['State'] = df['State'].str.strip().str.lower()
df['County'] = df['County'].str.strip().str.lower()

# merge and save
final = pd.merge(df, census, on=['State', 'County'], how='inner')
final.to_csv("data/processed/final_dataset_with_income.csv", index=False)

print(f"Added median income. New shape: {final.shape}")