def main():
    names = []
    name_counter = 0
    while True:
        name = input("\nEnter in 'add', 'insert' or 'done' when you are finished.: ")
        if name.lower() == 'done':
            break
        names.append(name)

        if name.lower() == 'add':
            names.remove("add")
            input("\nEnter a name: ")
        
        if name.lower() == 'insert':
            names.remove('insert')
            input("\nEnter a name: ")
            position = int(input(f"Enter index (0 to {len(names)}): "))
            if 0 <= position <= len(names):
                names.insert(position, name)

    print(names)
main()