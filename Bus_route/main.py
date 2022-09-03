from collections import defaultdict
class Map:
    def __init__(self):
        self.graph = defaultdict(list)

    def edge(self, src, dest):
        self.graph[src].append(dest)

    def DFS(self, n):
        list = []
        visited = set()
        self.util(1, visited, list, n)

    def util(self, src, visited, list, n):
        visited.add(src)
        list.append(src)
        for neighbour in self.graph[src]:
            if neighbour not in visited:
                 self.util(neighbour, visited, list, n)
        if int(n) in list:
            print(' '.join(map(str, list)))
            exit(0)
        else:
            list.remove(src)

if __name__ == '__main__':
    station = Map()
    n = input()
    stations = input().split()
    for i in range(2, int(n) + 1):
        station.edge(int(stations[i-2]), i)

    station.DFS(n)