def main():
    names = []

    while True:
        name = input("\nEnter a name and type 'done' to finish typing your list: ")
        if name.lower() == 'done':
            break
        names.append(name)

    name_extend = names.extend(['Christopher', 'Samuel', 'Joshua'])

    print("Final list of names:", names)
    print()
main()