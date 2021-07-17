import random, os, time, requests, datetime

def menu():
  print("""
 ██████╗ ███████╗ █████╗ ██████╗  █████╗ 
██╔═████╗╚══███╔╝██╔══██╗██╔══██╗██╔══██╗
██║██╔██║  ███╔╝ ███████║██████╔╝███████║
████╔╝██║ ███╔╝  ██╔══██║██╔══██╗██╔══██║
╚██████╔╝███████╗██║  ██║██║  ██║██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
Made by Ozara#1111
  """)

  print("""
  [1] Nitro Generator
  [2] Nitro Checker
  [3] Nitro Generator + Checker
  [4] Exit
  """)

  choice = int(input("[?]: "))
  valid = 0
  valid_codes = []
  invalid = 0

  if choice == 1:
    amt = int(input("[+] Enter how many codes you want to Generate: "))
    codeLen = 16
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123457890"
    k = open("NitroGenResults/Codes.txt", "w")
    for i in range(amt):
      print("[+] https://discord.gift/" + ''.join(random.choice(letters) for i in range(codeLen)))
      k.write("https://discord.gift/" + ''.join(random.choice(letters) for i in range(codeLen)) + "\n")
    k.close()
    print("[+] Codes saved to Codes.txt")
  elif choice == 2:
    with open("CodesToCheck.txt") as f:
      for line in f:
        s = requests.Session()
        nitro = line.strip("\n")
        start = datetime.datetime.now()


        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"


        r = s.get(url)

        if r.status_code == 200:
          print(f"[+] Valid | {nitro}".format(line.strip("\n")))
          valid_codes.append(nitro)
          valid += 1

          
          k = open("CheckerResults/Valids.txt", 'w')
          k.write(valid_codes)
        else:
          print(f"[-] Invalid | {nitro}".format(line.strip("\n")))
          invalid += 1
      print("\n")
      print(f"""
      Valids = {valid}
      Invalids = {invalid}
      Valid Codes: {', '.join(valid_codes)}
      """)
  elif choice == 3:
    amt = int(input("[+] Enter how many codes you want to Generate and Check: "))
    codeLen = 16
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123457890"
    g = open("AutopilotResults/AllCodes.txt", "w")
    u = open("AutopilotResults/Valids.txt", "w")
    n = open("AutopilotResults/Invalids.txt", "w")
    for i in range(amt):
      g.write("https://discord.gift/" + ''.join(random.choice(letters) for i in range(codeLen)) + "\n")
    g.close()

    with open("AutopilotResults/AllCodes.txt") as f:
      for line in f:
        invalid_codes = []
        valid_codes = []
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        s = requests.Session()

        r = s.get(url)

        if r.status_code == 200:
          print(f"[+] Valid | {nitro}".format(line.strip("\n")))

          valid_codes.append(nitro)
          break
        else:
          print(f"[-] Invalid | {nitro}".format(line.strip("\n")))

          invalid_codes.append(nitro)



  elif choice == 4:
    os.system('cls')
    print("[+] Quitting...") 
    time.sleep(5)
    exit(0)   
menu()