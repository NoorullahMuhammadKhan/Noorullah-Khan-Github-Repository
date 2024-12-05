# API Test

import pandas as pd
import random

# Load your dataset
df = pd.read_csv('D:/Documents/PACE_Dev/raw_dataset2.csv')

# Extract first names from CUSTOMER_NAME (assuming first name is the first word)
df['FirstName'] = df['CUSTOMER_NAME'].apply(lambda x: x.split()[0])

# Sample gender determination based on typical name frequencies (random example)
def determine_gender(name):
    if name[-1].lower() in ['a', 'e', 'i']:
        return 'female'
    else:
        return 'male'

# Apply the gender determination function
df['PredictedGender'] = df['FirstName'].apply(determine_gender)

# Save the updated DataFrame to a new CSV file
df.to_csv('D:/Documents/PACE_Dev/cleaned_dataset2_with_gender.csv', index=False)

print("Gender prediction completed and saved to 'cleaned_dataset2_with_gender.csv'.")




