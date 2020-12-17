#!/usr/bin/env python

import styles

Format=styles.FormattedText
print=styles.print_formatted_text
custom=styles.style

"""
Example usage of 'print_container', a tool to print
any layout in a non-interactive way.
"""


textparts = Format(
    [
        ("class:title", "blkcnvs__[beta]__ "),
        ("class:h1.face", "face"),
        ("class:h1.ozone", "ozone"),
        (" ", "\n"),
    ]
)
print(textparts, style=custom)


def print_box(text, title="blkcnvs__[beta]__"):
    print_container(
        Frame(
            TextArea(text="Hello world!\n"),
            title="Stage: parse",
        )
    )

    
