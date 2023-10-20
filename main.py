class Product:

    all_products = []

    def __init__(self, id, name, price, quantity):
        # Run validations on the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        # Assign to self object
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.all_products.append(self)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def update_product(self, new_name, new_price, new_quantity):
        self.name = new_name
        self.price = new_price
        self.quantity = new_quantity

    @classmethod
    def add_new_product(cls):
        id = len(cls.all_products) + 1
        name = input("Enter the name of the new product: ")
        price = float(input("Enter the price of the new product: "))
        quantity = int(input("Enter the quantity of the new product: "))
        new_product = cls(id, name, price, quantity)
        print(f"New product {new_product.get_name()} added successfully!")

    @classmethod
    def delete_product(cls, product_id):
        for product in cls.all_products:
            if product.get_id() == product_id:
                cls.all_products.remove(product)
                print(f"Product {product.get_name()} deleted successfully.")
                cls.readjust_ids()
                return
        print("Product not found.")

    @classmethod
    def readjust_ids(cls):
        for i, product in enumerate(cls.all_products):
            product.id = i + 1

    def __str__(self):
        return f'Product({self.id},{self.name},{self.price}, {self.quantity})'

    def __repr__(self):
        return f'Product({self.id},{self.name},{self.price}, {self.quantity})'


class VendingMachine:
    def __init__(self):
        # Assign to self object
        self.money_inserted = 0.00
        self.balance = 0.00
        self.sold_quantity = 0.00
        self.sold_products = []

    def insert_money(self, money):
        if money <= 0.00:
            raise ValueError
        self.money_inserted += money

    def get_balance(self):
        return self.balance

    def get_sold_quantity(self):
        return self.sold_quantity

    def get_sold_products_list(self):
        return self.sold_products

    def sell_product(self, amount):
        self.balance += amount
        self.sold_quantity += 1


def main():
    product1 = Product(1, "Bounty", 7, 10),
    product2 = Product(2, "Snickers", 9, 10),
    product3 = Product(3, "Kit Kat", 5, 10),
    product4 = Product(4, "Toblerone", 20, 10),
    product5 = Product(5, "Ritter Sport", 12, 10),
    product6 = Product(6, "Mars", 8, 10)

    vending_machine = VendingMachine()

    print("Welcome to Chocolate Vending Machine, please select your choice:")
    for instance in Product.all_products:
        print(f"[{instance.id}] - {instance.name} - {instance.price:.2f} RON - {instance.quantity} items")
    print(f"[{len(Product.all_products) + 1}] - Exit store \n[{len(Product.all_products) + 2}] - SHOP")


    while True:
        try:
            # Get user input
            user_selection = int(input("Please enter the selected choice:"))
            # Check if user selected a product
            while user_selection < 1 or user_selection > len(Product.all_products)+2:
                user_selection = int(input("Invalid choice. Please re-enter:"))
            if int(user_selection) in range(1, len(Product.all_products) + 1):
                for prod in Product.all_products:
                    if prod.get_id() == user_selection:
                        prodObj = prod
                print(f"You have selected \"{prodObj.get_name()}\" - the price is {prodObj.get_price():.2f} RON")
                # Ask user to confirm the product selection or exit
                product_selection = int(input("Make your choice [\t 1 - Buy Product \t 2 - Exit selection]:"))
                if product_selection == 1:
                    # Check if inserted money is less than price
                    while vending_machine.money_inserted < prodObj.price:
                        print(f"You have inserted {vending_machine.money_inserted:.2f} RON into the machine so far.")
                        while True:
                            try:
                                money_to_insert = float(input("Please enter the amount of money you would like to insert: "))
                                vending_machine.insert_money(money_to_insert)
                            except ValueError:
                                continue
                            else:
                                break
                    # Sell the product and calculate available change
                    prodObj.quantity = prodObj.quantity - 1
                    vending_machine.money_inserted = vending_machine.money_inserted - prodObj.price
                    vending_machine.sell_product(prodObj.price)
                    vending_machine.sold_products.append(prodObj.name)
                    print(f"Thank you! Please take your \"{prodObj.name}\", the remaining quantity in the vending machine is {prodObj.quantity}.")
                    print(f"The remaining change in the machine is {vending_machine.money_inserted:.2f} RON.")
                    # Ask user if wants to buy another product or exit
                    another_product_selection = int(input("Do you want to buy another product? [\t 1 - Yes \t 2 - Exit selection]:"))
                    while another_product_selection == 1:
                        for instance in Product.all_products:
                            print(f"[{instance.id}] - {instance.name} - {instance.price:.2f} RON - {instance.quantity} items")
                        print(f"[{len(Product.all_products) + 1}] - Exit store \n[{len(Product.all_products) + 2}] - SHOP")
                        # Ask user to select a product
                        another_user_selection = int(input("Please enter the selected choice:"))
                        while another_user_selection < 1 or another_user_selection > len(Product.all_products) + 2:
                            another_user_selection = int(input("Invalid choice. Please re-enter:"))
                        if int(another_user_selection) in range(1, len(Product.all_products) + 1):
                            for prod in Product.all_products:
                                if prod.get_id() == another_user_selection:
                                    prodObj = prod
                            print(f"You have selected \"{prodObj.get_name()}\" - the price is {prodObj.get_price():.2f} RON")
                            # Ask user to confirm the product selection or exit
                            another_product_selection = int(input("Make your choice [\t 1 - Buy Product \t 2 - Exit selection]:"))
                            if another_product_selection == 1:
                                # Check if inserted money is less than price
                                if prodObj.quantity <= 0:
                                    print("Please select another product as we are out of stock")
                                    another_product_selection = int(input("Do you want to buy another product? [\t 1 - Yes \t 2 - Exit selection]:"))
                                else:
                                    while vending_machine.money_inserted < prodObj.price:
                                        print(f"You have inserted {vending_machine.money_inserted:.2f} RON into the machine so far.")
                                        while True:
                                            try:
                                                money_to_insert = float(input("Please enter the amount of money you would like to insert: "))
                                                vending_machine.insert_money(money_to_insert)
                                            except ValueError:
                                                continue
                                            else:
                                                break
                                    # Sell the product and calculate available change
                                    prodObj.quantity = prodObj.quantity - 1
                                    vending_machine.money_inserted = vending_machine.money_inserted - prodObj.price
                                    vending_machine.sell_product(prodObj.price)
                                    vending_machine.sold_products.append(prodObj.name)
                                    print(f"Thank you! Please take your {prodObj.name}, the remaining quantity in the vending machine is {prodObj.quantity}.")
                                    print(f"The remaining change in the machine is {vending_machine.money_inserted:.2f} RON.")
                                    another_product_selection = int(input("Do you want to buy another product? [\t 1 - Yes \t 2 - Exit selection]:"))
                    # Exit the selection
                    if another_product_selection == 2:
                        for instance in Product.all_products:
                            print(f"[{instance.id}] - {instance.name} - {instance.price:.2f} RON - {instance.quantity} items")
                        print(f"[{len(Product.all_products) + 1}] - Exit store \n[{len(Product.all_products) + 2}] - SHOP")
                # Exit the selection
                if product_selection == 2:
                    for instance in Product.all_products:
                        print(f"[{instance.id}] - {instance.name} - {instance.price:.2f} RON - {instance.quantity} items")
                    print(f"[{len(Product.all_products) + 1}] - Exit store \n[{len(Product.all_products) + 2}] - SHOP")
            # Exit
            if user_selection == len(Product.all_products) + 1:
                exit()
            # Admin section
            if user_selection == len(Product.all_products) + 2:
                print("This section is for Admin")
                print("\n1 - View Balance \t 2 - View Sold Products \t 3 - Update Product \t 4 - Add New Product \t 5 - Delete Product \t 6 - Exit Admin")
                admin_selection = int(input("Please enter your admin choice:"))
                while admin_selection < 1 or admin_selection > 6:
                    admin_selection = int(input("Invalid choice. Please re-enter:"))
                if admin_selection == 1:
                    print(f"Total balance is {vending_machine.get_balance()}")
                    print(f"Total sold quantity is {vending_machine.get_sold_quantity()}")
                elif admin_selection == 2:
                    print(f"Sold products are {vending_machine.get_sold_products_list()}")
                elif admin_selection == 3:
                    for instance in Product.all_products:
                        print(f"[{instance.id}] - {instance.name} - {instance.price:.2f} RON - {instance.quantity} items")
                    product_id = int(input("Enter the ID of the product you want to update: "))
                    # Find the product by ID
                    for prod in Product.all_products:
                        if prod.get_id() == product_id:
                            prodObj = prod
                            break
                    else:
                        print("Product not found.")
                        continue
                    # Input the new details
                    new_name = input("Enter the new name: ")
                    new_price = float(input("Enter the new price: "))
                    new_quantity = int(input("Enter the new quantity: "))
                    # Update the product
                    prodObj.update_product(new_name, new_price, new_quantity)
                    print(f"Product details updated successfully.")
                    for instance in Product.all_products:
                        print(f"[{instance.id}] - {instance.name} - {instance.price:.2f} RON - {instance.quantity} items")
                    print(f"[{len(Product.all_products) + 1}] - Exit store \n[{len(Product.all_products) + 2}] - SHOP")
                elif admin_selection == 4:
                    Product.add_new_product()
                    for instance in Product.all_products:
                        print(f"[{instance.id}] - {instance.name} - {instance.price:.2f} RON - {instance.quantity} items")
                    print(f"[{len(Product.all_products) + 1}] - Exit store \n[{len(Product.all_products) + 2}] - SHOP")
                elif admin_selection == 5:
                    product_id =int(input("Enter the ID of the product you want to delete: "))
                    Product.delete_product(product_id)
                    for instance in Product.all_products:
                        print(f"[{instance.id}] - {instance.name} - {instance.price:.2f} RON - {instance.quantity} items")
                    print(f"[{len(Product.all_products) + 1}] - Exit store \n[{len(Product.all_products) + 2}] - SHOP")
                elif admin_selection == 6:
                    for instance in Product.all_products:
                        print(f"[{instance.id}] - {instance.name} - {instance.price:.2f} RON - {instance.quantity} items")
                    print(f"[{len(Product.all_products) + 1}] - Exit store \n[{len(Product.all_products) + 2}] - SHOP")
                else:
                    print("That is an invalid choice.")
        except ValueError:
            continue
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())