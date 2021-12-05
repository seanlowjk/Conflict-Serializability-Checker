class PrecedenceGraph:
    def __init__(self):
        self.graph = {}
        self.is_acyclic = True 

    def add_edge(self, from_xact, to_xact):
        from_xact_no = from_xact.transaction
        to_xact_no = to_xact.transaction

        if from_xact_no not in self.graph:
            self.graph[from_xact_no] = {}

        if to_xact_no not in self.graph[from_xact_no]:
            self.graph[from_xact_no][to_xact_no] = True 
    
    def has_conflicting_precedence(self, from_xact, to_xact):
        from_xact_no = from_xact.transaction
        to_xact_no = to_xact.transactio
        return to_xact_no in self.graph and from_xact_no in self.graph[to_xact_no]
