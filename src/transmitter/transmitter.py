import argparse
import pathlib
import encoder

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