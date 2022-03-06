#!/usr/bin/ python3
# github.com/thenurhabib

# Import Modules
import sys
import time
from googlesearch import search


# Colors
class ColorsClass:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


# banner
banner = f"""

████████▄   ▄██████▄     ▄████████  ▄████████    ▄█   ▄█▄    ▄████████    ▄████████ 
███   ▀███ ███    ███   ███    ███ ███    ███   ███ ▄███▀   ███    ███   ███    ███ 
███    ███ ███    ███   ███    ███ ███    █▀    ███▐██▀     ███    █▀    ███    ███ 
███    ███ ███    ███  ▄███▄▄▄▄██▀ ███         ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███    ███ ███    ███ ▀▀███▀▀▀▀▀   ███        ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███    ███ ███    ███ ▀███████████ ███    █▄    ███▐██▄     ███    █▄  ▀███████████ 
███   ▄███ ███    ███   ███    ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███ 
████████▀   ▀██████▀    ███    ███ ████████▀    ███   ▀█▀   ██████████   ███    ███ 
                        ███    ███              ▀                        ███    ███ 
                                                        𝓐𝓭𝓿𝓪𝓷𝓬𝓮 𝓖𝓸𝓸𝓰𝓵𝓮 𝓓𝓸𝓻𝓴𝓲𝓷𝓰 𝓣𝓸𝓸𝓵."""


for col in banner:
    print(ColorsClass.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

authorInformation = f"""
-----------------------------------------------------------------------------------
|                    Author  :  Md. Nur habib                                     |
|                    Github  :  github.com/thenurhabib                            |
|                    Twitter :  twitter.com/thenurhab1b                           |
----------------------------------------------------------------------------------- """


for col in authorInformation:
    print(ColorsClass.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)


lineBreck = "\n"
for col in lineBreck:
    print(ColorsClass.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)

try:
    takePathFromUser = input(
        f"{ColorsClass.BOLD}\n[$] - Do You Like To Save The Output In A File? (Y/N) "
    ).strip()
    saveLogInformation = ""

except KeyboardInterrupt:
    print("\n")
    print("\033[1;91m[$]- User Interruption Detected..!\033[0")
    time.sleep(0.5)
    sys.exit(1)


def loggerFunction(takePathFromUser):
    try:
        file = open((saveLogInformation) + ".txt", "a")
        file.write(str(takePathFromUser))
        file.write("\n")
        file.close()

        if takePathFromUser.startswith("y" or "Y"):
            saveLogInformation = input("[$] - Enter File Name: ")
            print("\n" + "  " + "»" * 78 + "\n")
            loggerFunction(takePathFromUser)
        else:
            print("[$]- Saving is Skipped...")
            print("\n" + "  " + "»" * 78 + "\n")
    except Exception:
        pass


def dorcksFunction():
    try:
        getDorkFromUser = input("\n[$] - Enter The Dork Search Query : ")
        getAmountFromUser = input("[$] - Enter The Number Of Websites To Display : ")
        print("\n ")
        requestVar = 0
        counterVar = 0

        for results in search(
            getDorkFromUser,
            tld="com",
            lang="en",
            num=int(getAmountFromUser),
            start=0,
            stop=None,
            pause=2,
        ):
            counterVar = counterVar + 1
            print("[$] - ", counterVar, results)
            time.sleep(0.1)
            requestVar = requestVar + 1
            if requestVar >= int(getAmountFromUser):
                break

            takePathFromUser = (counterVar, results)
            loggerFunction(takePathFromUser)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n")
        print("\033[1;91m[$]- User Interruption Detected. Exiting...\033[0")
        time.sleep(0.5)
        sys.exit(1)

    sys.exit()


if __name__ == "__main__":
    dorcksFunction()
