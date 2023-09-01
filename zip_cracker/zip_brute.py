import zipfile
from tqdm import tqdm
import itertools

zip_file = "crackit.zip" #Path to your zipfile goes here
zip_file = zipfile.ZipFile(zip_file)

character_set = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

max_pass_length = 4

n_words = len(character_set) ** max_pass_length
print("Total password to test : ", n_words)


for password_length in range(1, max_pass_length + 1):
    for word in tqdm(itertools.product(character_set, repeat=password_length), total=len(character_set) ** password_length, unit="word",ascii =' //'):
        password = "".join(word)
        try:
            zip_file.extractall(pwd=password.encode())
        except:
            continue
        else:
            print("\n[+] Password found : ", password)
            exit(0)

print("[!] Password not found, try longer password or diffrent characterset.")
