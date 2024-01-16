import numpy as np
from visualization import plot_characteristics

# Enter Parameters here:
mu = 1  # Service rate
N = 10  # Buffer size
lambd_range = np.linspace(0.1, 0.9, 20)  # Range of arrival rates

# Plotting the characteristics
plot_characteristics(lambd_range, mu, N)
