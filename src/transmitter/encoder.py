import binascii
import numpy as np


def to_binary(text):
    """Converts the text to a binary numpy array
    E.g.: a -> 0b1100001 -> ['1' '1' '0' '0' '0' '0' '1']
    """
    binary = []

    for c in text:
        ascii_val = ord(c)
        bits = bin(ascii_val)[2:]
        padding = "0"*(7-len(bits))
        bits = padding + bits
        bits = [int(b) for b in bits]
        binary.append(bits)
    
    binary = np.array(binary)
    binary[binary == 0] = -1

    return binary

def convolutional_encoder(source):
    """Implements the convolutional encoder for one symbol"""
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
        


def get_codeword(symbols):
    """Converts the binary source symbols into the corresponding codeword using a convolutional encoder (see page 206)"""
    return np.apply_along_axis(convolutional_encoder,1,symbols)
    

def encode(text):
    """Encode the given text"""
    binary = to_binary(text)
    binary = get_codeword(binary)
    return binary
