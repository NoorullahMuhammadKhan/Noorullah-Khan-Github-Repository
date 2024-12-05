# CTGAN Data Generation Test
from sdv.tabular import CTGAN
import pandas as pd

# Load your cleaned data
df = pd.read_csv('file path')

# Initialize the CTGAN model
model = CTGAN()

# Fit the model to the data
model.fit(df)

# Generate synthetic data
synthetic_data = model.sample(50)

# Save the synthetic data to a CSV file
synthetic_data.to_csv('file path', index=False)

print("Synthetic data generation completed using CTGAN. The synthetic dataset has been saved to 'file path.")
