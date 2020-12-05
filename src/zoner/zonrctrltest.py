import os

from models import Domain, Matter

path=os.path


prv=lambda lst: [i for i in lst if i.startswith('.')]
pub=lambda lst: [i for i in lst if not i.startswith('.')]

home=Domain(os.environ.get('HOME'))
home.pathclass(*home.content)

