import utils.pulse as pulse
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



def sample(j):
    f = np.vectorize(pulse.root_raised_cosine)
    return f(ts - j*t_sample, t_sample, beta)
    

def get_basis(n):
    basis = sample(0)
    for j in range(1,n):
        basis = np.vstack((basis, sample(j)))
    
    return basis

def form(codewords):
    n = len(codewords[0])
    basis = get_basis(n)
    waves = []
    for i in range(codewords.shape[0]):
        # cw = codewords[i]
        # cw = cw.reshape((-1, 1))*basis
        # cw = cw.flatten()
        # waves = np.hstack((waves, cw))

        cw = codewords[i]
        cw = cw.reshape((-1, 1))*basis
        cw = np.sum(cw, axis=0)
        waves.append(cw)

    return np.array(waves)
    #return waves[nbr_sample:].flatten()

