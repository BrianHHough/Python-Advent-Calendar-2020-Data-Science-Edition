from test_your_code import check_funcion
import numpy as np

def generate_arr(start, end):
  # YOUR CODE GOES HERE
  my_array = np.arange(start,end)
  return my_array
  
print(check_funcion(generate_arr))