import sys

#sys.path.append('../')

from aimgen.generator import Generator

def main(debug=False, levelname=None):
    generator = Generator.create()
    generator.generate()
