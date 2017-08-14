import numpy as np
import matplotlib.pyplot as plt

# toy dataset
greyhounds = 500
labs = 500

# generate random height of greys and labs
grey_height = 28 + 4  * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

# plot a histogram
plt.hist([grey_height, lab_height], stacked=True, color=['r','b'])
plt.show()
