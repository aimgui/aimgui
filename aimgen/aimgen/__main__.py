import sys

sys.path.append('../')

from generate.generator import Generator

if __name__ == '__main__':
    generator = Generator.create()
    generator.generate()