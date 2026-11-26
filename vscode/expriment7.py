
# Experiment 7: RSA and Diffie-Hellman Algorithms

# ---------------- RSA Algorithm ----------------

# Select two prime numbers
p = 61
q = 53

# Calculate n and Euler's totient
n = p * q
phi = (p - 1) * (q - 1)

# Public and private keys
e = 17
d = pow(e, -1, phi)

# Original message
message = 65

# Encryption
ciphertext = pow(message, e, n)

# Decryption
decrypted = pow(ciphertext, d, n)

print("----- RSA Algorithm -----")
print("Original Message:", message)
print("Public Key:", (e, n))
print("Private Key:", (d, n))
print("Encrypted Message:", ciphertext)
print("Decrypted Message:", decrypted)


# ------------ Diffie-Hellman Algorithm ------------

# Public parameters
prime = 23
generator = 5

# Private keys of Alice and Bob
sparsh_private = 6
vish_private = 15

# Calculate public keys
sparsh_public = pow(generator, sparsh_private, prime)
vish_public = pow(generator, vish_private, prime)

# Calculate shared secret keys
sparsh_shared = pow(vish_public, sparsh_private, prime)
vish_shared = pow(sparsh_public, vish_private, prime)

print("\n----- Diffie-Hellman Key Exchange -----")
print("Alice Public Key:", sparsh_public)
print("Bob Public Key:", vish_public)
print("Alice Shared Secret:", sparsh_shared)
print("Bob Shared Secret:", vish_shared)

if sparsh_shared == vish_shared:
    print("Shared Secret Established Successfully!")
else:
    print("Key Exchange Failed!")
