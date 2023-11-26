import os
import pathlib

def make_path(*args):
    #current_dir=os.getcwd()
    #new_dir= os.path.join(current_dir,os.pardir,*args)
    CURRENT_DIR = pathlib.Path().resolve()
    DATA_DIR=CURRENT_DIR.parent.joinpath(args)
    return DATA_DIR

def make_path_list(*args):
    #data_dir = make_path(*args)
    #items = [os.path.join(data_dir, item) for item in os.listdir(data_dir)]
    #items_list = list(filter(lambda x: os.path.isfile(x), items))
    CURRENT_DIR = pathlib.Path().resolve()
    DATA_DIR=CURRENT_DIR.parent.joinpath(args)
    # Glob aplica la li
    return list(DATA_DIR.glob("*"))


def make_directories_list(*args):
    data_dir = make_path(*args)
    dir = [os.path.join(data_dir, item) for item in os.listdir(data_dir)]
    dir_list = list(filter(lambda x: os.path.isdir(x), dir))
    return dir_list