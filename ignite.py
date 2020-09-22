# coding: utf-8
# %load canvas/constructs/base/ignite.py
#!/usr/bin/python3

#Global modules and aliases

import subprocess
os=subprocess.os
path=os.path

#Global variables

homed=os.environ.get('HOME')
dotd=os.environ.get('PWD')


class Project():

	#class variables

	dnames=['.', 'canvas', 'nexus', 'studio', 'portal']

	#class functions
	
	def __init__(self, label, genre):
		self.label = label
		self.genre = genre

	@classmethod
	def get_project_paths(cls, dnames):
		cls.paths=project_paths

	def domain(self):
		if os.getcwd() != homed:
			os.chdir(homed)
			for d in self.dnames:
				self.dpaths[d]=path.abspath(d)
		#lvlone=[path.join(dpths[dpath], sd) for sd in os.listdir(dpths[dpath])]
		#lvlfiles=[f for f in lvlone if path.isfile(f)]
		#lvlfolders=[d for d in lvlone if path.isdir(d)]
		#return lvlfolders, lvlfiles
		return self.dpaths

	def summary(self):
		brief=(
        f"Project {self.label}\n"
        f"type: \t {self.genre}\n"
        #f"folders: \t {domain()}\n"
        #f"main directory: {se	lf.domain}\n"
        )
		return brief


def main():

	prjct_one=Project('magic_beans', 'graphic design')
	print(prjct_one.summary())
	print(prjct_one.domain())

if ( __name__ == "__main__"):
	main()
