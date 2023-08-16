''' To install matplotlib package:-

    pip intsall matplotlib

'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# Checking Matplotlib Version

# print(matplotlib.__version__)

'''
Pyplot
Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:
'''

# Now the Pyplot package can be referred to as plt.


xpoints = np.array([5, 10])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
