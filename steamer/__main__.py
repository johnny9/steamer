from . import shortcuts
from . import artwork
import sys
import argparse
import os


def add_shortcut(args):
    shortcuts_file = shortcuts.load_steam_shortcuts()
    full_path = os.path.abspath(args.target)
    new_shortcut = shortcuts.SteamShortcut(args.name,
                                           full_path,
                                           os.getcwd(),
                                           args.directory)
    shortcuts_file.add_shortcut(new_shortcut)


def download_artwork(args):
    artwork.download_assets_for_steamid(args.appid)


parser = argparse.ArgumentParser(prog='steamer',
                                     description="Create a Steam shortcut")
subparses = parser.add_subparsers()
shortcut_parser = subparses.add_parser('addshortcut')
shortcut_parser.add_argument('name', help='Name for the shortcut')
shortcut_parser.add_argument('target', help='Path to program/game to run')
shortcut_parser.set_defaults(func=add_shortcut)

download_parser = subparses.add_parser('downloadartwork')
download_parser.add_argument('appid', help='Steam appid to download artwork from')
download_parser.set_defaults(func=download_artwork)

args = parser.parse_args()


