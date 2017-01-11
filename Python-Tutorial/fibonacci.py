#!usr/bin/python
# Code to generate Fibonacci sequence
# It uses a function fibonacci to print a fibonacci sequence less than n 
def fibonacci(n):
    a, b=0,1
    while b < n:
       print b
       a, b = b, a+b


if __name__=='__main__':
    fibonacci(10)
    
