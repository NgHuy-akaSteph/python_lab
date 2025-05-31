import json
import hashlib

def elgamal_verify(message, signature, public_key):
    p = public_key["p"]
    g = public_key["g"]
    y = public_key["y"]
    r, s = signature["r"], signature["s"]
    if not (0 < r < p and 0 <= s < p-1):
        return False
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % p
    left = pow(g, h, p)
    right = (pow(y, r, p) * pow(r, s, p)) % p
    return left == right

with open("public_key.json", "r") as f:
    public_key = json.load(f)
with open("message.txt", "r") as f:
    message = f.read().strip()
with open("signature.json", "r") as f:
    signature = json.load(f)
is_valid = elgamal_verify(message, signature, public_key)
if is_valid:
    print("[+] Chữ ký hợp lệ")
    print(message)
else:
    print("[-] Chữ ký không hợp lệ hoặc thông điệp không đúng")