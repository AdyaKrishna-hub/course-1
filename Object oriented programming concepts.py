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

#HW1
#PART1
#class is a template/blueprint for a new data type. An object is a specific instance of this class
#PART2
#class passenger has a relationship of dependency with the class transportation
#Class Table has a relationship of inheritance with Furniture

#HW2
#freezer and fridge are classes that have a relationship of inheritance from ColdStorage, hence ColdStorage is a superclass of both.
#ColdProduct has a relationship of dependency with ColdStorage. Hence, ColdProduct uses ColdStorage
#Cold Product has a relationship of inheritance with Product, hence, ColdProduct extends Product.
#Class Product has a relationship of aggregation with  class Storage. Hence, Storage contains objects of Product
#ColdStorage has a relationship of inheritance with the class Storage. Hence, Storage is a superclass consisting of ColdStorage, which consists of Freezer and Fridge

#HW3
class Point: #point is a class identifier here
    def __init__(self,x,y): #x is a parameter variable here
        self.x=x #x is an instance variable here 
        self.y=y
    def __str__(self):
        s = f'({self.x},{self.y})'
        return s
def origin():
    x = Point(0,0) #x is a local variable here #constructor of the class is a class identifier here #4.1 new object is created
    return x
x = origin() #global variable
print(x) #4.2, prints string in readable form

#PART2:
#static variable is not present in this code




