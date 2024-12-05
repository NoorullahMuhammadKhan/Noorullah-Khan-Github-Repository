# STATISTICAL CORRELATION BETWEEN INSURANCEPREMIUM AND INSURNACEACCESS IN DATASET 1


import pandas as pd

# Load the dataset
df = pd.read_csv('D:/Documents/PACE_Dev/cleaned_dataset1.csv')

# Check if the columns are numeric
print(f"InsurancePremium data type: {df['InsurancePremium'].dtype}")
print(f"InsuranceAccess data type: {df['InsuranceAccess'].dtype}")

# Convert 'InsuranceAccess' to numeric if necessary (e.g., if it's a categorical variable like 'Low', 'Medium', 'High')
# This is just an example mapping, adjust according to your actual data
if df['InsuranceAccess'].dtype == 'object':
    access_mapping = {'Low': 100, 'Medium': 500, 'High': 1000}  # Example mapping
    df['InsuranceAccess'] = df['InsuranceAccess'].map(access_mapping)

# Check for NaN values in the relevant columns
print(f"NaN values in InsurancePremium: {df['InsurancePremium'].isna().sum()}")
print(f"NaN values in InsuranceAccess: {df['InsuranceAccess'].isna().sum()}")

# Calculate the correlation between InsurancePremium and InsuranceAccess
correlation = df['InsurancePremium'].corr(df['InsuranceAccess'])

# Print the correlation
print(f"Correlation between InsurancePremium and InsuranceAccess: {correlation:.2f}")

