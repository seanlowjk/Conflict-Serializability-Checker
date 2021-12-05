class Action:
    READ_ACTION = 'R'
    WRITE_ACTION = 'W'

    def __init__(self, transaction_info):
        self.info =transaction_info
        self.operation = transaction_info[0]
        assert self.operation == Action.READ_ACTION or self.operation == Action.WRITE_ACTION

        self.transaction = transaction_info[1:-1]
        self.object = transaction_info[-1]

    def has_conflict(self, action):
        return self.object == action.object \
            and self.transaction != action.transaction \
            and (self.operation == Action.WRITE_ACTION or action.operation == Action.WRITE_ACTION)

    def __str__(self):
        return self.info 
