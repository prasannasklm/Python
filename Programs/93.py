import numpy as np
'''
    Create an nd array using numpy and add the elements in given list to it and perform the sum operation
    INPUT
        elements: list of elements
    OUTPUT
        return the sum of the elements
    Example:
        input:
            elements = [1,2,3,4]
        output:
            10
    Note: Replace the None with output in return statement.
    '''
a=np.array([[10,20,30],[2,4,6],[4,6,2]])
print(a)
print("sum of elements in array is:",np.sum(a))
