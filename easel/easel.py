# coding: utf-8
# %load /home/altvu/canvas/projects/blk_cnvs/easel/easel.py
#!/usr/bin/env python3
from PIL import Image, ImageFilter

os=Image.os
path=os.path
homed=os.environ.get('HOME')
dotd=os.environ.get('PWD')

def fluxzone():
    '''
    utility function - initialise user namespace with relevant workflow domain
        input - None
        output - dictionary
    '''
    userds=[
        'canvas',
        'nexus',
        'studio',
        'portal',
        '.blk_cnvs',
        '.task',
        '.marks',
        '.elinks',
        '.newsboat',
        '.convex'
        ]
    os.chdir(homed)
    dpths={}
    for d in userds:
        dpths[d]=(path.abspath(d), os.listdir(d))
    os.chdir(dotd)
    return dpths

def pathlist(directory):
    '''
    utility function - gather all files from specified directory into list
        input - string
        output - list
    '''
    filepaths=[]
    for dnm, dpth, fls in os.walk(directory, topdown=True):
        if len(os.listdir(dnm)) > 0:
            for f in fls:
                filepaths.append(path.join(dnm, f))
    return filepaths

def pathstamp(filepaths):
    '''
        utility function - sort all files into categories from filelist
        input - list
        output - dictionary input for path_atlas
    '''
    ftypes={
    'image': ('.jpg','.png','.svg', '.ppm','.jpeg'),
    'doc': ('.pdf','.doc','.html'),
    'code': ('.py','.pyc','.sh','.ipynb','.js'),
    'data': ('.json', '.xml'),
    'media': ('.mp3','.mp4'),
    }
    fldict={}
    for ft in ftypes.keys():
        fldict['image']=[f for f in filepaths if f.endswith(ftypes['image'])]
        fldict['doc']=[f for f in filepaths if f.endswith(ftypes['doc'])]
        fldict['code']=[f for f in filepaths if f.endswith(ftypes['code'])]
        fldict['data']=[f for f in filepaths if f.endswith(ftypes['data'])]
        fldict['media']=[f for f in filepaths if f.endswith(ftypes['media'])]
    return fldict

def path_atlas():
    '''
    main function - returns categorised filepaths for conditional script processing
        input - None
        output - two dictionary types:
            first one extracts directory meta content
            second one
    '''
    dpaths=fluxzone()
    os.chdir(homed)
    shownpaths=[path.abspath(d) for d in dpaths.keys() if
    d.isalpha()]
    flow_meta={}
    flow_content={}
    for d, sd in dpaths.values():
        if d in shownpaths and '.meta' in sd:
            metad=path.join(d, '.meta')
            flow_meta[path.basename(d)]=(metad, os.listdir(metad))
            flow_content[path.basename(d)]=pathstamp(pathlist(d))
    os.chdir(dotd)
    return flow_meta, flow_content

def interface():
    '''
    main function - calls relavent functions for user input and script output
        input - None
        output - display
    '''
    meta, content=path_atlas()
    intro=(
        f"|||_easel__[beta]_|||\n"
        f"||graphics_design_module||\n"
        f"|||.an altvu construct.|||\n"
        )
    br=(
        f"__________________________\n"
        )
    print(intro.center(30))
    print(br)
    print(f"|flow_zones|\n")
    flowdom=content.fromkeys(content.keys())
    for d in content.keys():
        print(f"|_{d}_|\t")
        for c in content[d].keys():
            flowdom[d]=content[d]
            if c == 'image'or c == 'media':
                print(f"{c} files: {len(content[d][c])}\t")

def main():
    '''
    main function - calls other main functions based on user defined conditional flow
    input - None
    output - function output
    '''
    interface()

if (__name__ == "__main__"):
	main()
