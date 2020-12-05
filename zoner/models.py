
from pathlib import Path


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
            elif self.name.endswith('rc'):
                return 'configuration'
            else:
                return 'unknown'

#    def __str__(self):
#        return {
#            f"{self.name.resolve().as_posix()}",
#            f"{self.get_filetype()}"
#            }


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


#    def __str__(self):
#        return {
#            f"{self.name.resolve().as_posix()}",
#            f"{self.get_foldertype()}"
#            }

class Domain:
    def __init__(self):
        self.files=[]
        self.folders=[]
        for path in Path.home().iterdir():
            if path.is_file():
                self.files.append(File(path.name))
            if path.is_dir():
                self.folders.append(Folder(path.name))

    def file_seek(self, suffix, directory='.'):
        pathlist=Path(directory).glob('**/*' + suffix)
        #filepaths=lambda lst: [f.__str__() for f in lst if Path.is_file(f)]
        return {f"{suffix}_files": self.files(pathlist)}



