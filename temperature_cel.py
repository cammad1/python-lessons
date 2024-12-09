def celsius_to_fahrenheit(celsius, fahrenheit):
    fahrenheit = (9/5 * celsius) + 32
    return fahrenheit

celsius = float(input("\nEnter the current temperature in Celsius. "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"\n{celsius} degrees celsius is equal to {fahrenheit:.2f} degrees fahrenheit.\n")
