string = "Hello World"
str1 = '\n'.join(chr(ord(char) & 127) for char in string)
str2 = '\n'.join(f"i {i} char {char} orig {ord(char):02x} mod {ord(char) ^ 127:02x}" for i, char in enumerate(string))
str3 = '\n'.join(f"i {i} char {char} orig {ord(char):02x} mod {ord(char) ^ 127:02}")

print(str1)
print(str2)
