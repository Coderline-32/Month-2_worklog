class ShoppingCart:
    def __init__(self):
        self.items_picked = {}
        self.items_price = {}

    def is_empty(self):
        return len(self.items_picked) == 0

    def add_item(self, productName, quantity, price):
        if productName in self.items_picked:
            self.items_picked[productName] += quantity
        else:
            self.items_picked[productName] = quantity
            self.items_price[productName] = price

    def remove_items(self, item):
        if item in self.items_picked:
            del self.items_picked[item]
            del self.items_price[item]
        else:
            print("Item not found!")

    def update_quantity(self, item, quantity):
        if item in self.items_picked:
            self.items_picked[item] = quantity
        else:
            print("Item not in cart.")

    def show_items_price(self):
        return self.items_price

    def show_items_quantity(self):
        return self.items_picked

    def calculate_price(self):
        total = 0
        for item in self.items_picked:
            total += self.items_price[item] * self.items_picked[item]
        return total

    def print_receipt(self):
        print("\n--- Receipt ---")
        for item in self.items_picked:
            quantity = self.items_picked[item]
            price = self.items_price[item]
            item_total = quantity * price
            print(f"{item.title()}: Quantity = {quantity}, Price = {price}, Total = {item_total}")
        print(f"Total: {self.calculate_price()}")

def prompt_User():
    print("Welcome to Kenuwn Sales store: \n")
    cart = ShoppingCart()

    while True:
        item = input("Enter the name of goods to buy: ").strip()
        try:
            price = float(input("Enter the item price: "))
            quantity = int(input(f"Enter amount of {item} to buy: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        cart.add_item(item, quantity, price)

        add_more = input("Do you want to add more items? (yes/no): ").strip().lower()
        if add_more != "yes":
            break

    remove_inquiry = input("Do you want to remove any item? (yes/no): ").lower()
    if remove_inquiry == "yes":
        remove_item = input("Enter item name to remove: ")
        cart.remove_items(remove_item)

    cart.print_receipt()

prompt_User()
