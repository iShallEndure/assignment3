import heapq
from collections import defaultdict, namedtuple

# Define a node class for the Huffman tree
class Node(namedtuple("Node", ["char", "freq"])):
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        heapq.heappush(heap, merged)

    huffman_tree = heapq.heappop(heap)
    return huffman_tree

def generate_codes(node, prefix="", codebook=defaultdict(str)):
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        generate_codes(node[0], prefix + "0", codebook)
        generate_codes(node[1], prefix + "1", codebook)
    return codebook

# Example character frequencies
frequencies = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}

huffman_tree = huffman_coding(frequencies)
codes = generate_codes(huffman_tree)

print("Huffman Codes:", codes)