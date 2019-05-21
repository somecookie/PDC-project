from math import cos
from math import pi
from math import sin
from math import sqrt
import numpy as np

t_sample=1/22050
nbr_sample=100
start = -2*t_sample
end = 15*t_sample
step = (end - start)/nbr_sample
beta=0.5
ts = np.arange(start, end, step)
if len(ts) != nbr_sample:
        ts = ts[:nbr_sample]

def root_raised_cosine(t):
    num = cos((1+beta)*pi*(t/t_sample)) + ((1-beta)*pi*sinc(t*(1-beta)/t_sample))/(4*beta)
    denom = 1-(4*beta*t/t_sample)**2
    coeff = (4*beta)/(pi*sqrt(t_sample))
    return coeff*num/denom

def sinc(x):
    if x == 0:
        return 1
    return sin(pi*x)/(pi*x)

def sample(j):
    f = np.vectorize(root_raised_cosine)
    return f(ts - j*t_sample)
    

def get_basis(n):
    basis = sample(0)
    for j in range(1,n):
        basis = np.vstack((basis, sample(j)))
    
    return basis

def form(codewords):
    n = len(codewords[0])
    basis = get_basis(n)
    waves = np.zeros(nbr_sample)
    for i in range(codewords.shape[0]):
        cw = codewords[i]
        cw = cw.reshape((-1,1))*basis
        cw = cw.flatten()
        waves = np.hstack((waves, cw))
    
    return waves[nbr_sample:].flatten()

