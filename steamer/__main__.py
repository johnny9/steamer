import sys
import argparse


def parse_args(arguments):
    parser = argparse.ArgumentParser(prog='steamer',
                                     description="Create a Steam shortcut")
    parser.add_argument('name', help='Name for the shortcut')
    parser.add_argument('target', help='Path to program/game to run')
    parser.parse_args(arguments)


parse_args(sys.argv)
