def main():
    names = []

    print()

    while True:
        name = input(f"Enter a name. Type 'pop' to delete the last name on the list; type 'done' to finish typing your list: ")
        if name.lower() == 'pop':
            names.pop()
        elif name.lower() == 'done':
            if names:
                removed_name = name.pop()
                print(f"Removed {removed_name}")
            break
        names.append(name)
        print("Names entered: ")
    
    print(names)

main()