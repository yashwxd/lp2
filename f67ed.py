def transposition_cipher(key, message):
    num_columns = len(key)
    num_rows = (len(message) + num_columns - 1) // num_columns
    encrypted_message = ''.join(message[i % len(message)] for i in range(num_columns * num_rows))
    decrypted_message = ''.join(encrypted_message[(key.index(i) * num_rows):(key.index(i) * num_rows) + num_rows] for i in sorted(key))
    return encrypted_message, decrypted_message


# Test the encryption and decryption
key = [1, 0, 3, 2]
message = "pune vidhyatri ghriha college of engineeing pune"

encrypted_message, decrypted_message = transposition_cipher(key, message)
print("Encrypted message:", decrypted_message)
print("Decrypted message:", encrypted_message)
