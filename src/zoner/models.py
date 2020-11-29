import os

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path


class Model(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def get(self, path):
        """Returns an object with a .path_details() call method
        that iterates over key,value pairs of its information."""
        pass

    @property
    @abstractmethod
    def path_type(self):
        pass


class DomainModel(Model):

    @dataclass
    class Address:
        """Class for organising units or bit in a domain."""
        name: str
        path_type: str=None
        address_info: tuple=None
        
        def __post_init__(self):
            """
            initialises object with path type, file or folder
            """
            path_types=['directory', 'file']
            if Path(self.name).exists():
                self.address = Path(self.name).resolve()
                if self.address.is_dir():
                    self.path_type=path_types[0]
                elif self.address.is_file():
                    self.path_type=path_types[1]
            return self.path_type

                
        def address_info(self):
            """
            if object is file type, returns class of file
            """
            is_file=lambda self: bool(self.is_file())
            is_dir=lambda self: bool(self.is_dir())
            hidden=lambda self: bool(self.name.startswith('.'))
            has_extension=lambda self: bool(self.suffix)
            is_config=lambda self: bool(self.name.endswith('rc'))

            def file_types(self=None):
                typedct={
                    'image': ('.jpg','.png','.svg', '.ppm','.jpeg'),
                    'document': ('.pdf','.doc','.html', '.txt', '.save'),
                    'code': ('.py','.pyc','.sh','.ipynb','.js'),
                    'data': ('.json', '.xml'),
                    'media': ('.mp3','.mp4'),
                }
                return typedct
                
            if is_file(self) and has_extension(self):
                unpack=lambda lst: " ".join(map(str, lst))
                file_type=file_types(self)
                genre=[ftype for ftype, extension in file_type.items() if self.suffix in extension]
                return(f"file type: {unpack(genre)}")
                
            elif is_file(self) and is_config(self):
                return(f"file type: configuration")
                
            elif is_file(self):
                return(f"file type: unknown")
                
            elif is_dir(self):
                peek=lambda self: [*self.iterdir()]
                has_meta=lambda self: bool(self.joinpath('.meta') in peek(self))
                is_repo=lambda self: bool(self.joinpath('.git') in peek(self))
                subdirectories=[pth for pth in peek(self) if is_dir(self)]
                files=[pth for pth in peek(self) if is_file(self)]
                return(f"subdirectories: {len(subdirectories)}", f"files: {len(files)}", f"flowzone: {has_meta(self)}")
