class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.last_transaction_amount = transaction_amount
        for _ in range(quantity):
            self.items.append(title)
        print(f"Added {quantity} x {title} at ${price:.2f} each. Total: ${self.total:.2f}")

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            removed_item = self.items.pop()
            self.total -= self.last_transaction_amount
            print(f"Removed {removed_item}. New total: ${self.total:.2f}")
        self.last_transaction_amount = 0

    def get_items(self):
        return self.items
