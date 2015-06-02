import math

class Vector:
    def __init__(self, n, x = 0):
        x_list = []
        if type(x)==type(x_list):
            x_list = x
        else:
            for i in range(n):
                x_list.append(x)
        self.vectoren = x_list
        self.lengte = len(x_list)

    def __str__(self):
        nieuwe_string = ""
        for i in self.vectoren:
            element = "{0:.6f}".format(i)
            nieuwe_string = nieuwe_string + str(element) + "\n"
        return nieuwe_string
    
    def lincomb(self,other,alpha,beta):
        lin = Vector(other.lengte)
        for i in range(other.lengte):
            lin.vectoren[i] = alpha * self.vectoren[i] + beta * other.vectoren[i]
        return lin

    def scalar(self,alpha):
        return self.lincomb(self,alpha,0)

    def inner(self,other):
        inproduct = 0
        for i in range(self.lengte):
            inproduct = inproduct + self.vectoren[i]*other.vectoren[i]
        return inproduct

    def norm(self):
        return math.sqrt(self.inner(self))
        
u=Vector(3,3)
w=u.scalar(2)
print(w)