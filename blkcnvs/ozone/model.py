# %load /home/altvu/canvas/projects/blkcnvs/zones/models.py
import methods

from pathlib import Path


def pathstamp(filepath):
    filetypes={
        'image': ('.jpg','.png','.svg', '.ppm','.jpeg'),
        'document': ('.pdf','.doc','.html', '.txt', '.save'),
        'code': ('.py','.pyc','.sh','.ipynb','.js'),
        'data': ('.json', '.xml'),
        'media': ('.mp3','.mp4'),
    }
    return unpack([filetype for filetype, extension in filetypes.items() if filepath.suffix in extension])

def pathsearch(qstrng, srchdir):
    return list(Path(srchdir).glob('**/*'+qstrng))


def fixup(lvlkey):
    meta=[pth for pth in zn.peek(ozone[lvlkey][0]) if pth.name == '.meta']
    cntnt=[pth for pth in zn.peek(ozone[lvlkey][0]) if pth.name == 'dnloads']
    return cntnt
    
class Trail:

    def __init__(self, label):
        self.label=Path(label).resolve()
        self.isdir=Path(label).is_dir()
                

    def __str__(self):
        if self.isdir:
            return f"{self.label} directory trail"
        else:
            return f"{self.label} file trail"

