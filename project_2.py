# **CALCULATOR WITH HISTORY**   

# history_file = 'history.txt'

# def show_history():
#     file = open(history_file, 'r')
#     lines = file.readlines() 
#     if len(lines) == 0:
#         print ('No history found!')
#     else:
#         for line in reversed(lines):
#             print(line.strip())
#     file.close()    

# def clear_history():
#     file = open(history_file, 'w')
#     file.close()    
#     print('History cleared.')

# def save_to_history(equation, result):
#     file = open(history_file, 'a')
#     file.write(equation + '=' + str(result) + '\n')
#     file.close()    

# def calculate(user_input):
#     parts = user_input.split()  
#     if len(parts) != 3:
#         print('Invalid input')
#         return
    
#     num1 = float(parts[0])
#     op = parts[1]
#     num2 = float(parts[2])  

#     if op == '+':
#         result = num1 + num2
#     elif op == '-':
#         result = num1 - num2
#     elif op == '*':
#         result = num1 * num2
#     elif op == '/':
#         if num2 == 0:
#             print('Error')
#             return
#         result = num1 / num2
#     elif op == '^':
#         result = num1 ** num2
#     else:
#         print('Invalid operator')
#         return
    
#     if int(result) == result:
#         result = int(result)
#     print('result: ', result)
    
#     save_to_history(user_input, result)


# def main():
#     print('---SIMPLE CALCULATOR--')
#     while True:
#         user_input = input('Enter calculation or cmd (history, clear, exit):').strip()
#         if user_input == 'exit':
#             print('Goodbye')
#             break
#         elif user_input == 'history':
#             show_history()
#         elif user_input == 'clear':
#             clear_history() 
#         else:
#             calculate(user_input)
        
# main()


# ==============================
# SIMPLE CALCULATOR WITH HISTORY
# ==============================

# File to store history
HISTORY_FILE = "history.txt"


# ------------------------------
# Utility functions
# ------------------------------
def show_history():
    """Show past calculations (most recent first)."""
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()

        if not lines:  # if history file is empty
            print("No history found!")
        else:
            print("\n--- Calculation History ---")
            for line in reversed(lines):  # show latest first
                print(line.strip())
    except FileNotFoundError:
        print("No history file yet!")


def clear_history():
    """Clear all history."""
    with open(HISTORY_FILE, "w") as file:
        pass  # just opening in 'w' mode clears file
    print("History cleared.")


def save_to_history(equation, result):
    """Save calculation into history file."""
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{equation} = {result}\n")


# ------------------------------
# Calculator logic
# ------------------------------
def calculate(user_input):
    """Perform calculation based on user input."""

    try:
        parts = user_input.split()

        # Handle single number operations (square, sqrt, etc.)
        if len(parts) == 2:
            op = parts[0]
            num = float(parts[1])

            if op == "sqrt":  # square root
                result = num ** 0.5
            elif op == "square":  # square
                result = num ** 2
            elif op == "cube":  # cube
                result = num ** 3
            else:
                print("Invalid single-argument operation!")
                return

            print("Result:", result)
            save_to_history(user_input, result)
            return

        # Handle two number operations (+, -, *, /, ^)
        elif len(parts) == 3:
            num1 = float(parts[0])
            op = parts[1]
            num2 = float(parts[2])

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    print("Error: Division by zero!")
                    return
                result = num1 / num2
            elif op == "^":  # power
                result = num1 ** num2
            elif op == "%":  # modulus
                result = num1 % num2
            else:
                print("Invalid operator!")
                return

            # Format result (e.g. 5.0 → 5)
            if result.is_integer():
                result = int(result)

            print("Result:", result)
            save_to_history(user_input, result)

        else:
            print("Invalid input format!")

    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print("Unexpected error:", e)


# ------------------------------
# Main Program Loop
# ------------------------------
def main():
    print("--- SIMPLE CALCULATOR ---")
    print("Available operations:")
    print(" - Binary: +, -, *, /, ^, %")
    print(" - Unary: square <num>, cube <num>, sqrt <num>")
    print(" - Commands: history, clear, exit\n")

    while True:
        user_input = input("Enter calculation or command: ").strip().lower()

        if user_input == "exit":
            print("Goodbye 👋")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)


# Run program
if __name__ == "__main__":
    main()
