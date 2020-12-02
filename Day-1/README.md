# DAY 1

## Prompt
Let's start with a warm-up task! If you are not familiar with NumPy yet, go to the resources section and check them out.
Write a function called generate_arr(start, end) that takes as input two integers start, end and returns a NumPy array (1 dimensional) containing all integers between those values including start and end. If you are not a beginner, provide a one-line solution here :) Note that you can test your function using check_funcion().

## Resources Used
* [GeeksforGeeks: Python Numpy](https://www.geeksforgeeks.org/python-numpy/?ref=lbp)
* [Numpy.org: Quickstart tutorial](https://numpy.org/doc/stable/user/quickstart.html)
* [Array creation](https://numpy.org/doc/stable/user/quickstart.html#array-creation)

## Learnings
* If you want to return a NumPy array with integers between what is put in the function...you need to first call it with `my_array = ...`
* Then you'll use `np.arrange(start,end)` to iterate from the beginning to the last.
* Finally, you'll return the array you defined with `return my_array`


