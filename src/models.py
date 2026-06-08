class Product:
    def __init__(self, product_id, title, category, price):
        self.product_id = product_id
        self.title = title
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.product_id} | {self.title} | {self.category} | ${self.price}"


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

        self.ratings = {}
        self.search_history = []
        self.cart_items = []

    def add_rating(self, product_id, rating):
        self.ratings[product_id] = rating

    def add_search(self, keyword):
        self.search_history.append(keyword)

    def add_cart(self, product_id):
        self.cart_items.append(product_id)