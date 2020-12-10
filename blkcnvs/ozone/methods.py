from pathlib import Path
from shutil import move

posix=lambda fpath: fpath.as_posix()
rplace=lambda strng: strng.replace(' ', '-').lower()
unpack=lambda lst: " ".join(map(str, lst))
search=lambda strng, lst: [rslt for rslt in lst if strng in rslt.as_posix()]
spacechk=lambda lst: [pth for pth in lst if len(posix(pth).split()) > 1]
peek=lambda dname: list(Path(dname).iterdir())
shift=lambda fpath, dpath: move(posix(fpath), dpath)
rname=lambda fpath: fpath.rename(rplace(posix(fpath)))

def dctdetails(dct):
    """
    utility - probes dictionary object and returns its composition
        input - object name (dictionary)
        output - keys paired with value type (tuple)
    """
    objtype=lambda dct: [type(dct[key]) for key in [*dct]]
    lvlkeys=lambda dct: [key for key in [*dct]]
    lvlvaldeet=lambda dct: [dct[key] for key in [*dct]]
    layerdetail=tuple(zip(objtype(dct), lvlkeys(dct), lvlvaldeet(dct)))
    return layerdetail


def fixup(lvlkey):
    meta=[pth for pth in zn.peek(ozone[lvlkey][0]) if pth.name == '.meta']
    cntnt=[pth for pth in zn.peek(ozone[lvlkey][0])]
    return content

def json_decode(filepath):
    with open(filepath, 'r') as jsnr: 
        data = json.load(jsnr) 
    return data


