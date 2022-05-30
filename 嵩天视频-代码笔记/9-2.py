class Restaurant():
    """创建一个饭店类"""
    def __init__(self, restaurant_name, cuisine_type):  
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def descibe_restaurant(self):
        print("The restuarant's name is " + self.restaurant_name.title())
        print("The cuisine's type is " + self.cuisine_type)

    
    def open_restaurant(self):
        print("The restaurant is opening!")

    
restaurant = Restaurant('guyuehu', 'huicai')
print("My res's name is " + restaurant.restaurant_name)
print("My cuisine's type is " + restaurant.cuisine_type + "\n")
restaurant.descibe_restaurant()
restaurant.open_restaurant()

restaurant_two = Restaurant('meiwei', 'yuecai')
restaurant_two.descibe_restaurant()

restaurant_three = Restaurant('zhijia', 'chuancai')
restaurant_three.descibe_restaurant()
    
