from review.product import Product
from review.products import ListProduct
lp=ListProduct()
lp.add_product(Product(100,"Product 1",200,10))
lp.add_product(Product(101,"Product 2",100,50))
lp.add_product(Product(102,"Product 3",150,20))
lp.add_product(Product(103,"Product 4",120,25))
lp.add_product(Product(104,"Product 5",180,30))
print("List of Products:")
lp.print_products()
print("*"*50)
lp.desc_sort_products()
print("List of Products sorted by price:")
lp.print_products()

print("*"*50)
lp.desc_sort_products_2()
print("List of Products sorted by price 2:")
lp.print_products()

print("*"*50)
lp.desc_sort_products_3()
print("List of Products sorted by price 3:")
lp.print_products()