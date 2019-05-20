import argparse
import pathlib
import encoder
import waveformer
import numpy as np
import matplotlib.pyplot as plt

t_sample=1/22050
nbr_sample=1000
step = 2*t_sample/nbr_sample
beta=0.01

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

    for i in range(14):
        x = np.arange(-t_sample, t_sample, step)-i*t_sample
        data = waves[i*nbr_sample:(i+1)*nbr_sample]
        plt.plot(x, data)
    plt.show()