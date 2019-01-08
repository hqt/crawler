import os


def create_directory(directory_path):
    try:
        os.mkdir(directory_path)
    except OSError as e:
        print("Creation of the directory %s failed" % directory_path)
        print(e)


def is_file_existed(file_path):
    try:
        f = open(file_path, 'r')
        f.close()
        return True
    except Exception as e:
        return False
