age = int(input("Type in your age here."))

def grade_lvl():
    if age >= 0 and age <= 4:
        print("You are not old enough to go to school yet.")
    
    elif age >= 5 and age <= 11:
        print("You are in elementary school.")
        
    elif age >= 12 and age <= 14:
        print("You are in middle school.")

    elif age >= 14 and age <= 18:
        print("You are in high school.")

    elif age >= 18:
        print("You are in college or above")

grade_lvl()