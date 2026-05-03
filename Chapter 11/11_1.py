"""
While our implementations work correctly on data sets of numbers,
they are not necessarily the best versions to use with very large data sets.
To mitigate these problems, you can import some of these functions
from NumPy, a popular library for numerical analysis.
"""

import numpy as np

lyst = [1, 2, 3, 4]
print(np.mean(lyst))
print(np.median(lyst))
print(np.std(lyst))
