
import time
import json

from pathlib import Path
from shutil import move

posix=lambda fpath: fpath.as_posix()
rplace=lambda strng: strng.replace(' ', '-').lower()
unpack=lambda lst: " ".join(map(str, lst))
posix_search=lambda strng, lst: [rslt for rslt in lst if strng in rslt.as_posix()]
string_search=lambda strng, lst: [rslt for rslt in lst if strng in rslt]
spacechk=lambda lst: [pth for pth in lst if len(posix(pth).split()) > 1]
casecheck=lambda lst: [pth for pth in lst if pth.name[0].isupper()]
peek=lambda dname: list(Path(dname).iterdir())
shift=lambda fpath, dpath: move(posix(fpath), dpath)
rname=lambda fpath: fpath.rename(rplace(posix(fpath)))
lcltime=lambda timestamp: time.localtime(int(timestamp))

def pathsearch(qstrng, srchdir):
    return list(Path(srchdir).glob('**/*'+qstrng))

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
        return [jsn for jsn in pathsearch('json', 'nexus/') if strngfilter in posix(jsn)]

def json_decode(filepath):
    with open(filepath, 'r') as jsnr:
        data = json.load(jsnr)
    return data


def json_encode(dictionary, filepath):
    with open(filepath, 'w') as jsnw:
        json.dump(dictionary, jsnw)

