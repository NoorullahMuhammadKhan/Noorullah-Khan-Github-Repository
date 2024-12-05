import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv(r'D:\Documents\PACE_Dev\raw_dataset2.csv')

# Filter for motor claims
df_motor = df.loc[df["INSURANCE_TYPE"] == "Motor"].copy()

# Fill in null values with the lowest degree for EducationLevel
df_motor['CUSTOMER_EDUCATION_LEVEL'] = df_motor['CUSTOMER_EDUCATION_LEVEL'].fillna('High School')

# Drop unwanted columns
df_motor = df_motor.drop(['TXN_DATE_TIME', 'TRANSACTION_ID', 'CUSTOMER_ID', 'POLICY_NUMBER',
                          'POLICY_EFF_DT', 'LOSS_DT', 'REPORT_DT', 'INSURANCE_TYPE',
                          'CUSTOMER_NAME', 'ADDRESS_LINE1', 'ADDRESS_LINE2', 'CITY', 'STATE',
                          'POSTAL_CODE', 'SSN', 'MARITAL_STATUS', 'EMPLOYMENT_STATUS', 'NO_OF_FAMILY_MEMBERS',
                          'RISK_SEGMENTATION', 'HOUSE_TYPE', 'SOCIAL_CLASS', 'ROUTING_NUMBER', 'ACCT_NUMBER',
                          'INCIDENT_STATE', 'INCIDENT_CITY', 'AGENT_ID', 'VENDOR_ID'], axis=1)

# Rename the columns for clarity
df_motor.rename(columns={
    'TENURE': 'TimeAsCustomer',
    'INCIDENT_HOUR_OF_THE_DAY': 'IncidentTime',
    'POLICE_REPORT_AVAILABLE': 'PoliceReportBool',
    'AGE': 'DriverAge',
    'CUSTOMER_EDUCATION_LEVEL': 'EducationLevel',
    'PREMIUM_AMOUNT': 'InsurancePremium',
    'INCIDENT_SEVERITY': 'IncidentSeverity',
    'ANY_INJURY': 'NumBodilyInjuries',
    'AUTHORITY_CONTACTED': 'AuthoritiesInvolved',
    'CLAIM_AMOUNT': 'TotalClaimAmount',
    'CLAIM_STATUS': 'ClaimStatus',
}, inplace=True)

# Multiply the InsurancePremium column by 12
df_motor['InsurancePremium'] *= 12

# Round InsurancePremium to whole numbers
df_motor['InsurancePremium'] = df_motor['InsurancePremium'].round().astype(int)

# Add empty column for DriverGender
df_motor['DriverGender'] = np.nan

# Define Distribution of AccidentType
accident_type_distribution = {
    'Multi-vehicle Collision': 0.419,
    'Single Vehicle Collision': 0.403,
    'Vehicle Theft': 0.094,
    'Parked Car': 0.084
}

np.random.seed(0)  # For reproducibility

# Generate AccidentType based on the distribution
df_motor['AccidentType'] = np.random.choice(
    list(accident_type_distribution.keys()),
    size=len(df_motor),
    p=list(accident_type_distribution.values())
)

# Define Distribution of NumVehiclesInvolved
def distribution_num_vehicles_involved(accident_type):
    if accident_type == 'Multi-vehicle Collision':
        return np.random.normal(3, 0.38)
    else:
        return 1

# Generate NumVehiclesInvolved based on the distribution
df_motor['NumVehiclesInvolved'] = df_motor['AccidentType'].apply(lambda x: distribution_num_vehicles_involved(x)).round().astype(int)

# Define Distribution of VehicleAge
vehicle_age_distribution = {
    '0': 0.047,
    '1': 0.044,
    '2': 0.049,
    '3': 0.046,
    '4': 0.053,
    '5': 0.050,
    '6': 0.050,
    '7': 0.045,
    '8': 0.052,
    '9': 0.053,
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

# Generate VehicleAge based on the distribution
df_motor['VehicleAge'] = np.random.choice(
    list(vehicle_age_distribution.keys()),
    size=len(df_motor),
    p=list(vehicle_age_distribution.values())
).astype(int)

# Define Distribution of InsuranceAccess
insurance_access_distribution = {
    500: 0.342,
    1000: 0.351,
    2000: 0.307
}

# Generate InsuranceAccess based on the distribution
df_motor['InsuranceAccess'] = np.random.choice(
    list(insurance_access_distribution.keys()),
    size=len(df_motor),
    p=list(insurance_access_distribution.values())
)

# Create 'DriverExperience' column
np.random.seed(0)  # For reproducibility
df_motor['DriverExperience'] = df_motor['DriverAge'] - 16 - np.random.randint(0, 7, size=len(df_motor))

# Create 'LicenceType' column based on 'DriverExperience'
conditions = [
    (df_motor['DriverExperience'] < 1),
    (df_motor['DriverExperience'] >= 1) & (df_motor['DriverExperience'] < 3),
    (df_motor['DriverExperience'] >= 3) & (df_motor['DriverExperience'] < 5),
    (df_motor['DriverExperience'] >= 5)
]
choices = ['Ls', 'P1', 'P2', 'Full']
df_motor['LicenceType'] = np.select(conditions, choices, default='')

# Reorder columns
df_motor = df_motor[['TimeAsCustomer', 'DriverAge', 'InsuranceAccess', 'InsurancePremium', 'DriverGender', 'EducationLevel', 'AccidentType', 'IncidentSeverity', 'AuthoritiesInvolved', 'IncidentTime', 'NumVehiclesInvolved', 'NumBodilyInjuries', 'PoliceReportBool', 'TotalClaimAmount', 'ClaimStatus', 'VehicleAge', 'DriverExperience', 'LicenceType']]

# Save the cleaned dataframe to a new CSV file
df_motor.to_csv(r'D:\Documents\PACE_Dev\cleanstage3_dataset2.csv', index=False)

print("Data processing completed. The cleaned dataset has been saved to 'D:\\Documents\\PACE_Dev\\cleanstage3_dataset2.csv'.")
