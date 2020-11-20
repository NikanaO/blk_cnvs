#!/usr/bin/env python3

def set_background():
    size = width, height = 640, 480;
    bkgrnd = Image.new( "RGB", size,  "cyan" )
    bkgrnd.save(fname'_bg')

