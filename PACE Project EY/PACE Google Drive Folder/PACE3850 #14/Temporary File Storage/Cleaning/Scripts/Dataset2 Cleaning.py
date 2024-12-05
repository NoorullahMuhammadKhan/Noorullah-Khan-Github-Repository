#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:13:01 2024

@author: aasnayemgazzalichowdhury
"""

import pandas as pd
import numpy as np

#Load the dataset
df = pd.read_csv('/Users/aasnayemgazzalichowdhury/Desktop/Uni Documents/2024 Session 2/COMP3850/cleaned_dataset_2_local.csv')

#Define Distribution of AccidentType
accident_type_distribution = {
    'Multi-vehicle Collision': 0.419,
    'Single Vehicle Collision': 0.403,
    'Vehicle Theft': 0.094,
    'Parked Car': 0.084
}

np.random.seed(0)  # For reproducibility

#Generate Accident Type based on the distribution
df['AccidentType'] = np.random.choice(
    list(accident_type_distribution.keys()), 
    size=len(df), 
    p=list(accident_type_distribution.values())
)


#Define Distribution of NumVehiclesInvolved
def distribution_num_vehicles_involved(accident_type):
        if accident_type == 'Multi-vehicle Collision':
           return np.random.normal(3, 0.38)  
        else:
           return 1 

np.random.seed(0)  # For reproducibility

#Generate NumVehiclesInvoled based on the distribution
df['NumVehiclesInvolved'] = df['AccidentType'].apply(lambda x: distribution_num_vehicles_involved(x)).round().astype(int)

#Define Distribution of VehicleAge 
vehicle_age_distribution = {
    '0' : 0.047,
    '1' : 0.044, 
    '2' : 0.049,
    '3' : 0.046,
    '4' : 0.053,
    '5' : 0.050,
    '6' : 0.050, 
    '7' : 0.045,
    '8' : 0.052, 
    '9' : 0.053,
    '10': 0.054,
    '11': 0.039,
    '12': 0.051,
    '13': 0.049,
    '14': 0.042,
    '15': 0.042, 
    '16': 0.055,
    '17': 0.040,
    '18': 0.046,
    '19': 0.037,
    '20': 0.056,
      
    }

np.random.seed(0)  # For reproducibility

#Define Distribution of VehicleAge
df['VehicleAge'] = np.random.choice(
    list(vehicle_age_distribution.keys()),
    size=len(df),
    p=list(vehicle_age_distribution.values())
    )

#Spit out the file
df.to_csv('/Users/aasnayemgazzalichowdhury/Desktop/Uni Documents/2024 Session 2/COMP3850/Adding_Columns_dataset_2_local.csv', index=False)
