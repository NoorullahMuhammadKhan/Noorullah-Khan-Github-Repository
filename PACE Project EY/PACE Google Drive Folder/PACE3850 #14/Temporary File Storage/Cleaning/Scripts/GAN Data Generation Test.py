import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Load the smaller dataset
df = pd.read_csv('D:/Documents/cleaned_data_50_rows.csv')

# Select only numeric columns for normalization
numeric_columns = df.select_dtypes(include=[np.number]).columns
df_numeric = df[numeric_columns]

# Normalize the numeric data between 0 and 1 for better GAN training
df_normalized = (df_numeric - df_numeric.min()) / (df_numeric.max() - df_numeric.min())

# Define the generator model
def create_generator():
    model = Sequential()
    model.add(Dense(16, input_dim=latent_dim, activation='relu'))
    model.add(Dense(data_dim, activation='sigmoid'))  # Output should match the dimension of the input data
    return model

# Define the discriminator model
def create_discriminator():
    model = Sequential()
    model.add(Dense(16, input_dim=data_dim, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    return model

# Set hyperparameters
latent_dim = 8  # Size of the noise vector, reduced for simplicity
data_dim = df_numeric.shape[1]  # Number of numeric features in the input data
adam = Adam(learning_rate=0.0001, beta_1=0.5)

# Create and compile the discriminator
discriminator = create_discriminator()
discriminator.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])

# Create the generator
generator = create_generator()

# Create the GAN model by combining the generator and discriminator
gan = Sequential([generator, discriminator])
discriminator.trainable = False
gan.compile(loss='binary_crossentropy', optimizer=adam)

# Training the GAN
def train_gan(epochs, batch_size=8):
    for epoch in range(epochs):
        # Generate random noise as input to initialize the generator
        noise = np.random.normal(0, 1, (batch_size, latent_dim))
        generated_data = generator.predict(noise)

        # Get a random set of real data from the dataset
        real_data = df_normalized.sample(batch_size)

        # Concatenate real and fake data
        combined_data = np.concatenate([real_data, generated_data])

        # Labels for real data: 1s, fake data: 0s
        labels = np.concatenate([np.ones((batch_size, 1)), np.zeros((batch_size, 1))])

        # Train the discriminator
        d_loss = discriminator.train_on_batch(combined_data, labels)

        # Generate misleading labels for fake data (pretend they're all real)
        misleading_labels = np.ones((batch_size, 1))

        # Train the generator (via the GAN model, where the discriminator is frozen)
        g_loss = gan.train_on_batch(noise, misleading_labels)

        # Print progress every 10 epochs
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Discriminator Loss: {d_loss[0]}, Generator Loss: {g_loss}")

# Train the GAN with fewer epochs and a smaller batch size for testing
train_gan(epochs=100, batch_size=8)

# Generate 50 rows of synthetic data using the trained generator
noise = np.random.normal(0, 1, (50, latent_dim))
synthetic_data = generator.predict(noise)

# Convert synthetic data to original scale
synthetic_data_df = pd.DataFrame(synthetic_data, columns=df_numeric.columns)
synthetic_data_denormalized = synthetic_data_df * (df_numeric.max() - df_numeric.min()) + df_numeric.min()

# Save the synthetic data to a CSV file
synthetic_data_denormalized.to_csv('D:/Documents/synthetic_data_50_rows.csv', index=False)

print("Synthetic data generation completed. The synthetic dataset has been saved to 'D:/Documents/synthetic_data_50_rows.csv'.")

