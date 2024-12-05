# STATISTICAL CORRELATION BETWEEN INSURANCEPREMIUM AND INSURNACEACCESS IN DATASET 1

# Load necessary libraries
library(ggplot2)

# Load the dataset
df <- read.csv('D:/Documents/PACE_Dev/cleaned_dataset1.csv')

# Check for NA values
print(paste("NA values in InsurancePremium:", sum(is.na(df$InsurancePremium))))
print(paste("NA values in InsuranceAccess:", sum(is.na(df$InsuranceAccess))))

# Calculate correlation
correlation <- cor(df$InsurancePremium, df$InsuranceAccess, use = "complete.obs", method = "pearson")
print(paste("Correlation between InsurancePremium and InsuranceAccess:", round(correlation, 2)))

# Plotting scatter plot
ggplot(df, aes(x = InsuranceAccess, y = InsurancePremium)) +
  geom_point() +
  labs(title = "Scatter Plot of InsurancePremium vs. InsuranceAccess",
       x = "InsuranceAccess",
       y = "InsurancePremium") +
  theme_minimal()
