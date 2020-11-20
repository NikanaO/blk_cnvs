#!/usr/bin/env python3

import subprocess

os = subprocess.os
path = os.path


def vectorize(ipath):
    p1 = subprocess.run(
        [
            "potrace",
            "-s",
            "-r 300",
            "-a 1",
            "-S 1" "--group" "--progress",
            ipath,
            "-o",
            opath,
        ]
    )
    return opath
