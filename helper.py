import os, sys
import shutil


def check_args(args, *arg):
    if len(args) > 0:
        return True
    else:
        print('No args')
        return None


def init(*args):
    if os.path.exists(os.getcwd() + '/zeon_fs'):
        print("Directory exists")
        return None

    os.mkdir('zeon_fs')


def add_file(path, *args):
    original = f'{path}'  # r'/Users/timur/Desktop/ZEON/test.py'
    target = '.'  # r'/Users/timur/Desktop/ZEON/Tasks/Task_1/test.py'
    shutil.copy(original, target)


def list_files(*args):
    os.system('ls')


def del_file(file):
    os.remove(f'./{file}')


def get_file(name, get_path):
    with open(get_path, 'r') as f_1:
        with open(name, 'w') as f_2:
            for line in f_1.readlines():
                f_2.writelines(line)


commands = {
    'init': init,
    'add': add_file,
    'list': list_files,
    'del': del_file,
    'get': get_file,
}
