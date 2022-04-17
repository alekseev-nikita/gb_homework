import os
from shutil import copyfile


def make_template():
    for root, dirs, files in os.walk('my_project'):
        if 'template' in root:
            for f in files:
                file_path = os.path.join(root, f)
                new_file_path = os.path.join('my_project', 'templates', root.split(os.sep)[-1])
                try:
                    os.makedirs(new_file_path)
                except FileExistsError:
                    pass
                copyfile(file_path, os.path.join(new_file_path, f))


make_template()
