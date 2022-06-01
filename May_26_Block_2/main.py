import sys

from helper import *


def main():
    _, command, *args = sys.argv
    if command in commands:
        commands[command](*args, command=command)
    else:
        print("Command not found!")


if __name__ == "__main__":
    main()