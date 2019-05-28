from math import cos
from math import pi
from math import sin
from math import sqrt

def root_raised_cosine(t, t_interval, beta):
    ##Added by Gonxhe
    assert T > 0    
    
    num = cos((1+beta)*pi*(t/t_interval)) + ((1-beta)*pi*sinc(t*(1-beta)/t_interval))/(4*beta)
    denom = 1-(4*beta*t/t_interval)**2
    coeff = (4*beta)/(pi*sqrt(t_interval))
    return coeff*num/denom

def sinc(x):
    if x == 0:
        return 1
    return sin(pi*x)/(pi*x)