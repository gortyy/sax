import argparse


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exercise", type=str)
    parser.add_argument("--triad", type=str)
    parser.add_argument("--time", type=int)

    return parser.parse_args()
