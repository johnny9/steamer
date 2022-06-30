from . import shortcuts
from . import artwork
import argparse
import os


def add_shortcut(args):
    shortcuts_file = shortcuts.load_steam_shortcuts()
    full_path = os.path.abspath(args.target)
    new_shortcut = shortcuts.SteamShortcut(args.name,
                                           full_path,
                                           os.getcwd())
    shortcuts_file.add_shortcut(new_shortcut)
    shortcuts_file.write_out()

    if args.steamid is not None:
        artwork.download_assets_for_steamid(args.steamid)

    if args.grid:
        artwork.link_artwork_to_users(new_shortcut.appid())


def download_artwork(args):
    artwork.download_assets_for_steamid(args.appid)


def link_artwork(args):
    shortcut_file = shortcuts.load_steam_shortcuts()
    shortcutid = shortcut_file.get_id_from_name(args.name)
    artwork.link_artwork_to_users(shortcutid)


parser = argparse.ArgumentParser(prog='steamer',
                                 description="Create a Steam shortcut")
subparses = parser.add_subparsers()
shortcut_parser = subparses.add_parser('addshortcut')
shortcut_parser.add_argument('name', help='Name for the shortcut')
shortcut_parser.add_argument('target', help='Path to program/game to run')
shortcut_parser.add_argument('--grid', help='Add grid artwork', required=False,
                             action='store_true', default=False)
shortcut_parser.add_argument('--steamid', help='Appid to download from', required=False,
                             default=None)
shortcut_parser.set_defaults(func=add_shortcut)

download_parser = subparses.add_parser('downloadartwork')
download_parser.add_argument('appid', help='Steam appid to download artwork from')
download_parser.set_defaults(func=download_artwork)

link_art_parser = subparses.add_parser('linkartwork')
link_art_parser.add_argument('name', help='Name of the shortcut to link to')
link_art_parser.set_defaults(func=link_artwork)

args = parser.parse_args()
args.func(args)


