# Define functions for basic arithmetic operations
def add(x, y):
    return x + y



def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main program loop
while True:
    # Display a menu of options to the user
    print("\nOptions:")
    print("\nEnter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    
    user_input = input(": ")  # Prompt the user for input
    
    if user_input == "quit":
        break  # Exit the loop and end the program if the user enters 'quit'
    
    # Check if the user's input is a valid operation
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform the selected operation and print the result
        if user_input == "add":
            print("Result: ", add(num1, num2))
        elif user_input == "subtract":
            print("Result: ", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result: ", multiply(num1, num2))
        elif user_input == "divide":
            print("Result: ",divide(num1, num2))
        
    else:
        print("Invalid input")  # Display an error message for invalid input

# End of program

