import argparse
import pathlib
import toml


def parse_config():
    parse = argparse.ArgumentParser()
    parse.add_argument('-c', '--config', help='Please provide config file path')
    args = parse.parse_args()

    if args.config:
        root = pathlib.Path(__file__).parent.parent.parent
        path = pathlib.Path.joinpath(root, args.config)
        return toml.load(path)
    else:
        parse.print_help()
