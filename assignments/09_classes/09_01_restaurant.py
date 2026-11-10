'''
difficulty 7/10



'''
class Restaurant:
    """ This will initialize the vaiables and self"""
    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize name + attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """ This will describe the restaurant"""
        print(f"The name of the restaurant is {self.restaurant_name} and the cuisine type is {self.cuisine_type}.")

python_cafe = Restaurant("Python Cafe", "Italian")


# print(f"Robert's restaurant is {python_cafe.restaurant_name}")

python_cafe.describe_restaurant()
