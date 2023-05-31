import random
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Compute d such that d*e ≡ 1 (mod phi)
    d = pow(e, -1, phi)

    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted

def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted)

# Example usage
p = 17
q = 11
public_key, private_key = generate_keypair(p, q)

message = "Hello, World!"
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)

