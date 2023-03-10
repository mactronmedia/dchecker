import whois # pip install python-
import colorama
from colorama import Fore
from termcolor import colored, cprint
import time 

start_time = time.time()

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
cyan = Fore.CYAN
reset  = Fore.RESET

print(colored("Bulk Domain Checker", "cyan", attrs=["reverse", "bold"]))
print(cyan+" ___                 _         ___ _           _")          
print("|   \ ___ _ __  __ _(_)_ _    / __| |_  ___ __| |_____ _ _ ") 
print("| |) / _ \ '  \/ _` | | ' \  | (__| ' \/ -_) _| / / -_) '_|") 
print("|___/\___/_|_|_\__,_|_|_||_|  \___|_||_\___\__|_\_\___|_|  ") 
print(reset)
                                                            
print(colored("Howdy, Mactron! Welcome to bulk domain checker!", "red", attrs=["reverse", "bold"]) + "\n")

domain = (input("Input Target Niche: "))
tld = input("Input TLD: ")

print("\t")

# Open & Read List With Suffix - Words From .txt File
with open("suffix.txt", "r") as domains:
    suffix_kws = domains.readlines()

#print(suffix_kws)    

suffix = []

for suffix_kw in suffix_kws:
    suffix.append(suffix_kw.replace("\n", ""))

#print(suffix)

#for word in suffix:
#  print(domain + word + "." + tld)

# Write Results in .txt File
with open("results.txt", "w") as results:
    for word in suffix:
        results.write(word + domain + "." + tld + "\n")
        results.write(domain + word + "." + tld)
        results.write('\n')

#print("Checking Database...")

with open("results.txt", "r") as urls:
    url_list = urls.readlines()

domains = []

for url in url_list:
    domains.append(url.replace("\n", ""))
    
domains_num = (len(domains))

print("Found", domains_num, "domain names") 

#WHOIS CHECKER

def is_registered(domain_name):
    """
    A function that returns a boolean indicating 
    whether a `domain_name` is registered
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)


if __name__ == "__main__":
    # list of registered & non registered domains to test our function
    #domains = []

    # iterate over domains

    reg = red + "is registred" + reset
    not_reg = green + "is not registred" + reset
   
    for domain in domains:
        time.sleep(0)
        if is_registered(domain) == True:
            print("+", domain, reg)
        else:
            print("+", domain, not_reg)
            with open("domains.txt", "a") as results:
                results.write(domain)
                results.write('\n')

time.sleep(2)
print("\n" + "Finishing the process!")

time.sleep(2)
print("\n" + "All available domains have been saved to txt file!")

time.sleep(2)
print ("\n"+ Fore.GREEN+"Domains generated in {0} seconds!".format(time.time() - start_time)+Fore.RESET)

time.sleep(4)
print("\n" + "Cya!" + "\n")        
