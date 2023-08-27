import hashlib

def read_dictionary(file_path):
	with open(file_path, 'r') as file:
		return [line.strip() for line in file]

def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()


def crack_password(target_hash,dictionary):
	for word in dictionary:
		hashed_word = hash_password(word)
		if hashed_word == target_hash:
			return word
	return None

if __name__ == "__main__":
	target_hash = "2d00c503a7a9910fa619bd03fe770cd3b47606d18c327a8dc191cee2770dd7ab" ##give your target hash here
	dictionary_file = "dictionary.txt" #this is path to your word list file
	dictionary = read_dictionary(dictionary_file)
	cracked_password = crack_password(target_hash, dictionary)

	if cracked_password:
		print(f"Password cracked, the password is : {cracked_password}")
	else:
		print("Password not found in dictionary")
