
import json
import subprocess

from pathlib import Path
from shutil import copy, move
from functools import reduce

psx=lambda fpath: fpath.as_posix()
ls=lambda dname: list(Path(dname).iterdir())
cp=lambda fpath, dpath: copy(psx(fpath), dpath)
mv=lambda fpath, dpath: move(psx(fpath), dpath)
srchpth=lambda strng, drctry: [*Path(drctry).glob('**/*'+strng+'*')]
srchlst=lambda strng, lst: [rslt for rslt in lst if strng in rslt]
unpck =lambda lst: " ".join(map(str, lst))
psxlst=lambda lst: [pth.as_posix() for pth in lst]

def _lst_tags(bktags):
          clntags=[]
          for item in bktags:
              if len(item) > 0:
                  clntags.append(item.strip())
          tagdata=[]
          for item in clntags:
              _, data=item.split('.')
              tagdata.append(data.strip())
          tagnames=[]
          for data in tagdata:
              tag=[tg for tg in data.split() if '(' not in tg]
              tagnames.append(unpck(tag))
          return tagnames

def get_tags():
        p1=subprocess.run(
            [
                "buku",
                "--np",
                "--stag",
            ],
            stdout=subprocess.PIPE,
            text=True,
        )
        return p1.stdout.splitlines()

tags=lambda : _lst_tags(get_tags())

def shortdate():
    from datetime import datetime
    now=datetime.now()
    today=now.strftime("%d%m")
    return today

def scan(fpath):
    data=[]
    with open(fpath) as file:
        for line in file:
            data.append(line.rstrip())
    return data

def burn(fpath, *data):
    with open(fpath, 'a') as file:
        for point in data:
            file.write(psx(point)+"\n")

def dcode(fpath):
    with open(fpath, 'r') as jsnr:
        data = json.load(jsnr)
    return data

def ecode(dictionary, fpath):
    with open(fpath, 'w') as jsnw:
        json.dump(dictionary, jsnw)

def duplicates(directory='.'):
    p1=subprocess.run(
        [
            "fdupes",
            "--order=name",
            "-dNI",
            directory,
        ],
        stdout=subprocess.PIPE,
        text=True,
    )
    return p1.stdout.splitlines()


    
spcecse=lambda directory: [psx(pth).replace(' ', '-') for pth in ls(directory)]
vidrnm=lambda vpth, nunme: vpth.rename(vpth.as_posix().replace(vpth.name.split('.')[0], nunme))


def timeprse(dbltime):
    import time
    fulltime=time.ctime(dbltime)
    return fulltime
    
    
