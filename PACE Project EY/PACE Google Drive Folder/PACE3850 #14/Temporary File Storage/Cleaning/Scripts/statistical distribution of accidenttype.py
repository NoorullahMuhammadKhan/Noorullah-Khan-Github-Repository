import pandas as pd
import numpy as np
from scipy import stats

# Step 1: Load the cleaned dataset and calculate the frequency distribution of AccidentType
cleaned_df = pd.read_csv(r'D:\Documents\PACE_Dev\cleaned_dataset1.csv')

# Calculate the frequency distribution of each AccidentType
accident_type_counts = cleaned_df['AccidentType'].value_counts(normalize=True)
accident_type_distribution = accident_type_counts.to_dict()

print("AccidentType distribution in cleaned dataset:")
print(accident_type_distribution)
