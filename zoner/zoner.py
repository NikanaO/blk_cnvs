#zoner/models.py

from pathlib import Path
from models import Domain


homed=Path.home()

def charter(root_directory=homed):
    isort={
        'files': lambda lst: {pth[0]: pth[2] for pth in lst if pth[1] == 'file'},
        'dirs': lambda lst: [pth for pth in lst if pth[1] == 'directory'],
        'rcfiles': lambda lst: [pth for pth in lst if pth[0].endswith('rc')],
        'unknown': lambda lst: [pth[0] for pth in lst if pth[2] is None],
        'flowzone': lambda lst: {pth[0]: pth[2][0:2] for pth in isort['dirs'](lst) if 'True' in pth[2][-1]},
        'hidden': lambda lst: [pth[0] for pth in lst if pth[0].startswith('.')],
        }

    homedom=[Domain(pth.name) for pth in homed.iterdir()]
    homeinfo=[(pth.name, pth.path_type, pth.address_info(pth.address)) for pth in homedom]

def main():

    homed=Domain('altvu')


if __name__ == "__main__":
    main()
