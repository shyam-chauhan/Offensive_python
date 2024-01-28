import math
import random

n = 0

def random_prime():
    prime_numbers = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101]
    return random.choice(prime_numbers)

def key_gen():
    global n
    p = random_prime()
    q = random_prime()
    n = p*q
    fin = (p-1)*(q-1)
    for e in range(2,fin):
        if(math.gcd(e,fin)==1):
            pbk = e
            break
    for d in range(1,fin):
        res = (d * pbk) % fin
        if(res == 1):
            prk = d
            break
    return pbk,prk,n
        

def encrypt(text,key,n):
    encrypted_text = ""
    for i in text:
        if(i.isupper()):
            encoded_letter = (int(ord(i)) - 54)    
        elif(i.islower()):
            encoded_letter =(int(ord(i)) - 86)
            print(encoded_letter)
        temp = str((encoded_letter**key) % n)
        while(len(temp) != 4):
            temp = str(0) + temp
        encrypted_text += temp
    return encrypted_text

def decrypt(cipher,key,n):
    count = 1
    ascii_val = ""
    decoded_text = ""
    cipher = str(cipher)
    for i in cipher:
        ascii_val += i
        if(len(ascii_val) == 4):
            ascii_val = int(ascii_val)
            decrypted_text = (ascii_val**key) % n
            temp = (int(decrypted_text) + 86)
            decoded_text += chr(temp)
            ascii_val= ""
        
        count = count + 1
    return decoded_text
        

if __name__ == '__main__':
    choice = 1
    try:
        while(choice != 4):
            choice = int(input("1.For key generation \n2.For Encryption \n3.For decryption \n4.Exit \nEnter number : "))
            if(choice == 1):
                pbk,prk,n = key_gen()
                print("Public key is : ",pbk)
                print("private key is : ",prk)
                print("'n' is : ",n)
            elif(choice == 2):
                text = input("Enter text to encrypt : ")
                key = int(input("Enter key for encryption : "))
                n = int(input("Enter value of 'n' : "))
                msg = [pow(ord(char), key, n) for char in text]
                print(msg)
                print("Cipher is : ",encrypt(text,key,n))
            elif(choice == 3):
                cipher = int(input("Enter cipher to decrypt : "))
                key = int(input("Enter key for decryption : "))
                n = int(input("Enter value of 'n' : "))
                print("Text is : ",decrypt(cipher,key,n))
            elif(choice == 4):
                exit()
            else:
                print("Error ! choose from following options in numbers")
    except Exception as e:
        print("Error occured!",e)
        
            
                     
