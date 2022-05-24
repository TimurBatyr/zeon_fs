import os

from helper import init


def test_init():
    try:
        arguments = os.path.exists(os.getcwd() + '/zeon_fs_v1')
        expected = None
    except:
        raise Exception('File doesnt exist')
    actual = init(arguments)
    assert expected == actual
