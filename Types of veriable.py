class Car:

    wheels = 4
    def __init__(self):
        self.mil = 10
        self.comp = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 15

print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)
