def classify_number():  # Function to classify a number as positive, negative, or zero
    while True:  # Loop to allow the user to classify additional numbers until they type 'exit'
        user_input = input("Enter a number (or type 'exit' to stop): ").strip().lower()

        if user_input == 'exit':  # Break condition
            print("Exiting the classification. Goodbye!")
            break

        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            number = int(user_input)  # Convert to integer if the input is valid
            if number > 0:
                print("The number is positive.")
            elif number < 0:
                print("The number is negative.")
            else:
                print("The number is zero.")
        else:
            print("Invalid input! Please enter a valid number or type 'exit' to stop.")

# Calling the function
classify_number()
