from product import Product

class ShoppingCart:
    def __init__(self):
        self.products = []
    
    def calculate_total_price(self):
       # self.total_price = ""
        #for item in self.products:
        pass
    
    def add_to_cart(self):
        self.new_product = Product()
        self.products.append(self.new_product)

    def empty_cart(self):
        self.products = []

    