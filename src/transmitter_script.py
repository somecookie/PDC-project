import argparse
import pathlib
from transmitter.encoder import Encoder
from transmitter.waveformer import Waveformer
import numpy as np
import matplotlib.pyplot as plt


def parse_args():
    """Parse the arguments of the main"""
    parser = argparse.ArgumentParser(description="Produces the codewords from the given text file")
    parser.add_argument('-i', type=str, required=True, help='path to the generated .txt file')

    args = parser.parse_args()

    args.i = pathlib.Path(args.i).resolve(strict=False)
    if not (args.i.suffix == '.txt'):
        raise ValueError('Parameter[i] is not a .txt file.')
    return args

if __name__ == "__main__":
    args = parse_args()
    
    with open(args.i, "r") as file:
        text = file.read()

    enc = Encoder(text) 
    codewords = enc.encode()
    wf = Waveformer(codewords)
    waves = wf.get_w()

    for i in range(codewords.shape[0]):
        data = waves[i]
        plt.plot(wf.ts, data)
    plt.show()