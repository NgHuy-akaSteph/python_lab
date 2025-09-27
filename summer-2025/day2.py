from math import sqrt

class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y
    
    def distance(self, p2):
        return sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)
    
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        ab = self.a.distance(self.b)
        bc = self.b.distance(self.c)
        ca = self.c.distance(self.a)
        if max(ab, bc, ca) * 2 >= (ab + bc + ca):
            print("INVALID")
        else:
            print(f"{(ab + bc + ca):.3f}")
            
a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for index in range(t):
    triagle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
    triagle.perimeter()
    i += 6

