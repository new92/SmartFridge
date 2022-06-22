#Imports
import CheckFridge
import time
#End of Imports

#Main Program
#This part of code will 
num = 1
i = 1
SmartFridge=[]
available = CheckFridge.check(SmartFridge)
print("To end the fill of the fridge please type: stop")
while num > 0 or i > 0:
    FLen = len(SmartFridge)
    product=input("Please type the name of the product you want to add to your fridge: ")
    SmartFridge.append(product)
    if product == "stop":
        num = 0 
        i = 0
        print("The fill of the fridge ended !")
    if i == 1 and product != "stop":
        print("Filling will continue !")
        i += 1
print("Number of products in the fridge: "+str(FLen))
time.sleep(2)
space=input("Do you want to check the missing products ?[Y/N] ")
while space != "Y" and space != "N":
    print("Invalid option !")
    time.sleep(1)
    space=input("Please enter again[Y/N]: ")
if space == "Y":
    print(available)
else:
    print("Exiting...")
    time.sleep(1)
    exit(0)
#End of the Program