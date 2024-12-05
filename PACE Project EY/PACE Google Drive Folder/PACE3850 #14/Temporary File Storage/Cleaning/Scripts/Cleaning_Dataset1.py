#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:28:04 2024

@author: aasnayemgazzalichowdhury
"""

import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/aasnayemgazzalichowdhury/Desktop/Uni Documents/2024 Session 2/COMP3850/Datasets/dataset1.csv')

# Rename columns for clarity and easier access
df.rename(columns={
    'incident_type': 'AccidentType',
    'incident_hour_of_the_day': 'IncidentTime',
    'number_of_vehicles_involved': 'NumVehiclesInvolved',
    'police_report_available': 'PoliceReportBool',
    'insured_sex': 'DriverGender',
    'age': 'DriverAge',
    'insured_education_level': 'EducationLevel',
    'policy_annual_premium': 'InsurancePremium',
    'policy_deductable': 'InsuranceAccess',
    'months_as_customer': 'TimeAsCustomer',
    'fraud_reported': 'Fraud',
    'incident_severity': 'IncidentSeverity',
    'bodily_injuries': 'NumBodilyInjuries',
    'authorities_contacted': 'AuthoritiesInvolved',
    'total_claim_amount': 'TotalClaimAmount',
    'auto_year': 'VehicleYear'
}, inplace=True)

# Clean 'PoliceReportBool' column
df['PoliceReportBool'] = df['PoliceReportBool'].replace({'?': 'NO'})

# Clean 'collision_type' column
df['collision_type'] = df['collision_type'].replace({'?':'NaN'})

# Clean 'property_damage' column
df['property_damage'] = df['property_damage'].replace({'?':'NO'})

# Round Insurance Premium column
df['InsurancePremium'] = df['InsurancePremium'].round().astype(int)

# Clean '_c39' column
df['_c39'] = df['_c39'].fillna('NaN')

# Save the cleaned dataframe to a new CSV file
df.to_csv('/Users/aasnayemgazzalichowdhury/Desktop/Uni Documents/2024 Session 2/COMP3850/Cleaning/cleaned_dataset1.csv', index=False)
