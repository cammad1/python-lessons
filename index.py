def main():
    names = []

    while True:
        name = input("Enter a name here and type 'done' when you're finished: ")

        if name.lower() == 'done':
            break
        names.append(name)

    print("\nList of names with indices: ")
    for i, name in enumerate(names, start=1):
        print(f"{i}: {name}")
    
main()