

import hashlib
import os

password = "mypassword123"


hash_without_salt = hashlib.sha256(password.encode()).hexdigest()

print("----- Password Hashing Without Salt -----")
print("Original Password:", password)
print("Hash Without Salt:", hash_without_salt)


salt1 = os.urandom(16)
salt2 = os.urandom(16)

hash_with_salt1 = hashlib.sha256(salt1 + password.encode()).hexdigest()
hash_with_salt2 = hashlib.sha256(salt2 + password.encode()).hexdigest()

print("\n----- Password Hashing With Salt -----")
print("Salt 1:", salt1.hex())
print("Hash With Salt 1:", hash_with_salt1)

print("\nSalt 2:", salt2.hex())
print("Hash With Salt 2:", hash_with_salt2)

print("\n----- Comparison -----")

if hash_without_salt == hash_with_salt1:
    print("Hashes are same")
else:
    print("Hashes are different")

if hash_with_salt1 != hash_with_salt2:
    print("Different salts generate different hashes.")

print("Password hashing comparison completed.")
