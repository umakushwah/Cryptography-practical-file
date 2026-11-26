
# Experiment 8: AES Encryption and SHA-256 Hashing

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib

# ---------------- AES Encryption ----------------

# Original message
message = "Hello, this is AES encryption practical."

# Generate a 16-byte secret key
key = get_random_bytes(16)

# Generate AES cipher object
cipher = AES.new(key, AES.MODE_CBC)

# Encrypt the message
ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))

# Decrypt the message
decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("----- AES Encryption -----")
print("Original Message:", message)
print("Secret Key:", key.hex())
print("Encrypted Message:", ciphertext.hex())
print("Decrypted Message:", decrypted.decode())


# ---------------- SHA-256 Hashing ----------------

# Generate SHA-256 hash
hash_object = hashlib.sha256(message.encode())
hash_value = hash_object.hexdigest()

print("\n----- SHA-256 Hashing -----")
print("Original Message:", message)
print("SHA-256 Hash:", hash_value)
print("Hash Length:", len(hash_value), "characters")
