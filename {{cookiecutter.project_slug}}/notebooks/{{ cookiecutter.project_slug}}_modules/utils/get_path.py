import os

def make_path(*args):
    current_dir=os.getcwd()
    new_dir= os.path.join(current_dir,os.pardir,*args)
    return new_dir

def make_item_list(*args):
    data_dir = make_path(*args)
    items = [os.path.join(data_dir, item) for item in os.listdir(data_dir)]
    items_list = list(filter(lambda x: os.path.isfile(x), items))
    return items_list


def make_directories_list(*args):
    data_dir = make_path(*args)
    dir = [os.path.join(data_dir, item) for item in os.listdir(data_dir)]
    dir_list = list(filter(lambda x: os.path.isdir(x), dir))
    return dir_list