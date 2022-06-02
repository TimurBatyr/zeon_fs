from hashlib import md5
from pathlib import Path
import os
import pickle
import shutil


BASE_DIR_PATH = 'zeon_fs_test'
DATABASE_PATH = f'{BASE_DIR_PATH}/db.txt'
DB_BY_NAME = 'BY_NAME'
DB_BY_HASH = 'BY_HASH'
DB_START_DATA = {DB_BY_NAME: {}, DB_BY_HASH: {}}


def init_fs(dir_name: str = BASE_DIR_PATH, *args, **kwargs) -> None:
    os.makedirs(dir_name, exist_ok=True)
    print('FS initialized')
    init_db()


def init_db(*args, **kwargs) -> None:
    if not Path(DATABASE_PATH).exists():
        with open(DATABASE_PATH, 'wb') as file:
            pickle.dump(DB_START_DATA, file)
            print('Database was initialized')
    print('Database already exists')


def copy_file(file_path: str, file_name: str = None, *args, **kwargs) -> bool:
    if not file_name:
        file_name = Path(file_path).name

    file_hash = hash_file(file_path)
    if check_in_db(file_name, file_hash):
        shutil.copyfile(file_path, f"{BASE_DIR_PATH}/{file_name}")
        add_to_db(file_name, file_hash)

        return True

    return False


def add_file(file_path: str, *args, **kwargs) -> bool:
    if not Path(file_path).exists():
        return False

    copy_file(file_path)
    return True


def hash_file(file_path: str, *args, **kwargs) -> str:
    if not Path(file_path).exists():
        return ''

    with open(file_path, 'rb') as file:
        return md5(file.read()).hexdigest()


def add_to_db(file_name: str, file_hash: str, *args, **kwargs) -> None:
    with open(f'{BASE_DIR_PATH}/db.txt', "rb") as db:
        data = pickle.load(db)
        data[DB_BY_NAME][file_name] = file_hash
        data[DB_BY_HASH][file_hash] = file_name

    with open(f'{BASE_DIR_PATH}/db.txt', "wb") as db:
        pickle.dump(data, db)


def get_by_key_from_index(index: str, key: str, *args, **kwargs) -> str:
    with open(DATABASE_PATH, "rb") as file:
        data = pickle.load(file)
        if index in data.keys():
            if key in data[index]:
                return data[index][key]
    return ''


def check_in_db(file_name: str, file_hash: str) -> bool:
    by_name_result = get_by_key_from_index(index=DB_BY_NAME, key=file_name)
    by_hash_result = get_by_key_from_index(index=DB_BY_HASH, key=file_hash)

    if by_name_result == '' and by_hash_result == '':
        return True

    return False


def delete_file(file_path: str, *args, **kwargs) -> bool:
    if not Path(file_path).is_file():
        return False

    delete_from_db(file_name=Path(file_path).name, file_hash=hash_file(file_path))
    os.remove(file_path)
    return True


def delete_from_db(file_name: str, file_hash: str, *args, **kwargs) -> None:
    with open(f'{BASE_DIR_PATH}/db.txt', "rb") as db:
        data = pickle.load(db)
        del data[DB_BY_NAME][file_name]
        del data[DB_BY_HASH][file_hash]

    with open(f'{BASE_DIR_PATH}/db.txt', "wb") as db:
        pickle.dump(data, db)


def list_files(*args, **kwargs) -> list:
    files_list = os.listdir(path=f'./{BASE_DIR_PATH}')
    for i in files_list:
        print(i)
    return files_list


def get_file(file_path: str, file_name: str, *args, **kwargs) -> bool:
    if not Path(file_path).is_file():
        return False

    copy_file(file_path, file_name)
    return True


commands = {
    'init': init_fs,
    'add': add_file,
    'del': delete_file,
    'list': list_files,
    'get': get_file,
}