#EXAMPLE 1
#class Product:
#    def __init__(self,description, id_num, price): #first parameter has to be 'self'
#        self.description = description # self basically does nothing, stores the variables within the object self
#        self.id_num = id_num
#        self.price = price
#    def __str__(self):
#        return f'product {self.description}, id {self.id_num} price {self.price}'

#p = Product('thinkpad', 0, 1299.95) #__init__() is called through the function within the class
#print(p)

#EXAMPLE2
#class Product:
#    current_id = 0 #static variable
#    def __init__(self,description, price): #first parameter has to be 'self'
#        self.description = description # self basically does nothing, stores the variables within the object self
#        self.id_num = Product.current_id
#        Product.current_id += 11
#        self.price = price
#    def __str__(self):
#        return f'product {self.description}, id {self.current_id} price {self.price}'

#p = Product('thinkpad', 1299.95) #__init__() is called through the function within the class
#print(p)


