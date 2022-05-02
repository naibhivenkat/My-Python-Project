class Computer:
    def config(self):
        print("i5, 16gb, 1TB")


comp1 = Computer()
comp2 = Computer()


Computer.config(comp1)


comp2.config()



