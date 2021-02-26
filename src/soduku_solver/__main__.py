import argparse
from .solver import solve


def main():

    parser = argparse.ArgumentParser(description='Example Soduku Solver')

    parser.add_argument(
        '--solve-soduku',
        action='store_true',
        help='efficiently test a soduku solution')
    args = parser.parse_args()

    if args.solve_soduku:
        solve()
    else:
        parser.print_help()
        exit(-1)


if __name__ == "__main__":
    main()