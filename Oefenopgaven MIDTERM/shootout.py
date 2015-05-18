import math

vuurkracht=int(input())
zwaartekracht=int(input())
afstand=int(input())

angle = (math.asin((zwaartekracht*afstand)/(vuurkracht*vuurkracht)))/2

round(angle,2)
print("{0:.2f}".format(angle))