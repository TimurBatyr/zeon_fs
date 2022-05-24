
import os

command = input('Print a particular command: ')
if command == 'mkdir':
    os.mkdir(input('Type the title of the dir:'))
if command == 'touch':
    file_name = input('title:')
    os.system(f"touch {file_name}")
if command == 'rm':
    file_name = input('title:')
    os.system(f"rm {file_name}")
if command == 'ls':
    os.system('ls')
if command == 'find':
    file_name = input('title:')
    os.system(f"find {file_name}")