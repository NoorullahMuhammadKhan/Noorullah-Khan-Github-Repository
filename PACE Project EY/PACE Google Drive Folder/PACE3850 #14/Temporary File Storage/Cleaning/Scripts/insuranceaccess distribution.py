import pandas as pd
import numpy as np

# Load the cleaned_dataset1
df = pd.read_csv(r'D:\Documents\PACE_Dev\cleaned_dataset1.csv')

# Describe the distribution of InsuranceAccess
insurance_access_desc = df['InsuranceAccess'].describe()
print("InsuranceAccess Description:")
print(insurance_access_desc)

# Define bins for InsuranceAccess with a step of 250
bins = np.arange(0, df['InsuranceAccess'].max() + 250, 250)

# Create a new column 'AccessCategory' to categorize the 'InsuranceAccess' values
df['AccessCategory'] = pd.cut(df['InsuranceAccess'], bins=bins, include_lowest=True)

# Calculate the distribution within the new categories
insurance_access_distribution = df['AccessCategory'].value_counts(normalize=True).sort_index()
print("\nInsuranceAccess Distribution (in 250 intervals):")
print(insurance_access_distribution)

# Save the distribution details for further use
insurance_access_distribution.to_csv(r'D:\Documents\PACE_Dev\insurance_access_distribution_250.csv')

