# STATISTICAL CORRELATION BETWEEN ACCIDENTTYPE AND NUMVEHICLESINVOLVED

import pandas as pd
import numpy as np
from scipy import stats

# Load the cleaned dataset
df = pd.read_csv(r'D:\Documents\PACE_Dev\cleaned_dataset1.csv')

# Check for the presence of all AccidentType categories
accident_types = df['AccidentType'].unique()
print("AccidentType categories found:", accident_types)

# Check the number of data points per AccidentType
counts = df['AccidentType'].value_counts()
print("Data points per AccidentType:")
print(counts)

# Perform ANOVA to determine the relationship between AccidentType and NumVehiclesInvolved
anova_results = stats.f_oneway(
    *[df['NumVehiclesInvolved'][df['AccidentType'] == accident_type] for accident_type in accident_types]
)

# Print the ANOVA results
print(f"ANOVA results: F-value = {anova_results.statistic}, p-value = {anova_results.pvalue}")

# If the p-value is significant (e.g., p < 0.05), we can assume a relationship exists
if anova_results.pvalue < 0.05:
    print("There is a significant relationship between AccidentType and NumVehiclesInvolved.")

    # Calculate the mean and standard deviation of NumVehiclesInvolved for each AccidentType
    accident_type_stats = df.groupby('AccidentType')['NumVehiclesInvolved'].agg(['mean', 'std']).reset_index()
    
    print("AccidentType statistics for NumVehiclesInvolved:")
    print(accident_type_stats)
else:
    print("No significant relationship found between AccidentType and NumVehiclesInvolved.")
