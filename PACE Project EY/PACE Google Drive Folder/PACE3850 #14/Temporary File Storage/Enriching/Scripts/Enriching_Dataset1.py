#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:24:45 2024

@author: aasnayemgazzalichowdhury
"""

import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('/Users/aasnayemgazzalichowdhury/Desktop/Uni Documents/2024 Session 2/COMP3850/Cleaning/cleaned_dataset1.csv')

# Replace '?' with 'NO' and then convert 'YES' to 1 and 'NO' to 0
df['PoliceReportBool'] = df['PoliceReportBool'].map({'YES': 1, 'NO': 0})

# Convert 'DriverGender' to numerical
# Convert 'MALE' to 0 and 'FEMALE' to 1
df['DriverGender'] = df['DriverGender'].map({'MALE': 0, 'FEMALE': 1})

# Convert 'Fraud' to numerical
# Convert 'Y' to 1 and 'N' to 0
df['Fraud'] = df['Fraud'].map({'Y': 1, 'N': 0})

# Create 'VehicleAge' column
# Calculate vehicle age using the formula: VehicleAge = 2015 - VehicleYear
df['VehicleAge'] = 2015 - df['VehicleYear']

# Create 'DriverExperience' column
# Calculate driver experience using the formula: DriverExperience = Age - 16 - Random(0,6)
np.random.seed(0)  # For reproducibility
df['DriverExperience'] = df['DriverAge'] - 16 - np.random.randint(0, 7, size=len(df))

# Create 'LicenceType' column based on 'DriverExperience'
# Determine license type based on experience using specified conditions
conditions = [
    (df['DriverExperience'] < 1),
    (df['DriverExperience'] >= 1) & (df['DriverExperience'] < 3),
    (df['DriverExperience'] >= 3) & (df['DriverExperience'] < 5),
    (df['DriverExperience'] >= 5)
]
choices = ['Ls', 'P1', 'P2', 'Full']
df['LicenceType'] = np.select(conditions, choices, default='')

# Drop unnecessary columns
columns_to_drop = ['policy_number', 'policy_bind_date', 'policy_state', 'policy_csl', 'umbrella_limit',
                   'insured_zip', 'insured_occupation', 'insured_hobbies', 'insured_relationship',
                   'capital-gains', 'capital-loss', 'incident_date', 'collision_type', 'incident_state',
                   'incident_city', 'incident_location', 'property_damage', 'witnesses', 'injury_claim',
                   'property_claim', 'vehicle_claim', 'auto_make', 'auto_model','_c39']
df.drop(columns=columns_to_drop, inplace=True)

# Save the cleaned dataframe to a new CSV file
df.to_csv('/Users/aasnayemgazzalichowdhury/Desktop/Uni Documents/2024 Session 2/COMP3850/Enriching/CleanedEnriched_Dataset1.csv', index=False)

