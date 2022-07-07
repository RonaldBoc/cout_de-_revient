class Item:
    def __init__(self, name, price = float, quantity = int):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    @classmethod
    
    def get_infos(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        return self(name, price, quantity)

    def show_infos(self):
        print(self.name, self.price, self.quantity)

produit1 = Item.get_infos()
produit1.show_infos()