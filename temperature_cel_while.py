def celsius_to_fahrenheit(fahrenheit):
    celsius = (fahrenheit * 9/5) + 32
    return celsius

while True:
    
    celsius = float(input("Enter the current temperature in Celsius: "))

    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"\nIt is {fahrenheit:.2f} degrees Fahrenheit\n")

    Continue = input("Do you want to continue? (yes/no)").lower().strip()

    if Continue != "yes":
        break

print("Goodbye!")