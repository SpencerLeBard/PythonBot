import matplotlib.pyplot as plt
import numpy as np

# Create a list of evenly-spaced numbers over the range
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot


# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4], [5, 10, 15, 20])
# plt.title("Linear relationship", fontsize=20)
# plt.xlabel("X Axis", fontsize=20)
# plt.ylabel("Y Axis", fontsize=20)
# plt.show()

# import pandas as pd

# data = {
#     'cars': [5, 4, 1, 7],
#     'boats': [2, 6, 0, 2]
# }

# vehicals = pd.DataFrame(data, index=['Peter', 'Sarah', 'Ali', 'John'])

# print(vehicals.info())
