# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:34:17 2023

@author: bagul
"""

def generate_shared_secret(p, g, a, b):
    # Calculate A = g^a mod p
    A = pow(g, a, p)
    # Calculate B = g^b mod p
    B = pow(g, b, p)

    # Calculate the shared secret using A and b
    shared_secret_A = pow(B, a, p)
    # Calculate the shared secret using B and a
    shared_secret_B = pow(A, b, p)

    # Both shared secrets should be the same
    if shared_secret_A == shared_secret_B:
        return shared_secret_A

    raise Exception("Shared secrets do not match")

# Example usage
p = 23
g = 5

# Alice's private key
a = 6
# Bob's private key
b = 15

shared_secret = generate_shared_secret(p, g, a, b)

print("Shared Secret:", shared_secret)
