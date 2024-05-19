class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        def f(i):
            if i == n-1:
                return [[n-1]]
            return [[i] + p for c in graph[i] for p in f(c)]
        return f(0)