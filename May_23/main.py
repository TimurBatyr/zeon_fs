from helper import *


def main():
    _, command, *args = sys.argv
    # print(sys.argv)

    # args = ''.join(args)
    if command in commands.keys():
        check_args(args)
        commands[command](*args)
    else:
        print('command not found')


if __name__ == '__main__':
    main()
