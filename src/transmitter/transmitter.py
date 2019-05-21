import argparse
import pathlib
import encoder
import waveformer
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
        
    codewords = encoder.encode(text)
    waves = waveformer.form(codewords)

    basis = waveformer.get_basis(14)
    for i in range(14):
        data = waves[waveformer.nbr_sample*i:waveformer.nbr_sample*(i+1)]
        plt.plot(waveformer.ts, data)
    plt.show()