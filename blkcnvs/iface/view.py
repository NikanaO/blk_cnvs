
#def interface():
#    """
#    main function - calls relavent functions for user input and script output
#        input - None
#        output - display
#    """
import os

from time import sleep
from prompt_toolkit import print_formatted_text as print

path=os.path
system=os.system


def display():
    size=lambda: os.get_terminal_size()
    _,width=size
    unpack=lambda lst: " ".join(map(str,lst))
    clear=lambda sec: sleep(sec);_=system("clear")

    scrpt = "_blkcnvs__[beta]_"
    scrptsgn = ".an_altvu_construct."
    descrdr = "_flow_zones_"
    dotprjcts = "_current_projects_"
    hmevu = "_altvu_home_"
    rootcntnts = f"{hmevu:_<{width}}\t:cntnt^{width}\n"
    print(f"{scrpt:_^{width}}\n{scrptsgn:|^{width}}\n")

def main():
    display()

if __name__ == "__main__":
    main()
