from collections import deque, defaultdict

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    friends = set()
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            friends.add(node)
            queue.extend(graph[node] - visited)
    
    return friends - {start}

def find_mutual_friends(graph, user1, user2):
    friends_user1 = bfs(graph, user1)
    friends_user2 = bfs(graph, user2)
    return friends_user1.intersection(friends_user2)

# Example graph representation
social_network = {
    'Alice': {'Bob', 'Carol'},
    'Bob': {'Alice', 'David', 'Eve'},
    'Carol': {'Alice', 'Eve'},
    'David': {'Bob'},
    'Eve': {'Bob', 'Carol'},
}

# Finding mutual friends between Alice and Bob
mutual_friends = find_mutual_friends(social_network, 'Alice', 'Bob')
print(f"Mutual friends between Alice and Bob: {mutual_friends}")