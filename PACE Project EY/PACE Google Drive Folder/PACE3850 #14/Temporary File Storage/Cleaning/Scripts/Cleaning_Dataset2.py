import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/aasnayemgazzalichowdhury/Desktop/Uni Documents/2024 Session 2/COMP3850/Datasets/dataset2.csv')

# Filter for motor claims
df_motor = df.loc[df["INSURANCE_TYPE"] == "Motor"].copy()

# Fill in null values with the lowest degree for EducationLevel
df_motor['CUSTOMER_EDUCATION_LEVEL'] = df_motor['CUSTOMER_EDUCATION_LEVEL'].fillna('High School')


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

# Fill empty values for 'ADDRESS_LINE2' 
df_motor['ADDRESS_LINE2'] = df_motor['ADDRESS_LINE2'].fillna('NaN')

# Fill empty values for 'VENDOR_ID'
df_motor['VENDOR_ID'] = df_motor['VENDOR_ID'].fillna('NaN')

# Save the cleaned dataframe to a new CSV file
df_motor.to_csv('/Users/aasnayemgazzalichowdhury/Desktop/Uni Documents/2024 Session 2/COMP3850/Cleaning/cleaned_dataset2.csv', index=False)

print("Data processing completed. The cleaned dataset has been saved to the relevant folder'.")
