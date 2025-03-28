import math

class Figur:
    def __init__(self):
        self.Name = "Figur"
    def Umfang(self):
        return 0
    def __str__(self):
        return self.Name

class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, Punkt2):
        return ((self.x - Punkt2.x)**2 + (self.y - Punkt2.y)**2)**0.5

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

class Dreieck(Figur):
    def __init__(self, a, b, c):
        super().__init__()
        self.Name = "Dreieck"
        self.a = a
        self.b = b
        self.c = c

    def Umfang(self):
        return round( self.a.distance(self.b) + self.b.distance(self.c) + self.c.distance(self.a),2)

    def __str__(self):
        return self.Name + " " + str(self.a) + ", " + str(self.b) + ", " + str(self.c)


class Rechteck(Figur):
    def __init__(self, P1, P2):
        super().__init__()
        self.Name = "Rechteck"
        self.P1 = P1
        self.P2 = P2

    def Umfang(self):
        breite = abs(self.P2.x - self.P1.x)
        hoehe = abs(self.P2.y - self.P1.y)
        return round (2 * (breite + hoehe),2)

    def __str__(self):
        return self.Name + " " + str(self.P1) + " - " + str(self.P2)


class Kreis(Figur):
    def __init__(self, Mittelpunkt, Radius):
        super().__init__()
        self.Name = "Kreis"
        self.m = Mittelpunkt
        self.r = Radius

    def Umfang(self):
        return round (2 * math.pi * self.r,2)

    def __str__(self):
        return self.Name + " M=" + str(self.m) + " r=" + str(self.r)
    

class Polygon(Figur):
    def __init__(self, Ecken):
        super().__init__()
        self.Name = "Polygon"
        self.Ecken = Ecken

    def Umfang(self):
        u = 0
        for i in range(len(self.Ecken)):
            p1 = self.Ecken[i]
            p2 = self.Ecken[(i+1) % len(self.Ecken)]
            u = u + p1.distance(p2)
        return round(u,2)

    def __str__(self):
        text = self.Name
        for punkt in self.Ecken:
            text = text + " " + str(punkt)
        return text
    

P1 = Punkt(0, 0)
P2 = Punkt(10, 0)
P3 = Punkt(10, 15)
P4 = Punkt(0, 15)
P5 = Punkt(5, 6)


k = Kreis(Punkt(2.3, 4.2), 3.4)
print(k)
print("Umfang:", k.Umfang())


r = Rechteck(P1, P2)
print(r)
print("Umfang:", r.Umfang())


d = Dreieck(P1, P2, P3)
print(d)
print("Umfang:", d.Umfang())


poly = Polygon([P1, P2, P3, P4, P5])
print(poly)
print("Umfang:", poly.Umfang())