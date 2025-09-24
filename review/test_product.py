from review.product import Product

p1=Product(100,"Thuốc lào",4,20)
print(p1)

p2=Product(200,"Thuốc ho",5,30)
p1=p2
print("Thông tin của p1=")
print(p1)
print("*"*50)
p1.name="Thuốc cảm cúm"
print("Thông tin của p2=")
print(p2)