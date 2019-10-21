import argparse
import pathlib
import toml


def parse_config():
    root = pathlib.Path(__file__).parent.parent.parent
    path = pathlib.Path.joinpath(root, 'dev.toml')
    return toml.load(path)
