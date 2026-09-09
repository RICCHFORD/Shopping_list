from shopping_list_func import *

'''Shopping List Application'''


def main():

    shopping_list = []
    while True:
        print("shoping list main menu")
        print("1. Add item to the list")
        print("2. Remove item from the list")
        print("3. view items on the list")
        print("4. Clear the list")
        print("5. Exite")

        Option = int(input("Welcome. Chosse an option(1-5) :"))

        if Option == 1:
            add_item(shopping_list)

        elif Option == 2:
            remove_item(shopping_list)

        elif Option == 3:
            view_list(shopping_list)

        elif Option == 4:
            clear_list(shopping_list)

        elif Option == 5:
            print("Have a nice day.")
            break
        else:
            print("Ivalid option, try again.")
            
if __name__ == "__main__":
    main()
