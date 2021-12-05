from argparse import FileType, ArgumentParser
from datetime import datetime
from json import load


def parse_cli():
    cli_parser = ArgumentParser(description="Follow the following arguments to provide your sequence of transactions")

    cli_parser.add_argument(
        "-i",
        dest="infile",
        type=FileType("r"),
        nargs="?",
        required=True,
        help="file which contains transaction actions",
    )

    args = cli_parser.parse_args()

    return args
