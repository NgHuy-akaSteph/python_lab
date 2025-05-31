import zlib

def zlib_compress(data):
    if not data:
        return b""
    # Convert string to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    compressed = zlib.compress(data, level=6)
    return compressed