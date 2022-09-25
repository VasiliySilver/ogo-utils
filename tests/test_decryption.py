import glob
from ogo_utils.decryption import walk_to_decrypt
import os
import shutil

from ogo_utils.encryption import walk_to_encrypt
from tests.test_encryption import test_encryption


def test_decryption():
    dir_to_encrypt, password, check_file, parent_dir, path = test_encryption()

    walk_to_decrypt(dir_to_encrypt, password)

    with open(check_file, 'r') as f:
        s = f.readline()
        assert s == 'This is the write command'

    # Удаление директории
    files = glob.glob(parent_dir + '/*')
    shutil.rmtree(path) if path in files else print('Нет такого файла')


if __name__ == '__main__':
    test_decryption()
