class PrecedenceGraph:
    def __init__(self):
        self.graph = {}
        self.is_acyclic = True 

    def add_edge(self, from_xact, to_xact):
        from_xact_no = from_xact.transaction
        to_xact_no = to_xact.transaction

        if from_xact_no not in self.graph:
            self.graph[from_xact_no] = []

        if to_xact_no not in self.graph[from_xact_no]:
            self.graph[from_xact_no].append(to_xact_no)
    
    def has_conflicting_precedence(self, from_xact, to_xact):
        from_xact_no = from_xact.transaction
        to_xact_no = to_xact.transaction
        return to_xact_no in self.graph and from_xact_no in self.graph[to_xact_no]

    def get_precedences(self):
        precedences = []

        for from_xact_no, to_xact_nos in self.graph.items():
            for to_xact_no in to_xact_nos:
                precedences.append((from_xact_no, to_xact_no))

        return precedences
