#!/usr/bin/env python3

'''
blkcnvs

A module for improved graphics design, web and content development workflow

Usage : ---

'''
__version__ = '0.0.0' 

import os
import subprocess
import sys
import time
#import warnings

#from PIL import Image
system=os.system
sleep=time.sleep

def confirm_import():
  width=pane_size()
  impmsgh=f"{__name__} imported"
  print(f"{impmsgh:.^{width}}")
  clear()

if __name__ != "__main__":
  confirm_import()


def main():
    """
    main - controls execution flow when run as script
    input - None
    output - module package output
    """
    width=pane_size()
    runmsgh=f"{__file__} executed without error"
    print(f"{runmsgh:.^{width}}")
    clear()

if __name__ == "__main__":
    main()
