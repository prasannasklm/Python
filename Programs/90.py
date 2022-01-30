import sys
'''write a program to add given two numbers with exception handling
        INPUT
            num_1: input integer
            num_2: input integer
        OUTPUT
            Return the sum of given two numbers if they are valid integers.
            Otherwise, return type of Error.

        Note: Replace the None with output in return statement.
        Example1:
            input:
                num1 = 1
                num2 = 2
            output:
            3
        Example2:
            input:
                num1 = 1
                num2 = hi
            output:
                NameError'''
a=input("enter a:")
b=input("enter b:")
try:
    c=int(a)+int(b)
    print(c)
except(ValueError):
    print("NameError")
