from Crypto.Util import number
import json

def generate_elgamal_keys(bits=1024):
    p = number.getPrime(bits) # Generate a large prime number p
    g = number.getRandomRange(2, p) # Generate a random base g
    x = number.getRandomRange(2, p-1) # Generate a random private key x
    y = pow(g, x, p) # Compute the public key y = g^x mod p
    return {"p": p, "g": g, "y": y}, {"p": p, "x": x}

public_key, private_key = generate_elgamal_keys()
with open("public_key.json", "w") as f:
    json.dump(public_key, f)
with open("private_key.json", "w") as f:
    json.dump(private_key, f)

print("[+] Khóa công khai đã được tạo và lưu vào public_key.json")
print("[+] Khóa bí mật đã được tạo và lưu vào private_key.json")