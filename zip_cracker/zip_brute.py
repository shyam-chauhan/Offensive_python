import zipfile
from tqdm import tqdm
import itertools


class zip_crack:

    def __init__():
        zip_file = ""
        char_set = ""
        max_pass_len = 0

    def info_in():
        global zip_file,char_set,max_pass_len
        zip_file = input("Path to your zipfile :")
        char_set = input("Provide character set that you want to use to crack password, DON'T REPEAT (default is a-z,A-Z,0-9) : ") or "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        max_pass_len = int(input("Provide maximum possible length of password(It will take time accordingly!) : "))


    def info_processor():
        global zip_file,char_set,max_pass_len
        zip_file = zipfile.ZipFile(zip_file)

        #print("Total password to test : ", total_tries())
    
        for password_length in range(1, max_pass_len + 1):
            for word in tqdm(itertools.product(char_set, repeat=max_pass_len), total=len(char_set) ** max_pass_len, unit="word",ascii =' //'):
                password = "".join(word)
                try:
                    zip_file.extractall(pwd=password.encode())
                except:
                    continue
                else:
                    print("\n[+] Password found : ", password)
                    exit(0)

        print("[!] Password not found, try longer password or diffrent characterset.")



    def total_tries():
        return (len(char_set) ** max_pass_len)


if __name__ == "__main__":
    z = zip_crack
    z.info_in()
    z.info_processor()
