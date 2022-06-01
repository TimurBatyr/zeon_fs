import hashlib

from helper import *
from pathlib import Path

target_path = 'zeon_fs_test'
source_path = 'test_values'
test_files = ['file1.txt', 'file2.txt', 'file3.txt']
files_hashes = {
    'file1.txt': 'd8578edf8458ce06fbc5bb76a58c5ca4',
    'file2.txt': 'b06f92d72df589cc2776982afc89d365',
    'file3.txt': '76ef6111ef38849310e022abc992bff3',
}


def test_init_fs():
    assert init_fs(target_path) is None
    assert Path(target_path).is_dir()


def test_init_db():
    assert init_db() is None
    assert Path(target_path + '/db.txt').exists()


def test_add_file():
    for file in test_files:
        assert add_file(f'{source_path}/{file}', target_path)
        assert Path(f'{target_path}/{file}').is_file()


# def test_hash_files():
#     for file in test_files:
#         assert hash_file(file) == ''
#     assert hash_file(f'{source_path}/file1.txt') == files_hashes['file1.txt']
#
#
# def test_add_to_db():
#     for file, file_hash in files_hashes.items():
#         add_to_db(file, file_hash)
#         assert get_by_key_from_index(DB_BY_NAME, file) == file_hash
#         assert get_by_key_from_index(DB_BY_HASH, file_hash) == file
#
#
# def test_delete_file():
#     for file in test_files:
#         assert delete_file(f'{target_path}/{file}')
#         assert not Path(f"{target_path}/{file}").is_file()
#
#
# def test_list_files():
#     dir_path = f'./{target_path}'
#     expected = os.listdir(dir_path)
#     for i in range(len(expected)):
#         assert list_files()[i] == expected[i]


# def test_get_file():
#     for num, file in enumerate(test_files):
#         assert get_file(f"{source_path}/{file}", f"{num}.{file}", target_path)
#         assert Path(f"{target_path}/{num}.{file}").is_file()