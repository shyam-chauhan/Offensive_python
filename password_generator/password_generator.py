import random

password = [] #pre-final pass phrase
final_pass = ''  #final pass phrase
le1 = 0 #length of numbers in password
le2 = 0 #length of special characters in password
pass_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #alphabets

digits = ['0','1','2','3','4','5','6','7','8','9'] #numbers to be used in password

symb = ['!','@','#','$','%','&'] #special characters to be used in password

len = int(input("How much long password you want to generate? : ")) #taking input of password length

sel = str(input("Do you want to add numbers? (y/n) : ")) #choose to add numbers or not

if(sel == 'y' or sel == 'Y'):
    le1 = int(input("How many numbers you want to add? : ") or 0) #how many numbers 
    for i in range(0,le1):
    	x = random.choice(digits)  #selecting random numbers from digits
    	password.append(x) #adding it to pre-final pass phrase
else:
    pass
    
sel = str(input("Do you want to add symbols? (y/n) :")) #special characters to be used in password
if(sel == 'y' or sel == 'Y'):
    le2 = int(input("How many symbols you want to add? : ")or 0) #how many special characters
    for i in range(0,le2):
    	x = random.choice(symb) #selecting random special characters from symb
    	password.append(x) #adding it to pre-final pass phrase
else:
    pass

remaining = int(len - le1 - le2) #couting remaining password length
for i in range(0,remaining):
	x = random.choice(pass_list) #selecting random character from pass_list
	password.append(x) #adding it to pre-final pass phrase


password = random.sample(password,len) #shuffling pass phrase to make it random

for i in password:
	final_pass += i  #converting to string
print("\nGenerated secure password is : ",final_pass) #printing generated password
