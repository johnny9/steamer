import sys
import argparse


parser = argparse.ArgumentParser(prog='steamer',
                                     description="Create a Steam shortcut")
subparses = parser.add_subparsers()
shortcut_parser = subparses.add_parser('addshortcut')
shortcut_parser.add_argument('name', help='Name for the shortcut')
shortcut_parser.add_argument('target', help='Path to program/game to run')

shortcut_parser = subparses.add_parser('downloadartwork')
shortcut_parser.add_argument('appid', help='Steam appid to download artwork from')

parser.parse_args()
