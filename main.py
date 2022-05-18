import sys
from helper import *


_, command, *args = sys.argv
# print(sys.argv)

args = ''.join(args)
if command in commands.keys():
    check_args(args)
    commands[command](args)
else:
    print('command not found')


