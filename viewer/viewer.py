
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
    def pane_size():
      _, width=os.get_terminal_size()
      return width
    unpack=lambda lst: " ".join(map(str,lst))
    clear=lambda sec: sleep(sec);_=system("clear")
    width = pane_size()
    pad = width - 10

    scrpt = "_blkcnvs__[beta]_"
    scrptsgn = ".an_altvu_construct."
    descrdr = "_flow_zones_"
    dotprjcts = "_current_projects_"
    hmevu = "_altvu_home_"
    hmd=os.listdir(os.environ.get('HOME'))
#    flowdirs = f"{descrdr:_>{width}}\t{unpack(zones):^{width}}\n"
#    prjctsumm = f"{dotprjcts:_>{width}}\t{unpack(prjcts):^{width}}\n"
    rootcntnts = f"{hmevu:_<{width}}\t{unpack(hmd):^{width}}\n"
    rootlngth = f"{hmevu:_<{width}}\t\t{str(len(hmd)) + ' files':<{width}}\n"
    print(f"{scrpt:_^{width}}\n{scrptsgn:|^{width}}\n")

    #if len(hmd) < 5:
     #   print(f"{rootcntnts:^{width}}\n")
#    else:
#        print(f"{rootlngth:<{width}}\n")
#        print(f"{flowdirs:^{width}}\n" f"{prjctsumm:^{width}}\n")


def main():
    display()

if __name__ == "__main__":
    main()
