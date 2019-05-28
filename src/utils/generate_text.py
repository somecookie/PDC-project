import argparse
import pathlib
import string
import random
"""
This script generates a textfile of a given size. It must be called the following way:
python generate_text.py -n number -o path/filename.txt
"""

parser = argparse.ArgumentParser(description="Generate automatically a textfile")
parser.add_argument('-n', type=int, required=True, help='size of the textfile')
parser.add_argument('-o', type=str, required=True, help='path to the generated .txt file')

args = parser.parse_args()

args.o = pathlib.Path(args.o).resolve(strict=False)
if not (args.o.suffix == '.txt'):
    raise ValueError('Parameter[o] is not a .txt file.')

size = args.n
path = args.o

text = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=size))

with open(path, 'w') as file:
    file.write(text)