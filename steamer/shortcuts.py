import vdf
import os
import binascii
import shutil


STEAM_PATH = os.path.join(os.path.expanduser("~"), '.steam', 'steam')
CONFIG_FILE = os.path.join(STEAM_PATH, 'config', 'config.vdf')
CONFIG_BACKUP = CONFIG_FILE + '.bak'


class SteamShortcut:
    def __init__(self, name, target, directory):
        self.values = dict()
        self.values['appid'] = binascii.crc32(str.encode(target + name)) | 0x80000000
        if self.values['appid'] >= 2**31:
            self.values['appid'] -= 2**32
        self.values['AppName'] = name
        self.values['Exe'] = '"' + target + '"'
        self.values['StartDir'] = '"' + directory + '"'
        icon_path = os.path.join(os.path.dirname(target), 'icon.png')
        if os.path.exists(icon_path):
            self.values['icon'] = icon_path
        else:
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
        self.values['tags'] = dict()

    def name(self):
        return self.values['AppName']

    def target(self):
        return self.values['exe']

    def directory(self):
        return self.values['StartDir']

    def get_dict(self):
        return self.values

    def set_icon_path(self, path):
        self.values['icon'] = path

    def appid(self):
        if self.values['appid'] < 0:
            return self.values['appid'] + 2**32
        return self.values['appid']


class SteamShortcutsFile:
    def __init__(self, path):
        with open(find_shortcuts_vdf(), 'rb') as file:
            self.path = path
            self.data = vdf.binary_load(file)

    def add_shortcut(self, shortcut):
        index = len(self.data['shortcuts'])
        for old_index in self.data['shortcuts']:
            if self.data['shortcuts'][old_index]['appid'] == shortcut.get_dict()['appid']:
                index = old_index
        self.data['shortcuts'][str(index)] = shortcut.get_dict()

    def write_out(self):
        with open(self.path, 'wb') as file:
            vdf.binary_dump(self.data, file)

    def get_id_from_name(self, name):
        for shortcut_index in self.data['shortcuts']:
            shortcut = self.data['shortcuts'][shortcut_index]
            if shortcut['AppName'] == name:
                return shortcut['appid'] + 2**32
        return None

    def __str__(self):
        return vdf.dumps(self.data, pretty=True)


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def find_shortcuts_vdf():
    return find_file('shortcuts.vdf', STEAM_PATH)


def load_steam_shortcuts():
    return SteamShortcutsFile(find_shortcuts_vdf())


def add_proton_to_shortcut(shortcutid):
    shutil.copyfile(CONFIG_FILE, CONFIG_BACKUP)
    with open(CONFIG_FILE) as file:
        data = vdf.load(file)

    if data is not None:
        steam_config = data['InstallConfigStore']['Software']['Valve']['Steam']
        if 'CompatToolMapping' not in steam_config:
            steam_config['CompatToolMapping'] = {}

        if shortcutid not in steam_config['CompatToolMapping']:
            steam_config['CompatToolMapping'][shortcutid] = {
                'name': 'proton_experimental',
                'config': '',
                'priority': '250',
            }

            with open(CONFIG_FILE, 'w') as file:
                vdf.dump(data, file, pretty=True)
