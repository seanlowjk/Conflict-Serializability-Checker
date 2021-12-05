from xacts.action import Action
from xacts.algos import permutations
from xacts.precedence import PrecedenceGraph


class ConflictChecker:
    def __init__(self):
        self.actions = []
        self.xact_nos = set()
        self.graph = PrecedenceGraph()

    def register_xact(self, xact_no):
        self.xact_nos.add(xact_no)

    def parse_precedences(self, precedences):
        self.actions = [Action(action.strip()) for action in precedences.split(",")]

        for i in range(len(self.actions)):
            for j in range(i + 1, len(self.actions)):
                prev_action = self.actions[i]
                next_action = self.actions[j]

                self.register_xact(prev_action.transaction)
                self.register_xact(next_action.transaction)

                if prev_action.has_conflict(next_action):
                    self.graph.add_edge(prev_action, next_action)

                if self.graph.has_conflicting_precedence(prev_action, next_action):
                    self.graph.is_acyclic = False

    def get_precedences(self):
        return self.graph.get_precedences()

    def is_conflict_serializable(self):
        return self.graph.is_acyclic

    def follows_precedence_order(self, schedule, precedence):
        return schedule.index(precedence[0]) < schedule.index(precedence[1])

    def get_serial_schedules(self):
        possible_serial_schedules = permutations(list(self.xact_nos))
        precedences = self.get_precedences()

        serial_schedules = []
        for schedule in possible_serial_schedules:
            is_possible_schedule = True
            for precedence in precedences:
                if not self.follows_precedence_order(schedule, precedence):
                    is_possible_schedule = False
                    break

            if is_possible_schedule:
                serial_schedules.append(schedule)

        return serial_schedules
