

from pathlib import Path


pk=lambda dname: list(Path(dname).iterdir())
psx=lambda fpath: fpath.as_posix()
unpck=lambda lst: " ".join(map(str, lst))

class Drop:
    """the workflow unit akin to a file and nested within zones"""
    def __init__(self, label):
        self.label=Path(label).resolve()
        self.isfile=Path(label).is_file()

    def stamp(self):
        drops={
            'image': ('.jpg','.png','.svg', '.ppm','.jpeg'),
            'document': ('.pdf','.doc','.html', '.txt', '.save'),
            'code': ('.py','.pyc','.sh','.ipynb','.js'),
            'data': ('.json', '.xml'),
            'media': ('.mp3','.mp4'),
            }
        if self.isfile:
            return unpck([drop for drop, extension in drops.items() if self.label.suffix in extension])
        else:
            return None


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




