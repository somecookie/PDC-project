import argparse
import pathlib
from transmitter.encoder import Encoder
from transmitter.waveformer import Waveformer
import numpy as np
import matplotlib.pyplot as plt


def parse_args():
    """Parse the arguments of the main"""
    parser = argparse.ArgumentParser(description="Produces the codewords from the given text file")
    parser.add_argument('-i', type=str, required=True, help='path to the intput .txt file')
    parser.add_argument('-o', type=str, required=True, help='path to the output .txt file')
    parser.add_argument('-d',type=bool, nargs='?', default=False, help='enable debug mode')
    parser.add_argument('-ns',type=bool, nargs='?', default=False, help='enable no summation')

    args = parser.parse_args()

    args.i = pathlib.Path(args.i).resolve(strict=False)
    if not (args.i.suffix == '.txt'):
        raise ValueError('Parameter[i] is not a .txt file.')
    
    args.o = pathlib.Path(args.o).resolve(strict=False)
    if not (args.o.suffix == '.txt'):
        raise ValueError('Parameter[o] is not a .txt file.')
    
    return args

if __name__ == "__main__":
    """
    This scripts takes a text file and convert it to discretized waveform signals.
    The signals are store in the desired output file.

    It takes the following arguments:
    -i: the input file
    -o: the output file
    [-d]: enable debug mode
    [-ns]: to indicate no summation
    """ 

    

    args = parse_args()

    summation = True if args.ns is not None else args.ns
    
    with open(args.i, "r") as file:
        text = file.read()

    enc = Encoder(text) 
    codewords = enc.encode()
    wf = Waveformer(codewords)
    waves = wf.get_w(summation)

    np.savetxt(args.o, waves.flatten())
    
    if args.d is None and summation:
        for i in range(codewords.shape[0]):
            data = waves[i]
            plt.plot(wf.ts, data)
        plt.show()
    elif args.d is None:
        for i in range(codewords.shape[1]):
            data = waves[i*wf.nbr_sample: (i+1)*wf.nbr_sample]
            plt.plot(wf.ts, data)
        plt.show()