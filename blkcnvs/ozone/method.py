
import time
import json

from pathlib import Path
from shutil import move

psx=lambda fpath: fpath.as_posix()

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
    'ls': lambda dname: list(Path(dname).iterdir())
    'mv': lambda fpath, dpath: move(psx(fpath), dpath)
    'rnm': lambda fpath: fpath.rename(strng['rplc'](psx(fpath)))
    }
    
def dctdetails(dct):
    """
    utility - probes dictionary object and returns its composition
        input - object name (dictionary)
        output - keys paired with value type (tuple)
    """
    objtype=lambda dct: [type(dct[key]) for key in [*dct]]
    lvlkeys=lambda dct: [key for key in [*dct]]
    layerdetail=zip(lvlkeys(dct), objtype(dct))
    return layerdetail


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


