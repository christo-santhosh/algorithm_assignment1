from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)
    def dfs(self, v, visited, stack):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, stack)
        stack.append(v)
    def reverse_graph(self):
        g_rev = Graph()
        for u in self.graph:
            for v in self.graph[u]:
                g_rev.add_edge(v, u)
        
        g_rev.nodes = self.nodes.copy()
        return g_rev
    def dfs_scc(self, v, visited, scc):
        visited.add(v)
        scc.append(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_scc(neighbor, visited, scc)
    def get_sccs(self):
        stack = []
        visited = set()
        for node in self.nodes:
            if node not in visited:
                self.dfs(node, visited, stack)
        g_rev = self.reverse_graph()
        visited.clear()
        sccs = []
        while stack:
            node = stack.pop()
            if node not in visited:
                scc = []
                g_rev.dfs_scc(node, visited, scc)
                sccs.append(sorted(scc))  
        return sccs
if __name__ == "__main__":
    g = Graph()
    edges = [
        ('a', 'b'), ('b', 'c'), ('c', 'a'), 
        ('d', 'c'), ('b', 'd'), ('c', 'e'), 
        ('d', 'e'), ('f', 'd'), ('e', 'f'), 
        ('g', 'e'), ('f', 'g'), ('h', 'f'), 
        ('g', 'h')
    ]
    for u, v in edges:
        g.add_edge(u, v)
    sccs = g.get_sccs()
    output_lines = [
        "Strongly Connected Components (SCCs):"
    ]
    for i, scc in enumerate(sccs, 1):
        scc_str = "{" + ", ".join(scc) + "}"
        output_lines.append(f"SCC {i}: {scc_str}")
    output_text = "\n".join(output_lines)
    print(output_text)
    with open("scc_results.txt", "w") as file:
        file.write(output_text)
