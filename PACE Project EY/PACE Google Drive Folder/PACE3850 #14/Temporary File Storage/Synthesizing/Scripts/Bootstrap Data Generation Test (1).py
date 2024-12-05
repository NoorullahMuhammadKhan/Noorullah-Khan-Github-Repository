import pandas as pd
import numpy as np

# Load your original dataset
df = pd.read_csv('D:\Documents\PACE_Dev\cleaned_dataset1.csv') # change this to the merged database 1

# Set the number of synthetic rows you want to generate
num_samples = 3000

# Generate synthetic data by sampling from the original data's distribution
synthetic_data = df.sample(n=num_samples, replace=True).reset_index(drop=True)

# Optionally, add some noise to numeric columns and ensure no negatives
for column in synthetic_data.select_dtypes(include=[np.number]):
    noise = np.random.normal(0, 0.01, size=synthetic_data[column].shape)
    synthetic_data[column] += noise
    synthetic_data[column] = synthetic_data[column].round()  # Round to nearest whole number
    synthetic_data[column] = synthetic_data[column].clip(lower=0)  # Ensure no negative values

# Save the synthetic data to 'synthetic_data_statisticalsampling.csv' in the Documents folder
synthetic_data.to_csv('D:/Documents/PACE_Dev/synthetic_dataset4.csv.csv', index=False)

# Print a statement to indicate the process is done
print("Synthetic data generation completed and saved to 'test_synthetic_dataset4.csv'")

