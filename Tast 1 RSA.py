import random
# Function to find Greatest Common Divisor (GCD)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# Function to find Modular Multiplicative Inverse
def multiplicative_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1 = 1
    temp_phi = phi
    # Extended Euclidean Algorithm
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1:
        return d + phi
# Function to generate RSA public and private keys
def generate_keypair(p, q):
    # Step 1: Calculate n
    n = p * q
    # Step 2: Calculate Euler Totient Function
    phi = (p - 1) * (q - 1)
    # Step 3: Choose random e
    e = random.randrange(2, phi)
    # Check if e and phi are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = gcd(e, phi)
    # Step 4: Generate private key d
    d = multiplicative_inverse(e, phi)
    # Public Key = (e, n)
    # Private Key = (d, n)
    return ((e, n), (d, n))
# Function to encrypt message
def encrypt(public_key, plaintext):
    # Separate e and n from public key
    e, n = public_key
    # Encrypt each character
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher
# Function to decrypt message
def decrypt(private_key, ciphertext):
    # Separate d and n from private key
    d, n = private_key
    # Decrypt each number back to character
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)
# ---------------- MAIN PROGRAM ----------------
# Take prime numbers from user
p = int(input("Enter first prime number: "))
q = int(input("Enter second prime number: "))
# Generate RSA keys
public_key, private_key = generate_keypair(p, q)
# Display keys
print("\nPublic Key:", public_key)
print("Private Key:", private_key)
# Take message input from user
message = input("\nEnter message: ")
# Encrypt the message
encrypted_msg = encrypt(public_key, message)
print("\nEncrypted Message:", encrypted_msg)
# Decrypt the message
decrypted_msg = decrypt(private_key, encrypted_msg)
print("Decrypted Message:", decrypted_msg)