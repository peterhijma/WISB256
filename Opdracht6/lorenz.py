import numpy
from scipy.integrate import odeint
import math

class Lorenz(object):
    def __init__(self,inistate,sigma=10,rho=28,beta=8/3):
        self.inistate=inistate
        self.sigma=sigma
        self.rho=rho
        self.beta=beta
        
    def solve(self,T,dt):
        def ode(self,h,t):
            u = h[0]
            v = h[1]
            w = h[2]
            xdt = self.sigma*(v-u)
            ydt = u*(self.rho-w)-v
            zdt = u*v-self.beta*w
            return [xdt,ydt,zdt]
        tijd=numpy.arange(0,T,dt)
        return odeint(ode,self.inistate, tijd)

#sigma = 10
#rho = 28
#beta = 8/3
#L1 = Lorenz([-1,1,0],sigma,rho,beta)
#u1 = L1.solve(50,.01)
#L2 = Lorenz([-1.001,1.001,.001],sigma,rho,beta)
#u2 = L2.solve(50,.01)
#print(u1[0,0],u2[0,0]) # print values of x at t=0
#print(u1[-1,0],u2[-1,0]) # print values of x at t=50