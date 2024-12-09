def main():
    names = []

    print()

    while True:
        names = input("Enter a name (or type 'done' to finish if you don't want to reverse the order of your list, and type 'reverse' to reverse the order of the names.):  ")
    
        if names.lower() == 'done':
                break
        elif names.lower() == 'reverse':
            names.reversed()

    print(names)

main()
