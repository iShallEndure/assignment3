import heapq

def prim_mst(graph):
    start_node = next(iter(graph))
    mst = []
    visited = set()
    min_heap = [(0, start_node, None)]  # (weight, node, parent)

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            if parent is not None:
                mst.append((parent, node, weight))
            for neighbor, cost in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(min_heap, (cost, neighbor, node))
    
    return mst

# Example graph representation
graph = {
    'A': {'B': 4, 'H': 8},
    'B': {'A': 4, 'C': 8, 'H': 11},
    'C': {'B': 8, 'D': 7, 'I': 2, 'F': 4},
    'D': {'C': 7, 'E': 9, 'F': 14},
    'E': {'D': 9, 'F': 10},
    'F': {'C': 4, 'D': 14, 'E': 10, 'G': 2},
    'G': {'F': 2, 'H': 1, 'I': 6},
    'H': {'A': 8, 'B': 11, 'G': 1, 'I': 7},
    'I': {'C': 2, 'G': 6, 'H': 7}
}

mst = prim_mst(graph)
print("Minimum",mst)