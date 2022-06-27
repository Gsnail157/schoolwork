class Item:
    def __init__(self, name, price, taxable):
        self.__name = name  # string
        self.__price = price
        self.__taxable = taxable  # boolean

    def __str__(self):
        return ("{:_<36}".format(self.__name) + "{:.2f}".format(self.__price))

    def getPrice(self):
        return self.__price
        pass

    def getTax(self, rate):
        if self.__taxable == True:
            tax_on_item = self.__price * rate
            return tax_on_item
        else:
            return 0
    pass


class Receipt:
    sub_total = 0
    tax = 0

    def __init__(self, tax_rate=0.07, purchase=[]):
        self.__tax_rate = tax_rate
        self.__purchase = []

    def __str__(self):
        for item in self.__purchase:
            print(item)
        print()
        return ("{:_<36}".format("Sub Total") + "{:.2f}\n".format(Receipt.sub_total) + "{:_<36}".format("Tax") + "{:.2f}\n".format(Receipt.tax) + "{:_<36}".format("Total") + "{:.2f}".format(Receipt.sub_total + Receipt.tax))

    def addItem(self, item):  # takes in an ITEM object as a parameter
        Receipt.sub_total += item.getPrice()
        Receipt.tax += item.getTax(self.__tax_rate)
        self.__purchase.append(item)
    pass


def ask_user_for_items():
    name = input("Enter Item name: ")
    price = float(input("Enter Item Price: "))
    taxable = (input("Is the item taxable (yes/no): "))
    if taxable == "yes":
        taxable = True
    else:
        taxable = False
    item = Item(name, price, taxable)
    receipt.addItem(item)


# Main Program
if __name__ == "__main__":
    print("Welcome to Receipt Creator")
    receipt = Receipt()
    while True:
        ask_user_for_items()
        response = input("Add another item (yes/no): ")
        if response == "yes":
            continue
        else:
            break
    print("----- Receipt time -----")
    print(receipt)
    print()
