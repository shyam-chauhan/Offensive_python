import math
import random

key_size = 16
half_key = (key_size//2)+2
print(half_key)


def is_prime(n):
    if(n<=1):
        return False
    else:
        for i in range(2,int((n**0.5)+1)):
            if((n%i)==0):
                return False
        return True

def random_prime():
    global key_size
    while True:
        rand_num = random.randrange(2**(key_size-1),2**key_size)
        if is_prime(rand_num):
            return rand_num

def gcd_find(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def key_gen():
    p = random_prime()
    q = random_prime()
    n = p*q
    fin = (p-1)*(q-1)
    e = random.randrange(2,fin)
    while(gcd_find(e,fin) != 1):
        e = random.randrange(2,fin)
    pbk = e
    prk = pow(pbk,-1,fin)
    return pbk,prk,n
    
def encrypt(text,key,n):
    encrypted_text = ""
    global key_size
    for i in text:
        num = ord(i)
        temp = str(pow(num,key,n))
        while(len(temp) != half_key):
            temp = str(0) + temp
        encrypted_text += temp
    return encrypted_text
   

def decrypt(cipher,key,n):
    plaintext = ""
    ascii_val = ""
    cipher = str(cipher)
    global key_size
    for i in cipher:
        ascii_val += i
        if(len(ascii_val) == half_key):
            ascii_val = int(ascii_val)
            num = pow(ascii_val, key, n)
            text = chr(num)
            plaintext += text
            ascii_val = ""
    return plaintext


        
if __name__ == '__main__':
    pbk,prk,n = key_gen()
    print("pbk is :", pbk)
    print("prk is :", prk)
    print("n is :", n)
    cipher = encrypt("hello",pbk,n)
    decrypted_text = decrypt(cipher,prk,n)
    print("cipher is :", cipher)
    print("decrypted text :",decrypted_text)
