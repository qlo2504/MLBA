class ListProduct:
    def __init__(self):
        self.products = []
    def add_product(self, p):
        self.products.append(p)
    def print_products(self):
        for p in self.products:
            print(p)

    def desc_sort_products(self):
        for i in range (0,len(self.products)):
            for j in range (i+1,len(self.products)):
                pi=self.products[i]
                pj=self.products[j]
                if pi.price < pj.price:
                    self.products[j]=pi
                    self.products[i]=pj

    def desc_sort_products_2(self):
        self.products=sorted(self.products, key=lambda x: x.price, reverse=True)

    def desc_sort_products_3(self):
        result = []
        items = self.products[:]  # copy để không làm hỏng danh sách gốc
        while items:
            max_item = max(items, key=lambda p: p.price)
            result.append(max_item)
            items.remove(max_item)
        self.products = result


