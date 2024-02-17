import numpy as np
import matplotlib.pyplot as plt

# Define the activity function
def activity(t):
    return (-0.25 * t**2 + 10 * t + 10) / 10

# Generate time values from 0 to 10 hours
t_values = np.linspace(0, 10, 100)

# Calculate activity values
activity_values = [activity(t) for t in t_values]

# Plot the activity of the catalyst over time
plt.plot(t_values, activity_values)
plt.xlabel('Time (hours)')
plt.ylabel('Activity of Catalyst')
plt.grid(True)
plt.show()



