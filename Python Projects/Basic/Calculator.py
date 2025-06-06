"""
Build a calculator with basic GUI. It should add, subtract, multiple, and divide. 
"""

# libraries
from tkinter import *
from tkinter import ttk

def add(val_1, val_2):
    try:
        output = val_1 + val_2
    except ValueError:
        pass

def subtract(val_1, val_2):
    try:
        output = val_1 - val_2
    except ValueError:
        pass

def divide(val_1, val_2):
    try:
        output = val_1 / val_2
    except ValueError:
        pass

def multiply(val_1, val_2):
    try:
        output = val_1 * val_2
    except ValueError:
        pass


root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="5, 4, 12, 12")
mainframe.grid(column=0, row=0, sticky=(N, E, W, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

