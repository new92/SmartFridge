#This part of code will check and return (if there is) the number of missing products

def check(Fridge):
    d = 1
    MissingProd = []
    FLen = len(Fridge)
    for i in range(FLen):
        prod = Fridge[i]
        if prod not in Fridge:
            MissingProd.append(prod)
    if len(MissingProd) == 0 and d >= 1:
        print("[!] 0 Missing products !")
