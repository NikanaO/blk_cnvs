#!/usr/bin/env python3
from pathlib import Path
from shutil import move

fltrdct={
    'jsons': lambda lst: [pth for pth in lst if pth.as_posix().endswith('json')],
    'imgs': lambda lst: [pth for pth in lst if pth.as_posix().endswith('png') or pth.as_posix().endswith('jpg')],
    'csvs': lambda lst: [pth for pth in lst if pth.as_posix().endswith('csv')],
    'txts': lambda lst: [pth for pth in lst if pth.as_posix().endswith('txt')],
    'webs': lambda lst: [pth for pth in lst if pth.as_posix().endswith('html') or pth.as_posix().endswith('css')]
    }

shiftdct=fltrdct.fromkeys(fltrdct.keys())
shiftdct['jsons']='/home/altvu/nexus/data/structured/jsons/'
shiftdct['imgs']='/home/altvu/studio/graphics/'
shiftdct['csvs']='/home/altvu/nexus/data/structured/csvs/'
shiftdct['txts']='/home/altvu/nexus/data/unstructured/'
shiftdct['webs']='/home/altvu/canvas/constructs/web/'

def peekdir(dname):
    peek=lambda dname: list(Path(dname).iterdir())
    return peek(dname)

def shiftit(fpath, dpath):
    posix=lambda fpath: fpath.as_posix()
    shift=lambda fpath, dpath: move(posix(fpath), dpath)
    return shift(fpath, dpath)

def main():
    dnloads='/home/altvu/portal/dnloads/'
    [shiftit(pth, shiftdct['txts']) for pth in fltrdct['txts'](peekdir(dnloads))]
    [shiftit(pth, shiftdct['csvs']) for pth in fltrdct['csvs'](peekdir(dnloads))]
    [shiftit(pth, shiftdct['imgs']) for pth in fltrdct['imgs'](peekdir(dnloads))]
    [shiftit(pth, shiftdct['jsons']) for pth in fltrdct['jsons'](peekdir(dnloads))]
    [shiftit(pth, shiftdct['webs']) for pth in fltrdct['webs'](peekdir(dnloads))]
    
if __name__ == "__main__":
    main()


