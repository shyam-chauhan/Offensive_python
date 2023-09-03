import whois
import pyfiglet

def info_in():
    global domain_name
    domain_name = str(input("Enter Domain name to search : " ))


def lookup(domain_name):

    try:
        info = whois.whois(domain_name)
        banner = pyfiglet.figlet_format(domain_name)
        print("Domain Lookup for : \n ")
        print(banner)
        for v in info:
            key, val = next(iter(info.items()))

            # printing result
            print(str(v) + " : " + str(info[v]) + "\n")
   
    except Exception as e:
        print(e)

if __name__ == "__main__":
    info_in()
    lookup(domain_name)


