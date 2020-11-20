

def interface():
    """
    main function - calls relavent functions for user input and script output
        input - None
        output - display
    """


def pane_size():
  size=os.get_terminal_size()
  return size.columns

def unpack(lst):
  return " ".join(map(str, lst))

def clear(seconds=3):
  sleep(seconds)
  _ = system("clear")

def display():
  width = pane_size()
  pad = width - 10
  cnvsd, prjcts = projects()
  scrpt = "_blkcnvs__[beta]_"
  scrptsgn = ".an_altvu_construct."
  descrdr = "_flow_zones_"
  dotprjcts = "_current_projects_"
  hmevu = "_altvu_home_"
  flowdirs = f"{descrdr:_>{width}}\t{unpack(zones):^{width}}\n"
  prjctsumm = f"{dotprjcts:_>{width}}\t{unpack(prjcts):^{width}}\n"
  rootcntnts = f"{hmevu:_<{width}}\t{unpack(hmd):^{width}}\n"
  rootlngth = f"{hmevu:_<{width}}\t\t{str(len(hmd)) + ' files':<{width}}\n"
  print(f"{scrpt:_^{width}}\n{scrptsgn:|^{width}}\n")
  if len(hmd) < 5:
    print(f"{rootcntnts:^{width}}\n")
    else:
      print(f"{rootlngth:<{width}}\n")
      print(f"{flowdirs:^{width}}\n" f"{prjctsumm:^{width}}\n")

def main():
 display()

if __name__ == "__main__":
  main() 

