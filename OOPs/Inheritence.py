class Product:  # Super Class| Base Class| Parent Clas
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def display_product_details(self):
        print("Product Name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("You Saved: {}".format(self.you_save))
        print("Rating: {}".format(self.ratings))


class ElectronicItem(Product):  # Sub Class|Derived Class|Child Class
    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months

    def get_warranty(self):
        return self.warranty_in_months

    def display_Electronic_product_details(self):
        self.display_product_details()
        print("Warranty: {}".format(self.warranty_in_months))


class GroceryItem(Product):
    def set_expiryDate(self, expiryDate):
        self.expiryDate = expiryDate

    def get_expiryDate(self):
        return self.expiryDate

    def display_Grocery_Item_details(self):
        self.display_product_details()
        print("expiryDate: {}".format(self.expiryDate))


# p = Product("Book", 30, 10, 4.5)  # Book Product
# p.display_product_details()

# e_item = ElectronicItem("Camera", 45000, 39000, 4.5)
# e_item.set_warranty(24)
# e_item.display_Electronic_product_details()

e_grocery = GroceryItem("Vegetables", 200, 180, 5.0)
e_grocery.set_expiryDate("15-09-2023")
e_grocery.display_Grocery_Item_details()
