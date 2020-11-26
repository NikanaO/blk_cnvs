import os

from models import Domain

path=os.path

def main():
    prv=lambda lst: [i for i in lst if i.startswith('.')]
    pub=lambda lst: [i for i in lst if not i.startswith('.')]

    home=Domain(os.environ.get('HOME'))
    home.pathclass(*home.content)


if __name__ == "__main__":
  main()


