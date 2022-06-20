import vdf
import pathlib
import os


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def find_shortcuts_vdf():
    steam_path = pathlib.Path.home() / '.steam'
    return find_file('shortcuts.vdf', steam_path.resolve())


def load_steam_shortcuts():
    with open(find_shortcuts_vdf(), 'rb') as file:
        return vdf.binary_load(file)

