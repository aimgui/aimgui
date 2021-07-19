import os
import sys
sys.path.append(os.getcwd())

from __aimgen__ import Generator

def main():
    generator = Generator.create()
    generator.generate()
