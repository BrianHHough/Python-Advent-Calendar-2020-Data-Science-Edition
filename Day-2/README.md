# Day 2

## Prompt
Missing data is an everyday problem that data scientists need to deal with. Write a function called `replace_nans(array)` that takes as input a NumPy array and returns it after replacing all `np.nan (numpy.nan)` values with -1.

## Resources Used
* [GeeksforGeeks: numpy.isnan() in Python](https://www.geeksforgeeks.org/numpy-isnan-python/)

## Solution

        from test_your_code import check_funcion
        import numpy as np

        def replace_nans(array):
        for i in range(0,len(array)):
            if np.isnan(array[i]):
            array[i] = -1
        return array
        
        print(check_funcion(replace_nans))

## Learnings
* Originally I thought this was the correct function:

        def replace_nans(array):
        array = np.isnan(np.nan)
        return array

* The output is right, but it outputs a boolean (not a Numpy array).
* You need to create a temp array that stores the boolean values and then you can refer to it and update the true values with -1 in the original array.
* To solve this, we define a variable `i` and iterate over the array using the index and check if that value is not a number (i.e. `np.isnan(array[i])`).
* If yes, then we set that value to -1 with `array[i] = -1`
* Then we return the array we want (array starts at 0 to length-1)

