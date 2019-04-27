import os
import requests
import dotenv

dotenv.load_dotenv()

API_TOKEN = os.getenv("TOKEN")
if API_TOKEN in [None, "your api token here", ""]:
    print("The script is missing the API Token.")
    quit()
API = "https://accgen.cathook.club/api/v1/account/" + API_TOKEN

def GetAccount():
    r = requests.get(API)
    return r.json()

amount = None
while not amount:
    try:
        amount = int(input("How many Accounts to you want? "))
    except ValueError:
        print("Needs to be a number...")
        continue
    except KeyboardInterrupt:
        quit()

acc_txt = open('accounts.txt', 'a')
print("\nGetting Accounts . . .\n")
acc_txt.write("\n")
for _ in range(amount):
    acc = requests.get(API).json()
    #acc = GetAccount()
    try:
        print("{}:{}".format(acc['login'], acc['login']))
        acc_txt.write("{}:{}\n".format(acc['login'], acc['password']))
    except KeyError:
        print("\n" + acc['error'])
        quit()

acc_txt.close()
print("\nAccounts have been appended to the accounts.txt")