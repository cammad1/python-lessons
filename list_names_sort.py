def main():
    names = []

    print()
    
    while True:
        name = input("Enter a name and type 'done' to finish typing your list: ")
        
        if name.lower() == 'done':
            break
        
        names.append(name)

    names.sort()

    print("\nNames of list in alphabetical order: ")

    for name in names:
        print(name)
    
    print()

main()
