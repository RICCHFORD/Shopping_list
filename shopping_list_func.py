
#shopping list

'''Removes items from your shopping list'''
def remove_item(shopping_list):
    remove = input('Which item do you wish to remove from your list? :')
    if remove in shopping_list:
        shopping_list.remove(remove)
    else:
        print(f'{remove} is not on your list.')




'''Add items to your shopping list'''
def add_item(shopping_list):
    num_items = int(input("How many items do you wish to add from your list? :"))
    for i in range(num_items):
        item_name = input(f"Enter the name of the item you wish to add to your list {i+1} :")
        shopping_list.append(item_name)
        print(f"{item_name} has been added to your list.")


'''View items in the list'''
def view_list(shopping_list):
    if shopping_list:
        print(shopping_list)
    else:
        print("Empty list.")


'''Clears list contents'''
def clear_list(shopping_list):
    if len(shopping_list) > 0:
        shopping_list.clear()
        print("Shopping list cleared")
    else:
        print("You haven't added anything to your list yet.")






