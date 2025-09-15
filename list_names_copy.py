def main():
    names = []

    print()
    
    while True:
        name = input("Enter a name and type 'done' to finish typing your list: ")
        
        if name.lower() == 'done':
            break
        
        names.append(name)

    names.copy()

    print("\nNames of list:")

    print(names)

    print("\nNames of list copied:")
    
    print(names.copy())

    print()

main()