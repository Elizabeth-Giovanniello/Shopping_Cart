#from product import Product

class ShoppingCart:
    def __init__(self):
        self.products = []
    
    def calculate_total_price(self):
        self.total_price = 0
        for item in self.products:
            self.total_price += item.price
        return self.total_price
    
    def add_to_cart(self, new_product):
        self.products.append(new_product)

    def empty_cart(self):
        self.products = []

    