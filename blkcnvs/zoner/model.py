# coding: utf-8

import os
path=os.path

def pathclass(*args):
    folders=[d for d in args if path.isdir(d)]
    files=[f for f in args if path.isfile(f)]
    return {'folders': [*folders], 'files': [*files] }

def dctdetails(dct):
    '''
    utility - probes dictionary object and returns its composition
        input - object name (dictionary)
        output - keys paired with value type (tuple)
    '''
    def detaildct(dct):
        return ([type(dct[key]) for key in [*dct]])
    def layerkeys(dct):
        return ([key for key in [*dct]])
    def layervallength(dct):
        return ([len(dct[key]) for key in [*dct]])
    layerdetail=tuple(zip(layerkeys(dct), detaildct(dct), layervallength(dct)))
    return layerdetail


def pathlist(directory='.'):
    '''
    utility - gather files from directory into list
        input - directory name (string)
        output - all directory filepaths (list)
    '''
    filepaths=[]
    for dname, dpath, files in os.walk(directory, topdown=True):
        if len(os.listdir(dname)) > 0:
            for file in files:
                filepaths.append(path.join(dname, file))
    return filepaths


def pathstamp(filepaths):
    '''
    utility - sort files into categories
        input - filepaths (list)
        output - filetype to filelist dictionary for controller functions
    '''
    def no_ext(file):
        '''
        TODO At some point make provisions to handle
        hidden files, which are prepended with a period
        '''
        if '.' not in path.basename(file):
            return True
        else:
            return False
    genre={
        'image': ('.jpg','.png','.svg', '.ppm','.jpeg'),
        'doc': ('.pdf','.doc','.html', '.txt', '.save'),
        'code': ('.py','.pyc','.sh','.ipynb','.js'),
        'data': ('.json', '.xml'),
        'media': ('.mp3','.mp4'),
    }
    pathpin={}
    for kind in genre.keys():
        pathpin['image']=[f for f in filepaths if f.endswith(genre['image'])]
        pathpin['doc']=[f for f in filepaths if f.endswith(genre['doc'])]
        pathpin['code']=[f for f in filepaths if f.endswith(genre['code'])]
        pathpin['data']=[f for f in filepaths if f.endswith(genre['data'])]
        pathpin['media']=[f for f in filepaths if f.endswith(genre['media'])]
        pathpin['unknown']=[f for f in filepaths if no_ext(f)]
    return pathpin
