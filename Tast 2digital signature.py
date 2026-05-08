# Import required libraries
from hashlib import sha256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
# Step 1: Generate RSA key pair
key = RSA.generate(2048)
# Store private and public keys
private_key = key
public_key = key.publickey()
print("RSA Key Pair Generated\n")
# Step 2: Original message
message = b"Hello Haroon"
print("Original Message:", message.decode())
# Step 3: Create SHA256 hash of message
hash_object = SHA256.new(message)
print("SHA256 Hash:", hash_object.hexdigest())
# Step 4: Sign the hash using private key
signature = pkcs1_15.new(private_key).sign(hash_object)
print("\nDigital Signature Created")
# Step 5: Verify signature using public key
try:
    # Verify original message hash with signature
    pkcs1_15.new(public_key).verify(hash_object, signature)
    print("Signature Verified Successfully")
except (ValueError, TypeError):
    print("Verification Failed")
# Step 6: Modify message slightly
modified_message = b"Hello haroon"
print("\nModified Message:", modified_message.decode())
# Create new hash for modified message
modified_hash = SHA256.new(modified_message)
# Step 7: Verify again using old signature
try:
    # Verification should fail because message changed
    pkcs1_15.new(public_key).verify(modified_hash, signature)
    print("Signature Verified")
except (ValueError, TypeError):
    print("Verification Failed (Message Changed)")