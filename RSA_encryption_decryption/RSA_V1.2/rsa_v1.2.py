import math
import random

n = 0

def random_prime():
    '''
    generates random prime number from given list prime_numbers
    :return: prime number 
    '''
    prime_numbers = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101]
    return random.choice(prime_numbers)

def key_gen():
    '''
    private and public key generator functions for RSA
    :return: private key, public key and N
    '''
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
    '''
    encryps given text using RSA method by converting letters to relevant ASCII 
    :param text: text you want to enctypt
    :param key: key to be used for encryption
    :param n: N to be used for mod opration
    '''
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
    '''
    decrypts given cipher using RSA method and converts ASCII to chracters individually 
    :param cipher: cipher(numbers) you want to decrypt 
    :param key: key to be used for decryption
    :param n: N to be used for mod opration
    '''
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
        
            
                     
