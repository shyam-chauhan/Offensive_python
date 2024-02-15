def filler(str):
    str += 'x'
    return str,len

def encrypt(str):
    str1 = ''
    str2 = ''
    l = len(str)
    if(l%2):
        str,l = filler(str)
    else:
        pass
    for chr in range(0,l):
        if (chr%2==0):
            str2 += s[chr]
        else:
            str1 += s[chr]
    return str1+str2

def decrypt(str):
    pass



if __name__ == '__main__':
    print("encryption is ",encrypt('abcde'))