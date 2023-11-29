import os
import pathlib
import pyhere
import pyprojroot

# Retorna un objeto de tipo directorio
#def make_dir_function(dir_name):
#    def dir_function(*args):
#        return pyprojroot.here().joinpath(dir_name, *args)
#    return dir_function

# Retorno un objeto de tipo directorio / de la carpeta padre, hasta el proyecto
def get_parent_path():
    CURRENT_DIR = pathlib.Path().resolve()
    DATA_DIR=CURRENT_DIR.parent
    return DATA_DIR

# Retorna la lista de los path a los diferentes elementos de la carpeta ROOT
def make_dir_list():
    CURRENT_DIR = pathlib.Path().resolve()
    DATA_DIR=CURRENT_DIR.parent
    return list(DATA_DIR.glob("*"))