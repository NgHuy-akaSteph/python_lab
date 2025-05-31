import random
import string
import time
from lzw_compress import lzw_pure_compress, lzw_codes_to_bytes
from huffman_compress import huffman_compress
from zlib_compress import zlib_compress


# Hàm tạo file
def create_repetitive_text(filename, size_mb=1):
    pattern = "abc"  # Chuỗi lặp -> Có thể thay đổi theo tạo độ lặp khác nhau
    data = (pattern * (int(size_mb * 1024 * 1024 / len(pattern))))[:int(size_mb * 1024 * 1024)]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)
    print(f"Created {filename} with size ~{size_mb}MB")

def create_random_text(filename, size_mb=1):
    data = ''.join(random.choice(string.ascii_lowercase) for _ in range(int(size_mb * 1024 * 1024)))
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)
    print(f"Created {filename} with size ~{size_mb}MB")

# Hàm đánh giá
def evaluate_compression(input_file):
    # Read input file
    with open(input_file, 'rb') as f:
        data = f.read()
    original_size = len(data)
    data_str = data.decode('utf-8', errors='ignore')

    # Huffman compression
    start_time = time.perf_counter()
    huffman_compressed, huffman_codes = huffman_compress(data_str)
    huffman_time = time.perf_counter() - start_time
    huffman_size = len(huffman_compressed) + len(str(huffman_codes).encode())  # Include code table size
    huffman_ratio = original_size / huffman_size if huffman_size > 0 else float('inf')

    # LZW pure compression
    start_time = time.perf_counter()
    lzw_codes = lzw_pure_compress(data_str)
    lzw_compressed = lzw_codes_to_bytes(lzw_codes)
    lzw_pure_time = time.perf_counter() - start_time
    lzw_pure_size = len(lzw_compressed)
    lzw_pure_ratio = original_size / lzw_pure_size if lzw_pure_size > 0 else float('inf')

    # LZW zlib compression (optional)
    start_time = time.perf_counter()
    zlib_compressed = zlib_compress(data)
    zlib_time = time.perf_counter() - start_time
    zlib_size = len(zlib_compressed)
    zlib_ratio = original_size / zlib_size if zlib_size > 0 else float('inf')

    # Print results
    print(f"File: {input_file}")
    print(f"Original Size: {original_size} bytes")
    print("\nHuffman Coding:")
    print(f"  Compressed Size: {huffman_size} bytes")
    print(f"  Compression Ratio: {huffman_ratio:.2f}")
    print(f"  Compression Time: {huffman_time:.4f} seconds")
    print("\nLZW:")
    print(f"  Compressed Size: {lzw_pure_size} bytes")
    print(f"  Compression Ratio: {lzw_pure_ratio:.2f}")
    print(f"  Compression Time: {lzw_pure_time:.4f} seconds")
    print("\nUse zlib:")
    print(f"  Compressed Size: {zlib_size} bytes")
    print(f"  Compression Ratio: {zlib_ratio:.2f}")
    print(f"  Compression Time: {zlib_time:.4f} seconds")
    print("-" * 50)

# Tạo file đầu vào
create_repetitive_text("repetitive_text.txt", size_mb=1)
create_random_text("random_text.txt", size_mb=1)
create_random_text("random_text_2.txt", size_mb=10)

# Đánh giá trên hai file
input_files = ["repetitive_text.txt", "random_text.txt", "random_text_2.txt"]
for file in input_files:
    evaluate_compression(file)