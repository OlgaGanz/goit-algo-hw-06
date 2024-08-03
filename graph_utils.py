import networkx as nx
import heapq


def dfs(graph: nx.Graph, start_vertex):
    visited = set()
    stack = [start_vertex]  
    while stack:
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))


def bfs(graph: nx.Graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
#     print(visited)
    bfs(graph, queue, visited)


def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]
    while pq:
        # print("pq: ", pq)
        # print("sp:", shortest_paths)
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths
