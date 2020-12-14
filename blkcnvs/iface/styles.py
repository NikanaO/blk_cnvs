import os

from time import sleep
from prompt_toolkit import print_formatted_text 
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style

path=os.path
system=os.system

class Display():
    '''Create a custom smart display for workflow '''
      #instance attr

    def __init__(self, header="blkcnvs__[beta]"):
        '''Initialise display with attributes'''
        self.header=header
        self.body=''
    #instance methods
    def get_body(self, body):
        self.body=body

    def set_style(self):
        headertxt=FormattedText([
            ('class:header', self.header),])
        headerstyle=Style.from_dict({
            'header': 'cyan bold'}) 
        

    def display(self):
        width, _=os.get_terminal_size() 
        unpack=lambda lst: " ".join(map(str,lst))
        #split=lambda strng: strng.split()
        alltxt=f"{self.header:_<{width}}\n{unpack(self.body):^{width}}\n"
        print(f"{alltxt}")


