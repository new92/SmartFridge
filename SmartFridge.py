#Imports
import CheckFridge
import time

#Main Program
num = 1
i = 1
SmartFridge=[]
available = CheckFridge.check(SmartFridge)
print("[+] To end the fill of the fridge please type: stop")
while num > 0 or i > 0:
    FLen = len(SmartFridge)
    product=input("[::] Please enter the name of the product to add to the fridge: ")
    SmartFridge.append(product)
    if product == "stop":
        num = 0 
        i = 0
        print("[!] The fill of the fridge ended !")
    if i == 1 and product != "stop":
        print("[+] Filling will continue !")
        i += 1
print("[+] Number of products in the fridge: "+str(FLen))
time.sleep(2)
space=input("[+] Do you want to check the missing products ? [Y/N] ")
while space != "Y" and space != "y" and space != "N" and space != "n" or space == None:
    print("[!] Invalid option !")
    time.sleep(1)
    space=input("[::] Please enter again[Y/N]: ")
if space == "Y":
    print(available)
else:
    print("[+] Exiting...")
    exit(0)
