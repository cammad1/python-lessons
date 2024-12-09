def operation(first_number, second_number):
    first_number = float(input("Enter the first number. "))
    second_number = float(input("Enter the second number. "))

    Addition = first_number + second_number
    Subtraction = first_number - second_number
    Multiplication = first_number * second_number
    Division = first_number / second_number

    print(f"{Addition} = {first_number} + {second_number}")
    print(f"{Subtraction} = {first_number} - {second_number}")
    print(f"{Multiplication} = {first_number} * {second_number}")
    print(f"{Division} = {first_number} / {second_number}")

while True:
    want_to_continue = input((print("\nDo you want to continue? (Yes/No)"))).strip().lower()
    
    if want_to_continue == 'yes':
        operation(first_number, second_number)
    if want_to_continue != 'yes':
        print("Exiting the calculator. Bye!")
        break
