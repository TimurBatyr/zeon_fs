import os
import filecmp
from pathlib import Path

from helper import init, add_file, list_files, del_file, get_file


def test_init():
    actual = ['zeon_fs_v2']
    expected = os.getcwd() + '/zeon_fs_v2'
    assert init(actual) == expected


def test_add_file():
    assert add_file('test/test.txt', '.') is None
    assert Path('test.txt').is_file()


def test_list_files():
    dir_path = '.'
    expected = os.listdir(dir_path)
    for i in range(len(expected)):
        assert list_files()[i] == expected[i]

    # assert type(list_files()) == list


def test_del_file():
    assert del_file('test.txt') is True
    assert not Path('test').is_file()


def test_get_file():
    name = 'test.txt'
    get_path = os.getcwd() + '/ModelDecomposition.txt'
    assert get_file(name, get_path) == True
    file1 = name
    file2 = 'ModelDecomposition.txt'
    comp = filecmp.cmp(file1, file2, shallow=True)
    assert comp is True
    os.remove(name)

