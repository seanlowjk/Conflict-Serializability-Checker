class PrecedenceGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_xact, to_xact):
        if from_xact not in self.graph:
            self.graph[from_xact] = {}

        if to_xact not in self.graph[from_xact]:
            self.graph[from_xact][to_xact] = True 
    
    def has_conflicting_precedence(self, from_xact, to_xact):
        return to_xact in self.graph and from_xact in self.graph[to_xact]
