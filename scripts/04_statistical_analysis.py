import pandas as pd
import statsmodels.formula.api as smf

# load the final dataset that includes the income data
df = pd.read_csv("data/processed/final_dataset_with_income.csv")

# bulk format columns (remove spaces and periods for statsmodels)
df.columns = df.columns.str.replace(' ', '_').str.replace('.', '', regex=False)

# scale variables down to thousands to fix the condition number warning
df['Population_k'] = df['TotalPopulation'] / 1000
df['Income_k'] = df['Median_Income'] / 1000

# fit ols models 
asthma_mod = smf.ols("Asthma_Pct ~ Days_PM25 + Days_Ozone + Population_k + Income_k", data=df).fit()
copd_mod = smf.ols("COPD_Pct ~ Days_PM25 + Days_Ozone + Population_k + Income_k", data=df).fit()

# print to console
print("--- Asthma Model ---")
print(asthma_mod.summary())

print("\n--- COPD Model ---")
print(copd_mod.summary())

# dump results to text file for the repo
with open("paper/regression_results.txt", "w") as f:
    f.write("ASTHMA MODEL\n" + "="*50 + "\n")
    f.write(asthma_mod.summary().as_text())
    f.write("\n\nCOPD MODEL\n" + "="*50 + "\n")
    f.write(copd_mod.summary().as_text())
    
print("\nResults successfully saved to paper/regression_results.txt")