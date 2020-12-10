
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


class File:
    """Class for organising units or bit in a domain."""
    filetypes={
        'image': ('.jpg','.png','.svg', '.ppm','.jpeg'),
        'document': ('.pdf','.doc','.html', '.txt', '.save'),
        'code': ('.py','.pyc','.sh','.ipynb','.js'),
        'data': ('.json', '.xml'),
        'media': ('.mp3','.mp4'),
    }
    def __init__(self, name):
        """
        initialises object with name and type
        """
        self.name=Path(name)

    def get_filetype(self):
        for filetype, extension in self.filetypes.items():
            if self.name.suffix in extension:
                return filetype
            elif posix(self.name).endswith('rc'):
                return 'configuration'
            else:
                return 'unknown'



class Folder:
    foldertypes={
        'user flow': ('.meta'),
        'git repo': ('.git', '.gitattributes', '.gitignore'),
        }

    def __init__(self, name):
        """
        initialises object with name and type
        """
        self.name=Path(name)

    def get_foldertype(self):
        peek=lambda self: [item.as_posix() for item in self.name.iterdir()]
        for foldertype, contentid in self.foldertypes.items():
            for item in peek(self):
                if item.split('/')[-1] in str(contentid):
                    return foldertype
        else:
            return 'standard'


class Domain:
    def __init__(self):
        self.files=[]
        self.folders=[]

    def get_path(self):
        for path in Path.home().iterdir():
            if path.is_file():
                self.files.append(File(path.name))
            if path.is_dir():
                self.folders.append(Folder(path.name))

    def file_seek(self, suffix, directory='.'):
        pathlist=Path(directory).glob('**/*' + suffix)
        return pathlist