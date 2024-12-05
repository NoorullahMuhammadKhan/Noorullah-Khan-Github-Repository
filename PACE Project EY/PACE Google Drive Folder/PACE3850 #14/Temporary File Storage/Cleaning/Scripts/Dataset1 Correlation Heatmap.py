# Correlation Matrix Heatmap Dataset 1

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Load your cleaned dataset
df = pd.read_csv('D:/Documents/PACE_Dev/cleaned_dataset1.csv')

# List of non-numeric columns to encode
non_numeric_columns = df.select_dtypes(include=['object']).columns

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Convert non-numeric columns to numeric using LabelEncoder
for column in non_numeric_columns:
    df[column] = label_encoder.fit_transform(df[column])

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Generate a larger correlation heatmap with adjusted layout
plt.figure(figsize=(16, 12))  # Further increase figure size for readability
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap for Cleaned Dataset 1', pad=20)  # Add padding to the title for better spacing
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout(pad=2)  # Adjust the layout to prevent clipping of labels
plt.savefig('D:/Documents/PACE_Dev/correlation_heatmap.png')  # Save the heatmap to a file
plt.show()

# Identify strong or notable correlations
strong_correlations = correlation_matrix.unstack().sort_values(ascending=False)

# Filter out self-correlations and keep only one instance of each pair
strong_correlations = strong_correlations[strong_correlations != 1].drop_duplicates()

# Set threshold for strong correlation
threshold = 0.7

# Display strong correlations above the threshold
significant_correlations = strong_correlations[strong_correlations.abs() > threshold]
print("Significant correlations (absolute value > {:.1f}):".format(threshold))
print(significant_correlations)

# Optionally, save the significant correlations to a text file
with open('D:/Documents/PACE_Dev/significant_correlations.txt', 'w') as file:
    file.write("Significant correlations (absolute value > {:.1f}):\n".format(threshold))
    file.write(significant_correlations.to_string())
