alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']

def encrypt(plain_text,shift): #hello h=7
    cipher_text=""
    for char in plain_text:
        pos=alphabet.index(char)
        new=(pos+shift)%26
        cipher_text+=alphabet[new]
    print("Here's the text after encryption:",cipher_text)

def decrypt(cipher_text,shift):
    print('NICE')

opt=input("Type 'e' for encryption & 'd' for decryption:\n")
msg=input("Type your message:\n")
key=int(input("Enter the value of shift key:\n"))

if opt=='e':
    encrypt(plain_text=msg,shift=key)

elif opt=='d':
    decrypt(cipher_text=msg,shift=key)


