import re
import numpy as np
import datetime
import numpy as np

    
def check_funcion(fun):
  test_list = [np.array([1, np.nan, 2, 3, 4]), np.array([1]), np.array([np.nan])]
  NoneType = type(None)
  if isinstance(fun(test_list[1]), NoneType):
    return "You return 'None', try again!"
  elif isinstance(fun(test_list[1]), type(np.array([]))):
    outputs = [np.array([1, -1, 2, 3, 4]), np.array([1]), np.array(-1)]
    results = []
    for i in range(len(test_list)):
      outp_func = fun(test_list[i])
      comparison = (outp_func == outputs[i])
      results.append(comparison.all())
    if all(results):
      return "Congrats, you passed the task! Submit it and see you tomorrow!"
    else:
      return "Try again, something is still not OK!"
  else:
    return "You should return a Numpy array!"

