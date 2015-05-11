import random
import math

def direct_needle(n):
   n_hits=0
   for i in range(n):
      x_center=random.uniform(0.,0.5)
      phi=random.uniform(0,math.pi/2)
      x_tip=x_center - math.cos(phi)/2.
      if x_tip < 0: n_hits += 1
   return n_hits
for k in range(10):
   print k, direct_needle(100000)