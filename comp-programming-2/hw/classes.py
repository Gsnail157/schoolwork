class ItemToPurchase:

    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total = 0
        total = self.item_price * self.item_quantity
        print(
            f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total}')

    def print_item_descriptions(self):
        print(f'{self.item_name}: {self.__item_description}')


class ShoppingCart:

    def __init__(self, customer_name='none', current_date='January 1,2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        if len(self.cart_items) == 0:
            print("Item not found in Cart. Nothing removed.")
            return
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return

    def modify_item(self, item_name, quantity):
        for item in self.cart_items:
            if item.item_name == item_name:
                item.item_quantity = quantity
                return
            else:
                print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total

    def get_cost_of_cart(self):
        total = 0

        for item in self.cart_items:
            total += item.item_quantity * item.item_price

        return total

    def print_total(self):
        print(f'OUTPUT SHOPPING CART')
        print(f'{self.customer_name} Shopping Cart - {self.current_date}')
        print(f'Number of Items: {cart.get_num_items_in_cart()}')
        print()
        if len(self.cart_items) == 0:
            print(f'SHOPPING CART IS EMPTY')
        for item in self.cart_items:
            total = 0
            total += item.item_price * item.item_quantity
            print(f'{item.item_name} @ {item.item_quantity} = ${total}')
        print()
        print(f'Total: ${cart.get_cost_of_cart()}')

    def print_description(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f'{self.customer_name} Shopping Cart - {self.current_date}')
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            print(f'{item.item_name}: {item.item_description}')


def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")


def execute_menu(choice, my_cart):
    if choice == "a":
        print("ADD ITEM TO CART")
        name = input("Enter the item name:\n")
        item_description = input(
            "Enter the item description:\n")
        price = float(
            input("Enter the item price:\n"))
        quantity = int(
            input("Enter the item quantity:\n"))
        item = ItemToPurchase(
            name, price, quantity, item_description)
        my_cart.add_item(item)

    elif choice == "r":
        print("REMOVE ITEM FROM CART")
        remove = input("Enter name of item to remove: ")
        my_cart.remove_item(remove)

    elif choice == "c":
        print("CHANGE ITEM QUANTITY")
        change = input("Enter the item name: ")
        num = input("Enter the new quantity:")
        my_cart.modify_item(change, num)

    elif choice == "i":
        my_cart.print_description()

    elif choice == "o":
        my_cart.print_total()


if __name__ == "__main__":
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    cart = ShoppingCart(name, date)
    print()
    print(f'Customer name: {cart.customer_name}')
    print(f'Today\'s date: {cart.current_date}')
    print()
    print_menu()
    print()
    choice = input("Choose an option:\n")
    while choice != "q":
        execute_menu(choice, cart)
        choice = input("Choose an option:\n")
