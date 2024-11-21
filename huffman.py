import heapq
from collections import defaultdict, Counter
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
def huffman_codes(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    root = heap[0]  
    huffman_code = {}
    def generate_code(node, current_code):
        if node:
            if node.char is not None:
                huffman_code[node.char] = current_code
            generate_code(node.left, current_code + "0")
            generate_code(node.right, current_code + "1")
    generate_code(root, "")
    return huffman_code
def encode_text(text, huffman_code):
    return ''.join(huffman_code[char] for char in text)
text = input("Enter the text to encode: ")
huffman_code = huffman_codes(text)  
print("Huffman Codes:")
for char, code in huffman_code.items():
    print(f"'{char}': {code}")
encoded_text = encode_text(text, huffman_code)
print("\nEncoded Text:")
print(encoded_text)