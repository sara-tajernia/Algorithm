from collections import defaultdict
from heapq import *
import math
import matplotlib.pyplot as plt

def input_data():
    n, m = list(map(int, input().split()))
    nodes = {}                                                                     #nodes[x, y]
    graph, cities, x_list, y_list, id_list, way, cars = [], [], [], [], [], [], []    # graph[start, finish, distance between 2 points, traffic]
                                                                                        # cities=[x_list, y_list, id_list] information to draw a map
                                                                                            #way[all the starts to, all the finish] information to draw a map
                                                                                                #cars[time of start, point of start, point of destination
    for i in range(n):
        id, x, y = input().split()
        x_list.append(float(x))
        y_list.append(float(y))
        id_list.append(id)
        coordinate = [float(x), float(y)]
        nodes[id] = coordinate
    for j in range(m):
        start, destination = input().split()
        way.append([start, destination])
        length = math.sqrt(pow((nodes[destination][0] - nodes[start][0]), 2) +          # find the distance between 2 connected points
                           pow((nodes[destination][1] - nodes[start][1]), 2))
        graph.append([start, destination, length, 0])                                   # trafic of all the ways at first is 0
        graph.append([destination, start, length, 0])
        
    num = int(input())
    for i in range(num):
        time, begin, end = input().split()
        cars.append([float(time), begin, end])
    cities = [x_list, y_list, id_list]
    return graph, cars, cities, way


def dijkstra(graph, start, destination):
    nodes = defaultdict(list)                   # nodes{start: [distance, finish, trafic]}
    for src, dist, distance, traffic in graph:
        nodes[src].append((distance, dist, traffic))

    min_heap, seen, shortest_path = [(0, start, ())], set(), {start: 0}             # use min_heap to find the best next node
                                                                                        # use seen variable to save all the nodes that we have been
                                                                                            # use shortest_path to save the shortest path to node
    cost, path = 'inf', []
    while min_heap:                                     # find the shortest path to node considering the traffic of each edge
        (cost, v1, path) = heappop(min_heap)
        if v1 not in seen:
            seen.add(v1)
            path += (v1,)
            if v1 == destination:
                break
            for distance2, v2, traffic2 in nodes.get(v1, ()):
                if v2 in seen:
                    continue
                prev = shortest_path.get(v2, None)
                next = cost + (distance2 * (1 + (0.3 * traffic2)))
                if prev is None or next < prev:
                    shortest_path[v2] = next
                    heappush(min_heap, (next, v2, path))

    if cost is not "inf":
        for i in range(len(path) - 1):                  # update the traffic according the shortest path that we found
            for j in range(len(graph)):
                if (path[i] == graph[j][0] and path[i + 1] == graph[j][1]) or \
                        (path[i] == graph[j][1] and path[i + 1] == graph[j][0]):
                    graph[j][3] += 1
        return cost, path, graph
    return float("inf"), None


def car(graph, cars):
    paths, all_path = [], []            # paths[cost, path, visited, start]use visited to ignore the cars that arrived the destination
                                            #all_path to save the paths that we dicided is the best to show in map bu red lines
    for i in range(len(cars)):
        for j in range(len(paths)):
            if paths[j][0] * 120 + paths[j][3] < cars[i][0] and paths[j][2] == False:
                for k in range(len(paths[j][1]) - 1):
                    for l in range(len(graph)):
                        if (graph[l][0] == paths[j][1][k] and graph[l][1] == paths[j][1][k + 1]) or \
                                (graph[l][0] == paths[j][1][k + 1] and graph[l][1] == paths[j][1][k]):      #reduce the trafic if the previous cars has left
                            graph[l][3] -= 1
                            paths[j][2] = True
        print('For car', i + 1, ':')
        cost, path, graph = dijkstra(graph, cars[i][1], cars[i][2])
        paths.append([cost, path, False, cars[i][0]])
        all_path.append(paths[i][1])
        print(paths[i][1])
        print(paths[i][0] * 120)
    return all_path

def Map(cities, ways, paths):
    x, y, id = cities
    for i in range (len(paths)):
        fig, ax = plt.subplots()
        for j in range(len(ways)):
            save = []
            for k in range(len(id)):
                plt.plot(y[k], x[k], 'bo')                 # find the coordination of all the cities in the map
                ax.annotate(id[k], (y[k], x[k]))
                if ways[j][0] == id[k] or ways[j][1] == id[k]:
                    save.append([y[k], x[k], id[k]])
                if len(save) == 2:
                    xs = [save[0][0], save[1][0]]
                    ys = [save[0][1], save[1][1]]
                    for l in range (len(paths[i])-1):           # check if the edge is common in the path make the road red else make it blue
                        if (save[0][2] == paths[i][l] and save[1][2] == paths[i][l+1]) or \
                                (save[1][2] == paths[i][l] and save[0][2] == paths[i][l+1]):
                            plt.plot(xs[0:2], ys[0:2], '-r')
                            break
                        else:
                            plt.plot(xs[0:2], ys[0:2], '-b')
                    break
        plt.show()

if __name__ == "__main__":
    graph, cars, cities, ways= input_data()
    paths = car(graph, cars)
    Map(cities, ways, paths)
