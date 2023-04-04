"""
Calculator Program

Goal: 
To create a user input calculator.  User enters a number, asks what they want to do, 
then do the operation.  It will then ask if it wants another input or end the program.
It will then loop

What to use:
 -Loops
 -Def (function)
 -case statement 
 -User input

 Outline

 Function that contains the case statement
 this will take in 2 inputs, the total and the number that will be applied to the total.

 main loop: 
 this will just loop through the funtion until the user wants to quit.
"""

"""
Function that calculates what the user is inputed

variables: 
total - keeps the total going
X - what the user enters that goes into the total
"""

"""importing for print f """
import os, sys

"""Total is the final number after the math has been done"""
total = 0.0

"""X is user inputted number"""
X = 0.0

"""Op is the operator that will preform"""
op = ''

"""yn is a yes or no if the user wants to keep going"""
yn = 'y'


def Calculator(total : int, op : str, X : int):
    int(total)
    int(X)
    match op.upper(): 
        case "D":
            total = total / X
        case "M":
            total = total * X
        case "A": 
            total = total + X
        case "S":
            total = total - X
        case _:
            print("Incorrect input")
    return total


print("Welcome to Calculator Program")
total = int(input("Enter A number: "))
while yn.lower() == 'y':
    int(total)
    X = int(input("Enter another number: "))
    print("D for Divide")
    print("M for Muliply")
    print("A for Add")
    print("S for Subtract")
    op = input("Enter What Operator you would like to use: ")
    total = Calculator(total, op, X)
    print("your total is: " + str(total))
    yn = input("Do you want to enter another value? ")


print("Thank you for using the program! Your total was " + str(total))