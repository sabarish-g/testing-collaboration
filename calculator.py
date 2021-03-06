"""
# -*- coding: utf-8 -*-
Created on Sat May  1 13:56:19 2021

@author: sabarish


This is an implementation of code to understand basic git commands.

This file implements a simple python calculator.

"""

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return round(self.a * self.b, 2)
    
    def divide(self):
        if self.b == 0:
            return "Cannot divide by 0"
        return round(self.a - self.b, 2)
 

def main():
    calc = Calculator(x,y)
    print('The addition is {}'.format(calc.add()))
    print('The subtraction is {}'.format(calc.subtract()))
    print('The multiplication is {}'.format(calc.multiply()))
    print('The divide is {}'.format(calc.divide()))
    


if __name__ == "__main__":
    main(x=1, y=2)
    main(x=100, y=2)
    main(x=10000, y=-5)
    main(x=-3, y=-3)
    main(x=-3, y=0)
    