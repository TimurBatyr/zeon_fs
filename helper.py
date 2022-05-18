import os, sys
import shutil


def check_args(args):
    if len(args) > 0:
        return True
    else:
        print('No args')
        return None


def init(_):
    if os.path.exists(os.getcwd() + '/zeon_fs'):
        print("Directory exists")
        return None

    os.mkdir('zeon_fs')


def add_file(path):
    original = f'{path}' #/Users/timur/Desktop/ZEON/test.py
    target = '.'
    shutil.copy(original, target)


def list_files(_):
    os.system('ls')


def del_file(file):
    os.remove(f'./{file}')


def get_file():
    pass


commands = {
    'init': init,
	'add': add_file,
    'list': list_files,
	'del': del_file,
    'get': get_file
}



