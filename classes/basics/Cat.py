class Cat:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi, my name is " + self.name)

    def greet(self, someone):
        print(f'Hi {someone}! My name is {self.name}')


chirola = Cat("chirola")

chirola.greet("bolainas")
