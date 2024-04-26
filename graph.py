from itertools import permutations
import brua_order

class HasseDiagram:
    def __init__(self, subset) -> None:   
        n = len(subset)
        self.hasse_diagram = [[0 for _ in range(n)] for _ in range(n)]
        self.graph_neig = [[0 for _ in range(n)] for _ in range(n)]


        for i in range(n):
            for j in range(n):
                if brua_order.compare(subset[i], subset[j]):
                    self.graph_neig[i][j] = 1

        for i in range(n):
            for j in range(n):
                if self.graph_neig[i][j] == 1:
                    is_neighbor = True
                    for u in range(n):
                        if u != i and u != j and self.graph_neig[i][u] == 1 and self.graph_neig[u][j] == 1:
                            is_neighbor = False
                            break
                    if is_neighbor:
                        self.hasse_diagram[i][j] = 1
        for i in range(n):
            self.hasse_diagram[i][i] = 0


perms = list(permutations([1, 2, 3]))
a = HasseDiagram(perms)
