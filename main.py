from utils.cli import parse_cli
from xacts.checker import ConflictChecker


def main():
    cli_args = parse_cli()
    actions = cli_args.infile.readline()

    checker = ConflictChecker()
    checker.parse_precedences(actions)

    print("Precedences: ")

    for from_xact, to_xact in checker.get_precedences():
        print("{} -> {}".format(from_xact, to_xact))

    print("\nIs it Conflict Serializable? ")
    print(checker.is_conflict_serializable())

    print("\nEquivalent Serial Schedules: ")
    for schedule in checker.get_serial_schedules():
        print(schedule)


if __name__ == "__main__":
    main()
