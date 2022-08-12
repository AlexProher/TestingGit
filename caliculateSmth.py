class Triangle:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def calculateTriangleSquare(self):
        p = (self.a+self.b+self.c)/2
        return(p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

    def __str__(self):
        return (f'a = {self.a}, b = {self.b}, c = {self.c}')
