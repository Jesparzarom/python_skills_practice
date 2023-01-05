# THIS CODE IS AN EXAMPLE IN CISCO NETACAD. NOT MINE.

# Cifrado
text = input("text: ")
cipher = ''

for char in text:
    
    if not char.isalpha():
        continue
    
    char = char.upper()
    code = ord(char) + 1
    
    if code >= ord('Z'):
        code = ord('A')
        
    cipher += chr(code)

print("cipher:", cipher)


# Descifrado
decipher = ""
for let in cipher:
    code = ord(let) - 1
    if code < ord('A'):
        code = ord('Z')
    decipher += chr(code)
    
print(decipher)
    