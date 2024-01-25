import math
import random

n = 0

def random_prime():
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 	401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
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
    return ((text**key) % n)

def decrypt(cipher,key,n):
    return((cipher**key) % n)

def print_str(str):
    print("Enter text to "+str+" : ")



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
                text = int(input("Enter text to encrypt : "))
                key = int(input("Enter key for encryption : "))
                n = int(input("Enter value of 'n' : "))
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
    except:
        print("Error occured!")
        
            
                     
