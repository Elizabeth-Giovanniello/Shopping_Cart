class ShoppingCart:
    def __init__(self):
        self.products = []
    
    def calculate_total_price(self):
        self.total_price = 0   #chose to pass the values in as floats. But could also pass them in as strings and add a step here to convert them to floats so we could find their sum
        for item in self.products:
            self.total_price += item.price
        return round(self.total_price, 2) #for some reason it was returning a super long decimal, so I added a round function to limit it to 2 decimal points
    
    def add_to_cart(self, new_product):
        self.products.append(new_product)

    def empty_cart(self):
        self.products = []  #resets it back to how it was in the beginning, empty but prepared to accept a list (so a customer's cart could be empty but still usable)

    