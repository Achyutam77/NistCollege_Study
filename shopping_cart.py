class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.price:.2f} x {self.quantity}"

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for p in self.products:
            if p.name == product.name:
                p.quantity += product.quantity
                return
        self.products.append(product)

    def remove_product(self, product_name, quantity=1):
        for p in self.products:
            if p.name == product_name:
                if p.quantity > quantity:
                    p.quantity -= quantity
                else:
                    self.products.remove(p)
                return

    def calculate_total(self):
        return sum(p.price * p.quantity for p in self.products)

    def show_cart(self):
        if not self.products:
            print("Cart is empty.")
        else:
            print("Cart contents:")
            for p in self.products:
                print(p)
            print(f"Total: {self.calculate_total():.2f}")

# Example usage:
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_product(Product("Apple", 0.99, 3))
    cart.add_product(Product("Banana", 0.59, 2))
    cart.show_cart()
    cart.remove_product("Apple", 1)
    cart.show_cart()