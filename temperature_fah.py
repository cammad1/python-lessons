def fahrenheit_to_celsius(fahrenheit):    
    celsius = (fahrenheit - 32) * 5/9
    return celsius


while True:
    
    fahrenheit = float(input("\nEnter the current temperature in Fahrenheit: "))

    celsius = fahrenheit_to_celsius(fahrenheit)

    print(f"\nIt is {celsius:.2f} degrees celsius\n")

    Continue = input("Do you want to continue? (yes/no)").lower().strip()

    if Continue != "yes":
        break

print("Goodbye!")