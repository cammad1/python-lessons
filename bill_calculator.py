"""
Problem Statement:
You are tasked with creating a Python program to 
calculate the total cost of a meal, including tax and tip. 
Your program should prompt the user to input the cost of the meal and the percentage of tip they want 
to leave. The program should then validate the tip percentage to ensure it is 
greater than or equal to 0. If the tip percentage is valid, the 
program should calculate the total cost including an 8% tax rate and the specified tip percentage.
Finally, the program should display the total cost of the meal.
Your task is to complete the Python program by implementing the 
calculate_total_cost() function. This function takes two parameters: meal_cost 
(the cost of the meal) and tip_percentage (the tip percentage to leave). It should return the total cost of the meal 
including tax and tip. If the tip percentage is less than 0, the function should print
"Please enter a valid tip percentage." and return None.
"""

def calculate_total_cost(meal_cost, tip_percentage):
    tax_rate = 0.08
    tax_amount = meal_cost * tax_rate
    tip_amount = meal_cost * (tip_percentage / 100)
    return meal_cost + tax_amount + tip_amount

meal_cost = float(input("\nEnter the cost of the meal: $"))
tip_percentage = float(input("Enter the tip percentage you want to pay"))

total_cost = calculate_total_cost(meal_cost, tip_percentage)

print(f"\nThe total cost of the meal, including tax and tip, is: ${total_cost:.1f}\n")