class Product:
    def __init__(self,id=None, name=None,quality=None, price=None): #Constructor
        self.id = id
        self.name = name
        self.quality = quality
        self.price = price

    def __str__(self): #Tự động thực thi khi xuất đối tượng
        return f"{self.id} {self.name} {self.quality} {self.price}"