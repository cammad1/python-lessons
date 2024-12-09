
"""
Problem Statement:
You are tasked with developing a Python program to determine a person's eligibility for obtaining a driver's license based 
on their age. Your program should include a function called check_ license_eligibility(age) which takes an integer parameter 
age representing the age of the person. The function should print a message indicating whether the person is eligible for a 
driver's license, a learner's permit, or if they are not eligible yet. Your program should prompt the user to input their age 
and then call the check_ license _eligibility) function determine their eligibility based on the provided age. Write a Python 
script that implements the above requirements. Ensure that your code follows proper coding conventions and includes appropriate 
comments to explain the functionality of each section. Test your program with different age inputs to verify its correctness.
"""

age = int(input("Please enter your age here: "))

if age <= 15:
    print("Sorry, you are not eleigible for a learners permit!")

if age > 15:
    print("Congrats! You are eligible for a learner's permit!")

if age >= 18 and age <= 17:
    print("Congrats! You are eligible for a driver's lisence!")