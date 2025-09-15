def main():
    names = []

    print()

    while True:
        name = input(f"Enter a name and either type 'clear' to clear the names, or type 'done' to finish typing your list: ")
        if name.lower() == 'clear':
            names.clear()
            
        elif name.lower() == 'done':
            break
        names.append(name)
        print("Names entered: ")
    
    print(names)

main()
