import sys

#from aimgen.generator import Generator
from __aimgen__ import Generator

def main(debug=False, levelname=None):
    generator = Generator.create()
    generator.generate()
