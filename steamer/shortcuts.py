import vdf
import pathlib
import os


class SteamShortcut:
    def __init__(self, name, target, directory):
        self.values = dict()
        self.values['appid'] = 0
        self.values['AppName'] = name
        self.values['Exe'] = target
        self.values['StartDir'] = directory
        self.values['icon'] = ''
        self.values['ShortcutPath'] = ''
        self.values['LaunchOptions'] = ''
        self.values['IsHidden'] = 0
        self.values['AllowDesktopConfig'] = 1
        self.values['AllowOverlay'] = 1
        self.values['openvr'] = 0
        self.values['Devkit'] = 0
        self.values['DevkitGameID'] = ''
        self.values['DevkitOverrideAppID'] = 0
        self.values['LastPlayTime'] = 0
        self.values['FlatpakAppID'] = ''
        self.values['tags'] = []

    def name(self):
        return self.values['AppName']

    def target(self):
        return self.values['exe']

    def directory(self):
        return self.values['StartDir']


class SteamShortcutsFile:
    def __init__(self, path):
        with open(find_shortcuts_vdf(), 'rb') as file:
            self.data = vdf.binary_load(file)


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def find_shortcuts_vdf():
    steam_path = pathlib.Path.home() / '.steam'
    return find_file('shortcuts.vdf', steam_path.resolve())


def load_steam_shortcuts():
    return SteamShortcutsFile(find_shortcuts_vdf())

