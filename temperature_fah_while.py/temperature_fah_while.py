def fahrenheit_to_celsius(fahrenheit):    
        celsius = (fahrenheit - 32) * 5/9
        return celsius

while True:
    
    fahrenheit = float(input("\nEnter the current temperature in Fahrenheit: "))

    celsius = fahrenheit_to_celsius(fahrenheit)

    print(f"\nIt is {celsius} degrees celsius\n")

    yes_no = input("Do you want to continue? (yes/no)".lower().strip())

    if yes_no == "yes":
        fahrenheit_to_celsius(fahrenheit)

    else:
        break