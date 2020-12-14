#!/usr/bin/env python3

'''
blkcnvs

A module for improved graphics design, web and content development workflow

Usage : ---

'''
__version__ = '0.0.0'

#import os
#import subprocess
#import sys
#import time
#import warnings

from ozone import model, method

def main():
    """
    main - controls execution flow when run as script
    input - None
    output - module package output
    """

    unpack=method.unpack

    #zones=[Trail(posix(zn[0])) for zn in flowzone.values()]

    print(
        f"creative zones:\n"
        f"{unpack([zn for zn in model.ozones.keys()])}"
        )


if __name__ == "__main__":
    main()
