import hashlib			#to use md5 encryption
from colorama import Fore	#to change color of text
from tqdm import tqdm		#for progress bar

flag = 0	#flag varibale determines if hash is cracked or not
cracked = ''	#if cracked plain text will be saved here

def encrypt(text):		#function to encrypt strings
	temp = text.strip()	#removing any white spaces
	enc = hashlib.md5(temp.encode()).hexdigest()	#encrypting with md5
	return enc	#returning encrypted value
	

def cracker(file,hash):		#function cracks hash
	global flag,cracked	#accessing global variables
	with open(file ,'r') as f:	#opening given file in read mode
		for password in tqdm(f):	#running loop for every string in file
			temp = encrypt(password)	#function call to encrypt string
			if(temp == hash):		#checking if string's hash value matches to given hash
				flag = 1		#setting flag as hash matched
				cracked = password	#storing plain text in global variable cracked
				break			#breaking loop
			else:
				pass

if __name__ == '__main__':
	hash = input("Paste your hash to be cracked : ").strip()	#taking hash input from user and removing white spaces
	file = input("Enter your password list file path : ")		#taking file path input from uset that to be used as password list
	
	try:	
		cracker(file,hash)		#function call to crack the given hash
		if(flag == 1):			#checking if hash cracked or not 
			print(f"{Fore.GREEN}Hash cracked, Plain text is : ",cracked)	#displaying plain text
		else:
			print(f"{Fore.RED}Hash couldn't be cracked ! use longer password list")		#hash not cracked displaying message
	except:
		print(f"{Fore.RED}Unknown Error")		#Incase anything goes wrong
