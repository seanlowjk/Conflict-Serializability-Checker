class Action:
    READ_OPERATION = "R"
    WRITE_OPERATION = "W"

    def __init__(self, transaction_info):
        self.info = transaction_info
        self.operation = transaction_info[0]
        assert (
            self.operation == Action.READ_OPERATION
            or self.operation == Action.WRITE_OPERATION
        ), "For {}: Operation must be {} or {}".format(
            transaction_info, Action.READ_OPERATION, Action.WRITE_OPERATION
        )

        self.transaction = transaction_info[1:-1]
        self.object = transaction_info[-1]

    def has_conflict(self, action):
        return (
            self.object == action.object
            and self.transaction != action.transaction
            and (
                self.operation == Action.WRITE_OPERATION
                or action.operation == Action.WRITE_OPERATION
            )
        )

    def __str__(self):
        return self.info
