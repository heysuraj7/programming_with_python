# Functions for addition, subtraction, multiplication, and division
def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

def mul(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> str:
    if b == 0:
        return "Division by zero is not possible"
    return a / b

# Calculator function to allow user to select an operation, input two numbers, and display the result
def calculator():
    while True:
        print("\nPossible operations:")
        print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit")
        choice = input("Choose an operation (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        match choice:
            case '1':
                print(f"The sum of {a} and {b} is {add(a, b)}")
            case '2':
                print(f"The difference of {a} and {b} is {sub(a, b)}")
            case '3':
                print(f"The product of {a} and {b} is {mul(a, b)}")
            case '4':
                result = div(a, b)
                print(f"The division of {a} and {b} is {result}")
            case _:
                print("Invalid choice! Please select a valid operation (1-5).")

# Calling the calculator function
if __name__ == "__main__":
    calculator()
