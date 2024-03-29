class MyClass:
    class_variable = "I am a class variable"
    # The __init__ method is a special method in Python classes and is used to initialize the instance's attributes.
    # The self parameter is a reference to the instance itself. It is automatically passed when you create an instance,
    # and you use it to refer to instance variables.

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    # Regular instance method
    def instance_method(self):
        print(f"Instance method called with {self.instance_variable}")

    # Static method
    @staticmethod
    def static_method(): # self is not required with static method
        print("Static method called")

# Creating an instance of MyClass
obj = MyClass("I am an instance variable")

# Calling instance method
obj.instance_method()
obj.static_method()

# Calling static method on the class
MyClass.static_method()
