# coding: utf-8
import time

from blkcnvs import model, method

pthsrch=method.pathsearch
psx=method.posix
pk=method.peek
nxjsn=method.nexjsons
dcd=method.json_decode
ecd=method.json_encode
dctdeets=method.dctdetails


def main():
    bklnks=nxjsn('buk')
    clipsnips=nxjsn('clipr')
    taskdeets=nxjsn('taskr')


def filerename(dirpath, replace=True):
    import os
    if replace:
        for count, fname in enumerate(pk(dirpath)):
            dst=method.rplace(psx(fname))
            src=os.path.join(dirpath, fname)
            dst=os.path.join(dirpath, dst)
            print(
                f"dst: {dst}\n"
                f"src: {src}\n"
                f"{count} files renamed"
            )
