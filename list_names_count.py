def main():
    names = []

    while True:
        name = input("\nEnter a name and type 'done' to finish typing your list: ")
        if name.lower() == 'done':
            break
        names.append(name)

        name_counter = names.count(name)
        
        print(f"The name '{name}' has been entered '{name_counter}' time(s)")

        if name.lower() == 'done':
            names.append(name)
        print("Names entered: ")
        
    print("Final list of names:", names)
    print()
main()