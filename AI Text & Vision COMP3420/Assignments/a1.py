import numpy as np # type: ignore
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Input, Flatten, Dense, Dropout # type: ignore

# Task 1
def light_pixels(image, lightness, channel):
    """Return a mask for each channel that identifies the pixels whose intensity is 
    above the given threshold."""
    
    # Map channel name to index
    channel_map = {'red': 0, 'green': 1, 'blue': 2}
    
    # Get the index for the specified channel
    channel_index = channel_map.get(channel.lower())
    
    if channel_index is None:
        raise ValueError("Channel must be 'red', 'green', or 'blue'.")
    
    # Create the mask: 1 where intensity > lightness, else 0
    mask = (image[:, :, channel_index] > lightness).astype(int)
    
    return mask

# Task 2
def histogram(image, buckets, channel):
    """
    Return a histogram of the channel, where the image is represented as a 
    3-channel numpy array with values between 0 and 255. A histogram is
    an array of length `buckets` where the i-th element is the count of pixels
    in the range [i * (256 // buckets), (i + 1) * (256 // buckets)).
    """
    
    # Map channel name to index
    channel_map = {'red': 0, 'green': 1, 'blue': 2}
    
    # Get the index for the specified channel
    channel_index = channel_map.get(channel.lower())
    
    if channel_index is None:
        raise ValueError("Channel must be 'red', 'green', or 'blue'.")
    
    # Get the relevant channel data
    channel_data = image[:, :, channel_index]
    
    # Initialize the histogram array
    hist = np.zeros(buckets, dtype=int)
    
    # Calculate the bucket size
    bucket_size = 256 // buckets
    
    # Populate the histogram
    for value in np.nditer(channel_data):
        bucket_index = min(value // bucket_size, buckets - 1)
        hist[bucket_index] += 1
    
    return hist

     
# Task 3
def build_deep_nn(rows, columns, channels, layer_options):
    """
    Return a Keras neural model that has the following layers:
    - a Flatten layer with input shape (rows, columns, channels)
    - as many hidden layers as the length of layer_options
    - layer_options is a list of layer options, such that:
      - hidden layer number i is of size layer_options[i][0] and activation
        layer_options[i][1]
      - if layer_options[i][2] > 0, then hidden layer number i is followed
        by a dropout layer with dropout rate layer_options[i][2]

    Parameters:
    rows (int): Number of rows in the input.
    columns (int): Number of columns in the input.
    channels (int): Number of channels in the input.
    layer_options (list of tuples): Each tuple contains three elements:
                                    (hidden_size, activation, dropout_rate).

    Returns:
    keras.models.Sequential: The constructed Keras model.
    """
    
    model = Sequential()
    
    # Flatten the input
    model.add(Flatten(input_shape=(rows, columns, channels)))
    
    # Add the hidden layers as specified in layer_options
    for hidden_size, activation, dropout_rate in layer_options:
        model.add(Dense(hidden_size, activation=activation))
        if dropout_rate > 0:
            model.add(Dropout(dropout_rate))
    
    # Add the output layer
    model.add(Dense(10, activation='softmax'))  # 10 units for 10 classes
    
    return model


if __name__ == "__main__":
     import doctest
     doctest.testmod()
