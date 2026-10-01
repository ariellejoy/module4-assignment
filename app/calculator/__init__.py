""" 
This file is the "app/calculator.py" file. It contains a simple calculator that can add, subtract, multiply, 
and divide numbers based on what the user types.
"""

# First, we need to get some functions that can actually do the math for us. These functions (addition, 
# subtraction, multiplication, and division) are in another file called "operations.py" in the "app" folder.
# This is like opening a toolbox and pulling out the tools we need to do our math.

import sys
import readline #this will enable history and editing
from typing import List
from app.calculation import Calculation, CalculationFactory
from app.operations import Operations

#creating a function that will display a help message / instructions 
def display_help() -> None:
    """Display help message with instructions."""

    help_message = """
    REPL Calculator Help
    --------------------
    In order to use the REPL calculator: input <operation> <num1> <num2> to perform a specific operation with 2 numbers 
    
    Supported operations include: 
    - add
    - subtract (note: this subtracts the second number from the first)
    - multiply
    - divide (note: this divides the first number by the second)

    Some special commands that could be helpful: 
    - help : Displays this help message
    - history : Shows your history of calculations 
    - exit : Exits the calculator 

    Example operations: 
    add 1 1 
    subtract 5 3
    multiply 2 4
    divide 10 2
    """
    print(help_message)

#creating a function that will display calcultions history 
def display_history (history: List[Calculation]) -> None: 
    """Display history of calculations preformed during the session (read: python3 main.py is running and REPL app is open)"""

    if not history: 
        print("No calculations have been performed yet.")
    else: 
        print ("Calculation History:")
        for idx, calculation in enumerate(history, start=1):
            print(f"{idx}. {calculation}")

# Now we're going to create the main function called "calculator". 
# A function is just a block of code that does something when you call it, kind of like a recipe that tells the 
# computer what to do.
def calculator():
    """REPL calculator that performs addition, subtraction, multiplication, and division. This calculator now uses Calculation classes"""
    
    #initializing list to keep track of history
    history: List[Calculation] = []

    # First, we print a message to welcome the user to the calculator.
    print("Welcome to the calculator REPL! Type 'help' for more instructions or 'exit' to quit")
    
    # This is the part where the calculator keeps running. The 'while True' means we are going to keep 
    # doing something (in this case, asking the user for input) until we tell it to stop.
    while True:
        # Now we ask the user to type something, like "add 5 3". 
        # This will get the operation (like "add") and two numbers from the user.
        #user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: ")
        try: 
            user_input: str = input(">> ").strip()
            if not user_input:
                continue # pragma no cover

            command = user_input.lower() #this will handle special commands

            if command == "help":
                display_help()
                continue
            elif command == "history":
                display_history(history)
                continue
            # This part checks if the user typed "exit". If they did, we print a message and stop the calculator.
            #if user_input.lower() == "exit":
            elif command == "exit":
                print("Exiting calculator now... Thank you!")
                sys.exit(0)

            try: 
            # Now we split the input into three parts: the operation (add, subtract, etc.) and the two numbers.
                operation, num1_str, num2_str = user_input.split()
            # We have to make sure the numbers are actually numbers, so we convert them to floats.
            #num1, num2 = float(num1), float(num2)
                num1: float = float(num1_str)
                num2: float = float(num2_str)
            except ValueError:
            # If the user doesn't type something correctly, like typing letters where numbers should be, we show an error.
                print("Invalid input. Please follow the format: <operation> <num1> <num2>")
                print("Type 'help' for more instructions!")
                continue  # This "continue" means: try again by going back to the top of the loop.

            try: 
                calculation = CalculationFactory.create_calculation(operation, num1, num2)
            except ValueError as ve:
                print(ve)
                print("Type 'help' for more instructions and the list of supported operations!")
                continue  # This "continue" means: try again by going back to the top of the loop.

            # Now we check what operation the user asked for and call the right function (addition, subtraction, etc.).
            try: 
                result = calculation.execute()
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                print("Please try again!")
                continue  # This "continue" means: try again by going back to the top of the loop.  
            except Exception as e:
                print(f"An error has occurred during calculation: {e}")
                print("Please try again!")
                continue  # This "continue" means: try again by going back to the top of the loop.

             # Finally, we print the result of the operation (for example, "Result: 8").
            result_str: str = f"{calculation}"
            print(f"Result: {result_str}")
            history.append(calculation)
        
        except KeyboardInterrupt:
            # EAFP example for handling unexpected interruption
            # Instead of checking if the user pressed Ctrl+C before each input,
            # we handle the KeyboardInterrupt exception.
            print("\nKeyboard interrupt detected. Exiting calculator. Goodbye!")
            sys.exit(0)

        except EOFError:
            # EAFP example for handling EOF (Ctrl+D)
            # Similar to KeyboardInterrupt, we handle the EOFError exception.
            print("\nEOF detected. Exiting calculator. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    calculator() # pragma no cover

        #if operation == "add":
            #result = Operations.addition(num1, num2)  # We call the addition function to add the two numbers.
        #elif operation == "subtract":
            #result = Operations.subtraction(num1, num2)  # We call the subtraction function to subtract the two numbers.
        #elif operation == "multiply":
            #result = Operations.multiplication(num1, num2)  # We call the multiplication function to multiply the two numbers.
        #elif operation == "divide":
            #try:
               # result = Operations.division(num1, num2)  # We call the division function to divide the two numbers.
           # except ValueError as e:
                # This part handles the case where someone tries to divide by zero, which we can't do.
                # The division function will throw an error if someone tries dividing by zero, and we catch that error here.
                #print(e)  # Show the error message.
                #continue  # Go back to the top of the loop and try again.
        #else:
            # If the user types an operation we don't understand, we show them a message.
            #print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
            #continue  # Go back to the top of the loop and try again.

       