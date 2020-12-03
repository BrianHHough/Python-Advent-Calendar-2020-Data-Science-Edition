from test_your_code import check_funcion
import numpy as np

def replace_nans(array):
  for i in range(0,len(array)):
    if np.isnan(array[i]):
      array[i] = -1
  return array
  
print(check_funcion(replace_nans))