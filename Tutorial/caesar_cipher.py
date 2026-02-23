def caesar_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
           
            if char.isupper():
               
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
               
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
          
            result += char
    
    return result

def caesar_decrypt(text, shift):
   
    return caesar_encrypt(text, -shift)

print("Caesar Cipher Program")
print("1. Encrypt")
print("2. Decrypt")

choice = input("\nEnter your choice (1/2): ")

if choice == '1':
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted = caesar_encrypt(message, shift)
    print(f"\nEncrypted message: {encrypted}")
    
elif choice == '2':
    message = input("Enter the message to decrypt: ")
    shift = int(input("Enter the shift value: "))
    decrypted = caesar_decrypt(message, shift)
    print(f"\nDecrypted message: {decrypted}")
    
else:
    print("Invalid choice!")
