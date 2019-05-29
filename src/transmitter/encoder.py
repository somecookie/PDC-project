import binascii
import numpy as np

class Encoder:
    """
    This class implements the encoder of transmitter
    """

    def __init__(self,text):
        """
        Constructor of the encoder

        :param text: the text in ascii format we want to encode
        """

        assert len(text) > 0
        self.text = text


    def to_binary(self):
        """Converts the text to a binary numpy array (where the 0 bits is -1)
        E.g., ab becomes
        [   
            [ 1  1 -1 -1 -1 -1  1]
            [ 1  1 -1 -1 -1  1 -1]
        ]

        """
        binary = []

        for c in self.text:
            ascii_val = ord(c)
            bits = bin(ascii_val)[2:]
            padding = "0"*(7-len(bits))
            bits = padding + bits
            bits = [int(b) for b in bits]
            binary.append(bits)
        
        binary = np.array(binary)
        binary[binary == 0] = -1

        return binary

    def convolutional_encoder(self,source):
        """Implements the convolutional encoder for one symbol
        
        :param source: the binary representation of the source symbol we want to transform using the convolutional encoder
        """
        source = source.flatten()
        k = source.shape[0]

        xs = np.ones((2*k,))
        for j in range(k):
            bj = source[j]
            bj_1 = source[j-1] if j-1 >=0 else 1
            bj_2 = source[j-2] if j-2 >=0 else 1
            
            xs[2*j-1] = bj*bj_2
            xs[2*j] = bj*bj_1*bj_2

        tmp = xs[-1]
        xs[1:] = xs[:-1]
        xs[0] = tmp
        return xs
            
    def get_codewords(self,symbols):
        """Converts the binary source symbols into the corresponding codeword using a convolutional encoder (see page 206)
        
        :param symbols: the binary source symbols for each character of the text
        """
        return np.apply_along_axis(self.convolutional_encoder,1,symbols)
        

    def encode(self):
        """Encode the given text using a convolutional encoder"""
        binary = self.to_binary()
        binary = self.get_codewords(binary)
        training_signal = self.encode_random_signal()
        np.savetxt("resources/training.txt", training_signal)
        binary = np.vstack((training_signal, binary, training_signal))
        return binary
    
    def encode_random_signal(self):
        """Encode the random binary sequence using a convolutional encoder"""
        rnd_binary = self.barker_code()
        print(rnd_binary)
        rnd_binary = self.get_codewords(rnd_binary.reshape((-1,7)))
        return rnd_binary
    
    def barker_code(self):
        barker = np.array([1,1,1,-1,-1,1,-1])
        if int(len(self.text)/4) > 0:
            barker = np.tile(barker, (int(len(self.text)/4), 1))
        return barker

    def random_binary(self):
        """
        Creates random binary numpy array of certain length. 
        These random texts will be added in the beginning and in the end of the true input we want to send.
        """
        random_binary = np.array([rnd.randint(0,1) for i in range(7)])
        random_binary[random_binary == 0] = -1
        ##We assume we need 25% of the length ot the true binary array in the beginning and in the end of our true binary array.
        ##For each character of my 25% of the text file, I create random binary arrays of length 8.
        for x in range(int(len(self.text)/4)-1):
            sig = np.array([rnd.randint(0,1) for i in range(7)])
            sig[sig == 0] = -1
            random_binary = np.vstack([random_binary,sig])
        return random_binary