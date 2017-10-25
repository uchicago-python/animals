from .dog import Dog

class Chihuahua(Dog):
    """Smallest breed of dog, named after Chihuahua, Mexico

    :param str name: Name of the Chihuahua
    :param int age: Age of the Chihuahua

    """

    def __init__(self, name, age):
        self.name = name
        self.age = age
