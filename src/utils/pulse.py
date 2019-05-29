from math import cos
from math import pi
from math import sin
from math import sqrt

def root_raised_cosine(t, t_sample, beta):
    assert t_sample > 0
    assert 0 < beta < 1
    num = cos((1+beta)*pi*(t/t_sample)) + ((1-beta)*pi*sinc(t*(1-beta)/t_sample))/(4*beta)
    denom = 1-(4*beta*t/t_sample)**2
    coeff = (4*beta)/(pi*sqrt(t_sample))
    return coeff*num/denom

def sinc(x):
    if x == 0:
        return 1
    return sin(pi*x)/(pi*x)