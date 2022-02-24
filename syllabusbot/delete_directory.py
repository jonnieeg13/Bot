import shutil


def delete_directory(path):
    try:
        shutil.rmtree(path)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


file_to_delete = r''
delete_directory(file_to_delete)
