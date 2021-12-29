from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.name = name
        self.customers_cart = ShoppingCart()
        self.customers_items = self.customers_cart.products   #created this variable because previously the review_cart method was unable to iterate 
    
    def add_to_customers_cart(self, added_product):
        self.customers_cart.add_to_cart(added_product)

    def review_cart(self):
        for item in self.customers_items:
            print(item.name)     #added .name because previously it was printing every attribute of the item
