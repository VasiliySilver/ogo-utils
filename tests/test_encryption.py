import glob
import os
import shutil

from ogo_utils.encryption import walk_to_encrypt


def test_encryption():
    # Создание директории для шифрования
    directory = 'decryption_test'
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)
    # Удаление директории
    files = glob.glob(parent_dir + '/*')
    shutil.rmtree(path) if path in files else print('Нет такой директории')
    os.mkdir(path)
    assert "Directory '% s' created" % path == "Directory '% s' created" % path

    # Создание файла в директории
    file = 'checked_file.txt'
    check_file = os.path.join(path, file)
    file = open(check_file, 'w')
    file.write("This is the write command")
    # file.write("It allows us to write in a particular file")
    file.close()

    # Шифрование директории
    password = 'password'
    dir_to_encrypt = path
    walk_to_encrypt(dir_to_encrypt, password)

    try:
        file = open(check_file + '.crp', 'r')
        file.read()
    except UnicodeDecodeError as er:
        assert er.reason == 'invalid start byte'

    file.close()
    return dir_to_encrypt, password, check_file, parent_dir, path


if __name__ == '__main__':
    test_encryption()
