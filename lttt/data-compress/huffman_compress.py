import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq):
    heap = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        internal = HuffmanNode(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        heapq.heappush(heap, internal)
    return heap[0]

def build_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}
    if root.char is not None:
        codes[root.char] = current_code or "0"
    if root.left:
        build_codes(root.left, current_code + "0", codes)
    if root.right:
        build_codes(root.right, current_code + "1", codes)
    return codes

def huffman_compress(data):
    if not data:
        return b"", {}
    freq = Counter(data)
    root = build_huffman_tree(freq)
    codes = build_codes(root)
    encoded = "".join(codes[c] for c in data)
    # Convert binary string to bytes
    padded_encoded = encoded + "0" * (8 - len(encoded) % 8)
    compressed = bytes(int(padded_encoded[i:i+8], 2) for i in range(0, len(padded_encoded), 8))
    return compressed, codes