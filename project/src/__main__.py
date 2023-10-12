import argparse

from project.src import core


def cli(argv=None) -> None:

    parser = argparse.ArgumentParser(
        prog='project',
        description='Add two floating point numbers',
    )

    parser.add_argument('num1', type=float)
    parser.add_argument('num2', type=float)

    args = parser.parse_args(argv)
    print(core.add(args.num1, args.num2))


if __name__ == '__main__':
    cli()
