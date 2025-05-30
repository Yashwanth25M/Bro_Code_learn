# (05:58:45)

# encryption program

# import random
# import string

# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()

# random.shuffle(key)

# # ENCRYPTION
# plain = input("enter a message to encrypt")
# cipher_text = ""

# for letter in plain:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f"Original messsage : {plain}")
# print(f"Encrypted messsage : {cipher_text}")

# # DECRYPTION
# cipher_text = input("enter a message to decrypt")
# plain = ""

# for letter in cipher_text:
#     index = key.index(letter)
#     plain += chars[index]

# print(f"Encrypted messsage : {cipher_text}")
# print(f"Original messsage : {plain}")


#More advanced program



# import random
# import string

# # Define character set
# chars = list(" " + string.punctuation + string.digits + string.ascii_letters)

# # Ask user for mode
# mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()

# # ENCRYPTION
# if mode == 'e':
#     # Generate random 10-digit numeric key
#     seed_key = "".join(random.choices(string.digits, k=10))
#     print(f"\n🔑 Your encryption key (save this!): {seed_key}")

#     # Generate key using seed
#     random.seed(seed_key)
#     key = chars.copy()
#     random.shuffle(key)

#     plain = input("Enter a message to encrypt: ")
#     cipher_text = ""
#     for letter in plain:
#         if letter not in chars:
#             print(f"Unsupported character: '{letter}'")
#             exit()
#         index = chars.index(letter)
#         cipher_text += key[index]

#     print(f"\n🧾 Encrypted message: {cipher_text}")

# # DECRYPTION
# elif mode == 'd':
#     seed_key = input("Enter your 10-digit key: ")
#     if not (seed_key.isdigit() and len(seed_key) == 10):
#         print("Invalid key format. Must be exactly 10 digits.")
#         exit()

#     random.seed(seed_key)
#     key = chars.copy()
#     random.shuffle(key)

#     cipher_text = input("Enter the encrypted message: ").strip()
#     plain = ""
#     for letter in cipher_text:
#         if letter not in key:
#             print(f"Unsupported character in ciphertext: '{letter}'")
#             exit()
#         index = key.index(letter)
#         plain += chars[index]

#     print(f"\n✅ Decrypted message: {plain}")

# else:
#     print("Invalid mode selected.")