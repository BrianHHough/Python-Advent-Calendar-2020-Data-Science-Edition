import re
import numpy as np
import datetime
import numpy as np

    
def check_funcion(fun):
  NoneType = type(None)
  if isinstance(fun(0,1), NoneType):
    return "You return 'None', try again!"
  test_list = [(2,21), (7,39)]
  results = [True, True]
  outputs = [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 
  [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]]
  correct_types = []
  for i in range(len(test_list)):
    outp_func = fun(test_list[i][0], test_list[i][1])
    for j in range(len(outp_func)-1):
      if outp_func[j] != outputs[i][j]:
        results[i] = False
    correct_types.append(type(outp_func)==np.ndarray)
  if len(results)>0 and all(results) and all(correct_types):
    return "Congrats, you passed the task! See you tomorrow!"
  elif len(results)>0 and all(results):
    return "You return a list instead of numpy.array"
  else:
    return "Try again, something is still not OK!"

