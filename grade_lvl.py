def grade_lvl(age):
    if age < 0:
        print("\nInvalid age\n")
    
    elif age >= 0 and age <= 4:
        print("\mYou are not old enough to go to school yet\n")
    
    elif age >= 5 and age <= 11:
        print("\nYou are in elementary school\n")
        
    elif age >= 12 and age <= 14:
        print("\nYou are in middle school\n")

    elif age >= 14 and age <= 18:
        print("\nYou are in high school\n")

    else:
        print("\nYou are in college or above\n")


while True:
    try:
        age = int(input("Type in your age here."))
        grade_lvl(age)
    except ValueError:
        print("\nPlease enter a valid age.")
        
    continue_prompt = input("\nDo you want to enter another age? (yes/no)").lower().strip()

    if continue_prompt != "yes":
        break

