#!/usr/bin/env python

import os

from prompt_toolkit import print_formatted_text 
from prompt_toolkit.formatted_text import HTML, FormattedText

from prompt_toolkit.styles import Style

from prompt_toolkit.shortcuts import print_container
from prompt_toolkit.widgets import Frame, TextArea


print = print_formatted_text

"""
Example of printing colored text to the output.
"""

style = Style.from_dict(
    {
        "title": "#00aaaa bold",
        "h1": "#ff0066",
    }
)

# Print using a a list of text fragments
