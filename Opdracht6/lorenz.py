import numpy
from scipy import odeint
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