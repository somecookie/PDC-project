import utils.pulse as pulse
import numpy as np


class Waveformer:
    """
    This class implements the waveform former of the transmitter
    """

    def __init__(self, codewords, t_sample=1/22050, nbr_sample=100, beta=0.5):
        """
        Constructor for the waveform former

        :param codewords: the codewords we are sending
        :param t_sample: the sampling period
        :param nbr_sample: the amount of samples we want when we discretize the basis
        :param beta: the beta parameter for the root-raised cosine
        """
        
        self.codewords = codewords
        self.n = codewords.shape[1]
        self.beta = beta
        
        self.t_sample = t_sample
        #self.nbr_sample = nbr_sample

        self.start = -2*t_sample
        self.end = (self.n+1)*t_sample
        #self.step = (self.end - self.start)/nbr_sample
        self.step = t_sample

        self.ts = np.arange(self.start, self.end, self.step)
        self.nbr_sample = len(self.ts)
        


    def discretize(self, j):
        """
        Discretize the root-raised cosine shifted by j*t_sample to the right

        :param j: shift to the right
        """

        f = np.vectorize(pulse.root_raised_cosine)
        return f(self.ts - j*self.t_sample, self.t_sample, self.beta)


    def get_basis(self):
        """
        Construct the basis of dimension self.n
        """

        basis = self.discretize(0)
        for j in range(1, self.n):
            basis = np.vstack((basis, self.discretize(j)))

        return basis


    def get_w(self, summation=True):
        """
        Build the discretized form of the waveform signal that the transmitter will send

        :param summation: boolean that indicates if we want the sum of the version of the signal
        """
        basis = self.get_basis()
        if summation:
            
            waves = []
            for i in range(self.codewords.shape[0]):
                cw = self.codewords[i]
                cw = cw.reshape((-1, 1))*basis
                cw = np.sum(cw, axis=0)
                waves.append(cw)

            return np.array(waves)
        else:
            
            waves = np.zeros(self.nbr_sample)
            for i in range(self.codewords.shape[0]):
                cw = self.codewords[i]
                cw = cw.reshape((-1,1))*basis
                cw = cw.flatten()
                waves = np.hstack((waves, cw))
            
            return waves[self.nbr_sample:].flatten()
