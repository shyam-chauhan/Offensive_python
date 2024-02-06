import numpy as np

def j_replace(text_lst):
    '''
    replaces all charachter j from list to character i
    :param text_lst: list of elemets
    :return: list of characters without j
    '''
    return ['i' if ch == 'j' else ch for ch in text_lst]

def filler(text_lst):
    '''
    adds x if there is character repeatation or string characters are odd
    :param text_lst: text list with possible repetative characters(e.g. ll,cc etc.)
    :return: list with filler x added between repetative characters and even size list
    '''
    for j in range(0,len(text_lst)-1):
        if(text_lst[j] == text_lst[j+1]):
            text_lst.insert(j+1,'x')

    if(len(text_lst)%2!=0):
        text_lst.append('x')
    return text_lst

def dupli_checker(key):
    '''
    removes repetative characters from key
    :param key: list with possible repetative characters
    :return: list with removed repetative characters
    '''
    new_key = []
    for chr in key:
        if chr not in new_key:
            new_key += chr
    return new_key

def list_matrix(key):
    '''
    uses key to generate list from which main matrix will be constructed
    :param key: key using which we need to construct playfair matrix
    :return: list with key characters at starting indices 
    '''
    alphabets = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lst = list(key)
    for i in alphabets:
        if i in key:
            pass
        else:
            lst.append(i)
    return lst

def matrix_gen(key):
    '''
    generates playfair matrix for encryption or decryption
    :param key: key to be used to generate matrix
    :return: constructed plafair matrix
    '''
    temp= []
    matrix = []
    lst = list_matrix(key)
    for i in lst:
        temp.append(i)
        if(len(temp)==5):
            matrix.append(temp)
            temp = []

    return np.array(matrix)
    
def encrypt(text,key):
    '''
    Encrypts text using playfair cypher technique
    :param text: plain text that is to be encrypted
    :param key: key to be used for encryption
    :return: Encrypted text string
    '''
    key = dupli_checker(key)
    plain_text = list(text)
    # print(plain_text)
    plain_text = filler(plain_text)
    # print(plain_text)
    plain_text = j_replace(plain_text)
    m = matrix_gen(key)
    cipher = []
    print("generated matrix is :\n",m)
    for chr in range(0,len(plain_text),2):
        row1 ,col1 = np.where(m == plain_text[chr])
        row2, col2 = np.where(m == plain_text[chr+1])
        row1,col1,row2,col2=int(row1),int(col1),int(row2),int(col2)
        if(row1==row2):
            col1=(col1+1)%5
            col2=(col2+1)%5
        elif(col1==col2):
            row1=(row1+1)%5
            row2=(row2+1)%5
        else:
            col1,col2=col2,col1
        cipher.append(m[row1][col1])
        cipher.append(m[row2][col2])

    cipher = ''.join(cipher)
    return cipher

def decrypt(cipher,key):
    '''
    Decrypts cipher using playfair cypher technique
    :param cipher: cipher text that is to be decrypted
    :param key: key to be used for decryption
    :return: decrypted text string
    '''
    key = dupli_checker(key)
    m = matrix_gen(key)
    cipher_list = list(cipher)
    decrypted= []
    for chr in range(0,len(cipher_list),2):
        row1 ,col1 = np.where(m == cipher_list[chr])
        row2, col2 = np.where(m == cipher_list[chr+1])
        row1,col1,row2,col2=int(row1),int(col1),int(row2),int(col2)
        if(row1==row2):
            col1=(col1-1)%5
            col2=(col2-1)%5
        elif(col1==col2):
            row1=(row1-1)%5
            row2=(row2-1)%5
        else:
            col1,col2=col2,col1

        decrypted.append(m[row1][col1])
        decrypted.append(m[row2][col2])

    while 'x' in decrypted:
        decrypted.remove('x')

    decrypted = ['i/j' if ch=='i' else ch for ch in decrypted]
    
    decrypted = ''.join(decrypted)
    return decrypted

if __name__ == '__main__':
    '''
    Main method
    '''
    choice = 1
    while(choice != 3):
        try:
            choice = int(input("1.For Encryption \n2.For Decryption \n3.Exit \nEnter number : "))
            if(choice == 1):
                #encryption
                text = input("Enter text to Encrypt : ")
                key = input("Enter key :")
                print("Encrypted text is :",encrypt(text,key))
            elif(choice == 2):
                #decryption
                text = input("Enter text to Decrypt : ")
                key = input("Enter key :")
                print("Decrypted text is :",decrypt(text,key))
            elif(choice == 3):
                #exit
                exit()
            else:
                #something not from following options !!
                print("Error ! choose from following options in numbers")
        except Exception as e:
            #catching exceptions
            print("Error occured! : ",e)