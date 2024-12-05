# ADDING GENDER INTO DATASET 2 using API

import pandas as pd
import requests

# Load the raw dataset
df = pd.read_csv('D:/Documents/PACE_Dev/raw_dataset2.csv')

# Extract the first name from the `CUSTOMER_NAME` column
df['FirstName'] = df['CUSTOMER_NAME'].apply(lambda x: x.split()[0])

# Function to get gender from Genderize.io API
def get_gender(name):
    try:
        response = requests.get(f'https://api.genderize.io?name={name}')
        if response.status_code == 200:
            return response.json().get('gender', None)
        else:
            return None
    except:
        return None

# Apply the function to get the gender for each first name
df['DriverGender'] = df['FirstName'].apply(get_gender)

# Save the updated dataframe
df.to_csv('D:/Documents/PACE_Dev/updated_dataset2.csv', index=False)

print("Gender prediction completed and saved to 'D:/Documents/PACE_Dev/updated_dataset2.csv'.")
