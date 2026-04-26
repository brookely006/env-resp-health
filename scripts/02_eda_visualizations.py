import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ensure the output directory exists
os.makedirs("paper/figures", exist_ok=True)

df = pd.read_csv("data/processed/merged_health_env_data.csv")

# set a clean, academic visual style
sns.set_theme(style="whitegrid")

# fig 1: scatterplot with an OLS trendline (PM2.5 vs Asthma)
plt.figure(figsize=(8, 6))
sns.regplot(
    data=df, 
    x="Days PM2.5", 
    y="Asthma_Pct", 
    scatter_kws={'alpha': 0.2, 'color': 'steelblue'}, 
    line_kws={'color': 'darkred'}
)
plt.title("Asthma Prevalence vs. Days with High PM2.5")
plt.xlabel("Days PM2.5")
plt.ylabel("Asthma Prevalence (%)")
plt.tight_layout()
plt.savefig("paper/figures/fig1_pm25_vs_asthma.png", dpi=300)
plt.close()

# fig 2: correlation heatmap for quantitative metrics
cols = ['Asthma_Pct', 'COPD_Pct', 'Median AQI', 'Days PM2.5', 'Days Ozone']
corr_matrix = df[cols].corr()

plt.figure(figsize=(7, 5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
plt.title("Correlation Matrix: Health Outcomes & Air Quality")
plt.tight_layout()
plt.savefig("paper/figures/fig2_correlation_matrix.png", dpi=300)
plt.close()

print("Figures saved to paper/figures/")