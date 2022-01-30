'''Create a dictionary using dictionary comprehension for the given keys and values lists (keys and values lists have same length)
   INPUT
       keys: list containing dictionary keys
       values: list containing dictionary values
   OUTPUT
       new_dict: dictionary formed with keys and values lists

   Note: Replace the None with output in return statement.
   Example 1:
       input:
           keys = ['a','b','c','dog']
           values = ['apple','boy','cat','d']
       output:
           {'a':'apple','b':'boy','c':'cat','dog':'d'}

   '''
keys=[1,2,3,4]
values=['a','b','c','d']
dc=[{keys[i]:values[i]} for i in range(len(keys))]
print(dc)
