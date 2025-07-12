import time

class SelfCheckout:
    def __init__(self):
        self.menu = {
            "1": {"item": "Pepperoni Pizza", "price": 12.99},
            "2": {"item": "Margherita Pizza", "price": 10.99},
            "3": {"item": "Vegetarian Pizza", "price": 11.99},
            "4": {"item": "Coke", "price": 1.99},
            "5": {"item": "Sprite", "price": 1.99},
            "6": {"item": "Water", "price": 0.99},
        }
        self.cart = []

    def display_menu(self):
        print("\n--- Pizza Checkout Menu ---")
        for key, value in self.menu.items():
            print(f"{key}. {value['item']:<20} ${value['price']:.2f}")
        print("-------------------------")

    def add_item_to_cart(self, item_key):
        if item_key in self.menu:
            self.cart.append(self.menu[item_key])
            print(f"{self.menu[item_key]['item']} added to cart.")
        else:
            print("Invalid item number.")

    def view_cart(self):
        print("\n--- Your Cart ---")
        if not self.cart:
            print("Your cart is empty.")
        else:
            total = 0
            for item in self.cart:
                print(f"- {item['item']:<20} ${item['price']:.2f}")
                total += item['price']
            print("-----------------")
            print(f"Total: ${total:.2f}")
        print("-----------------")

    def checkout(self):
        if not self.cart:
            print("\nYour cart is empty. Please add items before checking out.")
            return

        total = sum(item['price'] for item in self.cart)
        print("\n--- Checkout ---")
        print(f"Your total is: ${total:.2f}")

