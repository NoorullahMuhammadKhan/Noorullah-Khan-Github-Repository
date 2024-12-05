Dataset1 <- read.csv("#")

# Calculate the distribution of VehicleAge
vehicle_age_distribution <- table(Dataset1$VehicleAge)

# Display the distribution
print(vehicle_age_distribution)

# Calculate total number of vehicles
total_vehicles = sum(vehicle_age_distribution)

# Calculate proportions for each age category
distribution = vehicle_age_distribution/total_vehicles
print(distribution)
