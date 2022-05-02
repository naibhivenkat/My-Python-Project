class Computer:

    def __init__(self):
        self.name = 'Venkat'
        self.age = 30

    def update(self):
        self.age = 35


c1 = Computer()
c2 = Computer()

c1.name = 'Naibhi'
c1.age = 50

c1.update()

print(c1.age)
print(c2.name)


