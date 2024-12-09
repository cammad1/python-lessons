def main():
    
    names = []

    print()

    while True:
    
        name = input("Enter a name (or type 'done' to finish, or type 'remove' to delete a name):  ")
    
        if name.lower() == 'done':
                break
        
        elif name.lower() == 'remove':
            
            if names:
                
                name_removed = input(f"What name do you want removed? ")
            
            if name_removed in names:
                
                names.remove(name_removed)

                print(f"{name_removed} has been removed.")
            
        
            
            else:
                print("We had a problem removing this item from the list, either it is not included in the list or the list is empty. Please try again.")
        else:
             names.append(name)
    
    print(f"\nYou entered {len(names)} names. ")

    print("The names you entered are: ")
   
    for name in names:
        print(names)


main()