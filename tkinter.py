# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""

# Function to update expression
# in the text entry box
def press(num):
    #point out the global expression variable
    global expression 

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    
    try:
        global expression
 