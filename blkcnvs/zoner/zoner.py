
from zoner import model as znm

def controller():
    """
    controller - uses model functions to establish session domain and chart associated assets/filepaths
        input - None
        output - two dictionary types:
         (1) extracts directory meta content
         (2) extracts directory asset content
    """
        
    homed=znm.os.environ.get('HOME')
    
    dpath=lambda dnm: znm.path.abspath(dnm)
    dlst=lambda dn: znm.os.listdir(dn)
    unpack=lambda lst: " ".join(map(str,lst))
    ddct=lambda dirname: {dpath(dirname): dlst(dpath(dirname))}

    

def main():
  controller()

if __name__ == "__main__":
  main()
