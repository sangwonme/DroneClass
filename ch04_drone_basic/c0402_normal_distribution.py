from djitellopy import Tello
import cv2, math, time

import matplotlib.pyplot as plt
import numpy as np

y = np.random.randn(1000)

# Create the figure and axis objects
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot the data as a line
ax[0].plot(y)

# Create a histogram of the data
ax[1].hist(y, bins=100)

# Set the labels and title
ax[0].set_title('Noise Line Plot')
ax[1].set_title('Noise Histogram')

# Show the figure
fig.savefig('./noise_distribution.png', dpi=100)
plt.show()