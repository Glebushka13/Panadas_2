import pandas as pd
import numpy as np

arr = np.array([1, 2, 3, 4])

result = pd.util.hash_array(arr)

print(result)
#Ņemot vērā 1d masīvu, atgrieziet deterministisku veselu skaitļu masīvu.
