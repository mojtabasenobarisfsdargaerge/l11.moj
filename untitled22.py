class Product:
    def __init__(self,name,price,stock,sell_count):
        self.name =name
        self.price =price
        self.sell_count =sell_count
        self.stock =stock
    def show(self):
        print(f"name :{self.name} price :{self.price} stock :{self.stock} sell_count :{self.sell_count} ")
    def sell(self,quantity):
        self.stock -=quantity
        self.sell_count +=quantity
    def restock(self,quantity):
        self.stock +=quantity
    def apply_discount(self,percentage):
        self.price =self.price * percentage
    def is_available(self):
        if self.stock == 0:
            raise ValueError("???")
class Location:
    def __init__(self, address, x_cordinate, y_cordinate):
        self.address = address
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate

    def calculate_distance(self, other_location):
        if not isinstance(other_location, Location):
            raise NotImplementedError("location should be from class location")
        x_distance = other_location.x_cordinate - self.x_cordinate
        y_distance = other_location.y_cordinate - self.y_cordinate
        import math
        return math.sqrt(x_distance ** 2 + y_distance ** 2)
class DigitalProduct(Product):
    def __init__(self,name,code,stock,sell_count,download_link):
        super().__init__(name,code,stock,sell_count)
        self.download_link =download_link
    def get_download_link(self):
        print("downlod shoro shod")
        import time
        time.sleep(15)
        print("rekhte shod")
        
    
n =DigitalProduct("s", 12322,123,123,43)
n.get_download_link()
    
class PhysicalProduct(Product):
    def __init__(self,name,code,stock,sell_count,m,weight,warehouse_location):
        super().__init__(name,code,stock,sell_count)
        self.m =m
        self.warehouse_location =warehouse_location
        self.weight =weight
    def calculate_shipping(self):
        n =self.m /10
        print(n)

    
    
    
    
    
    
    