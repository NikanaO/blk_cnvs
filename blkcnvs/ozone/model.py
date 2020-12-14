#!/usr/bin/ env python3
from pathlib import Path

import method

pk=method.peek
psx=method.posix
unpck=method.unpack


def pathstamp(filepath):
    filetypes={
        'image': ('.jpg','.png','.svg', '.ppm','.jpeg'),
        'document': ('.pdf','.doc','.html', '.txt', '.save'),
        'code': ('.py','.pyc','.sh','.ipynb','.js'),
        'data': ('.json', '.xml'),
        'media': ('.mp3','.mp4'),
    }
    return unpck([filetype for filetype, extension in filetypes.items() if filepath.suffix in extension])

ozones={pth.parent.name: pth.parent for pth in Path.home().glob('*/.meta')}

class Zone:
    """overarching container for workflow units"""
    def __init__(self, label):
        self.label=Path(label).resolve()
        self.isdir=Path(label).is_dir()

    def contents(self):
        """returns contents of directory if object is directory"""
        if self.isdir:
            return [Zone(label).label for label in list(Path(self.label).iterdir())]
        else:
            return None

    def __str__(self):
        if self.isdir:
            return f"'{self.label.name}' contains {len(list(self.label.iterdir()))} paths"
        else:
            return None



