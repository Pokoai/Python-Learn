class Restaurant():
    """创建一个饭店类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def descibe_restaurant(self):
        """描述餐馆的名字和类型"""
        print("The restuarant's name is " + self.restaurant_name.title())
        print("The cuisine's type is " + self.cuisine_type)

    
    def open_restaurant(self):
        print("The restaurant is opening!")     


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_icecream(self):
        for flavor in self.flavors:
            print("We have " + flavor + " icecream.")


icecreamstand = IceCreamStand('FrozenQueen', 'icecream')
icecreamstand.flavors = ['dsaf', 'gsg', 'yti']
icecreamstand. show_icecream()