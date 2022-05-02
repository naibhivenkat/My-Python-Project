class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("The Config is", self.cpu, self.ram)


comp1 = Computer('i7', 8)

comp2 = Computer('AMD', 12)

comp1.config()
comp2.config()



