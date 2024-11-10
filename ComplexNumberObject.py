class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imagianary = b
        self.polarMagnitude = 0
        self.angle = 0
        self.findPolar()
        self.display()

    def findPolar(self):
        self.polarMagnitude = math.sqrt(pow(self.real, 2) + pow(self.imagianary, 2))
        self.angle = math.atan(self.imagianary/self.real)

    def display(self):
        if self.imagianary > -1:
            print(f"{self.real} + {self.imagianary}i")
        else:
            print(f"{self.real} {str(self.imagianary)[0]} {str(self.imagianary)[1:]}i")

        #Polar Form
        print(f"{self.polarMagnitude}(cos({self.angle}) + i sin({self.angle}))")
