
import time
import json

from pathlib import Path
from shutil import move

psx=lambda fpath: fpath.as_posix()
unpck=lambda lst: " ".join(map(str, lst))
lcltime=lambda timestamp: time.localtime(int(timestamp))

chk={
    'spce': lambda lst: [pth for pth in lst if len(psx(pth).split()) > 1],
    'cse': lambda lst: [pth for pth in lst if pth.name[0].isupper()],
    }

srch={
    'sfx': lambda ext, dnm: list(Path(dnm).glob('**/*' + ext)),
    'pfx': lambda pfx, dnm: list(Path(dnm).glob('**/' + str(pfx) + '*')),
    'strpth': lambda strng, dnm: list(Path(dnm).glob('**/*' + str(strng) + '*')),
    'strlst': lambda strng, lst: [rslt for rslt in lst if strng in rslt],
    }

strng={
    'rplc': lambda char: char.replace(' ', '-'),
    'lwr': lambda char: char.lower(),
    }

pthop={
    'ls': lambda dname: list(Path(dname).iterdir()),
    'mv': lambda fpath, dpath: move(psx(fpath), dpath),
    'rnm': lambda fpath: fpath.rename(strng['rplc'](psx(fpath))),
    }
    
def deetstrct(jsondecoded):
    """
    utility - probes decoded json object and returns its composition
        input - jsondecoded
        output - keys paired with value type (tuple)
    """
    dstrct={}
    if type(jsondecoded) == list:
        dstrct['list']={}
        for length, datastrct in enumerate(jsondecoded):
            dstrct[length]=datastrct
            if 'dict' in str(type(datastrct)):
                dstrct['keys']=[*datastrct]
        return dstrct
#        print(
#            f"data_structure[]:\t{type(datastrct)}")
#            f"keys: {[*datastrct]}") 
#        print(f"sublevel one")


def nexjsons(strngfilter=''):
    if len(strngfilter) == 0:
        return [jsn for jsn in pathsearch('json', 'nexus/')]
    else:
        return [jsn for jsn in pathsearch('json', 'nexus/') if strngfilter in psx(jsn)]

def json_decode(filepath):
    with open(filepath, 'r') as jsnr:
        data = json.load(jsnr)
    return data


def json_encode(dictionary, filepath):
    with open(filepath, 'w') as jsnw:
        json.dump(dictionary, jsnw)



# %load /home/altvu/canvas/vectorize.py
def trashr(ipath):
    p1 = subprocess.run(["trash", ipath])
    print(f"trash_list:\n")
    p2 = subprocess.run(["trash-list"])
