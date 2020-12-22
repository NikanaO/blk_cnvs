#!/usr/bin/env python3 


__version__ = '0.0.0'

import ozone.method as method
import ozone.model as model
import viz.styles as styles
import viz.view as view

def jsonvu(filename):
    decoded=mth.json_decode(filename)
    deetstrct=mth.deetstrct(decoded)
    pass

def main():
    ozones=[mod.Zone(pth.parent) for pth in mod.Path.home().glob('*/.meta')]
    print(f"ozones:\n") 
    for nm in ozones:
        print(f"{nm.label.name}")
        

if __name__ == "__main__":
	main()


