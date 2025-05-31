import hashlib

def hash_message(message):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(message.encode('utf-8'))
    return sha1_hash.hexdigest()

def hash_file(file_path):
    try:
        sha1_hash = hashlib.sha1()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):  # Read file in 4KB chunks
                sha1_hash.update(chunk)
        return sha1_hash.hexdigest()
    except Exception as e:
        return f"Error reading file: {e}"

if __name__ == "__main__":
    input_message = input("Enter the message: ")
    print(f"Hashed from message: {hash_message(input_message)}")
    input_file_path = input("Enter the file path: ")
    print(f"Hashed from file: {hash_file(input_file_path)}")
