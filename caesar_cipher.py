alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']

def encrypt(plain_text,shift): 
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
          pos=alphabet.index(char)
          new=(pos+shift)%26
          cipher_text+=alphabet[new]
        elif(char.isupper()):
           cipher_text += chr((ord(char) + shift-65) % 26 + 65)
        else:
           cipher_text+=char
    print("Here's the text after encryption:",cipher_text)   ##Encryption function

def decrypt(cipher_text,shift):
    plain_text=""
    for c in cipher_text:
        if c in alphabet:
           p=alphabet.index(c)
           n=(p-shift)%26
           plain_text+=alphabet[n]
        elif c.isupper():
           plain_text+= chr((ord(c) - shift-65) % 26 + 65)
        else:
           plain_text+=c
    print("The message after decryption is: ",plain_text)    ##Decryption function


flag=True
while flag:
    opt=input("Type 'enc' for encryption & 'dec' for decryption:\n")
    msg=input("Type your message:\n")
    key=int(input("Enter the value of shift key:\n"))        

    if opt=='enc':
      encrypt(plain_text=msg,shift=key)

    elif opt=='dec':
      decrypt(cipher_text=msg,shift=key)
    
    con=input("Type 'yes' to continue; type 'no' to exit\n")
    if con=='no':
      flag=False
print("Good bye. Have a nice day!!")



