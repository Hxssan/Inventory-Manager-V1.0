#---------------------------------------------------------------------------------------------------
with open("IMAssetTV.txt", "r") as file:
    AssetVal = int(file.readline().strip())

def MainMenu():
    print("")
    print("=====================")
    print("  Inventory Manager  ")
    print("=====================")
    print("")
    print("(1) - Inventory Total")
    print("(2) - Bank Accounts")
    print("(3) - Stock Value")
    print("(4) - Asset Value")
    print("")
    Page = int(input("Select A Page:"))
    menuSelection(Page)
#---------------------------------------------------------------------------------------------------
with open("IMAssetTV.txt", "r") as file:
    AssetVal = int(file.readline().strip())
with open("IMStockTV.txt", "r") as file:
    StockVal = int(file.readline().strip())
with open("IMStockPP.txt", "r") as file:
    StockPrice = int(file.readline().strip())
with open("Company1.txt", "r") as file:
    c1bal = float(file.readline().strip())
with open("Company2.txt", "r") as file:
    c2bal = float(file.readline().strip())

accbal = c1bal + c2bal
StockProf = StockVal - StockPrice
totalval = AssetVal + StockProf + accbal
def PageIT():
    print("=====================")
    print("   Inventory Total   ")
    print("=====================")
    print("")
    print("Total Inventory Value Is : £"+str(totalval))
    print("")
    print("Inventory Value From Cash Is : £"+str(accbal))
    print("Inventory Value From Stock Value  : £"+str(StockProf))
    print("Inventory Value From Asset Worth Is : £"+str(AssetVal))
    print("")
    percentage1 = round((accbal/totalval) * 100, 1)
    percentage2 = round((StockProf/totalval) * 100, 1)
    percentage3 = round((AssetVal/totalval) * 100, 1)
    print(str(percentage1)+"% Of Inventory Value From Cash Is")
    print(str(percentage2)+"% Of Inventory Value From Stock Value")
    print(str(percentage3)+"% Of Inventory Value From Asset Worth")
    print("")
    print("Top 3 Largest Individual Holdings Are :")
    print("")
    print("(1) - ")
    print("(2) - ")
    print("(3) - ")
    print("")
    PageReturn = input("Would you like to return to the menu y/n:")
    PRSelection(PageReturn)
    
    
#---------------------------------------------------------------------------------------------------
def PageBA():
    print("=====================")
    print("     Bank Accounts   ")
    print("=====================")
    print("")
    print("(1)Company Account 1")
    print("Current Value = £"+str(c1bal))
    print("")
    print("(2)Company Account 2")
    print("Current Value = £"+str(c2bal))
    print("")
    BAPage = int(input("Select An Account To Modify (Or 0 To Go Back To Menu)"))
    BASelection(BAPage)

def BA1():
    print("=====================")
    print("  Company Account 1  ")
    print("=====================")
    print("")
    bpbav = input("What Is The Current Balance: £")
    print("Sucessfully Updated Value To: £"+str(bpbav))
    with open("Company1.txt", "w") as file:
        file.write(bpbav)
    PageReturn = input("Would you like to return to the menu y/n:")
    PRSelection(PageReturn)

def BA2():
    print("=====================")
    print("  Company Account 2  ")
    print("=====================")
    print("")
    
    rpbav = input("What Is The Current Balance: £")
    print("Sucessfully Updated Value To: £"+str(rpbav))
    with open("Company2.txt", "w") as file:
        file.write(rpbav)
    PageReturn = input("Would you like to return to the menu y/n:")
    PRSelection(PageReturn)
#--------------------------------------------------------------------------------------
with open('IMStock.txt', 'r') as file:
    lines = file.readlines()
    tav = 0
    for index, line in enumerate(lines):
        values = line.strip().split(",")
        name = values[0]
        value = int(values[1])
        quantity = int(values[2])
        asset_value = value * quantity
        tav += asset_value

    newtv = str(tav)
    with open("IMStockTV.txt", "w") as file:
        file.write(newtv)

def PageSV():
    print("")
    print("=====================")
    print("     Stock Value     ")
    print("=====================")
    print("(1) - View Stock")
    print("(2) - Add Stock")
    print("(3) - Edit Stock")
    print("(4) - Delete Stock")
    print("")
    print("Total Value Of Stock Is :"+str(StockProf))
    print("Total Items In Stock Is :"+str())
    print("Average Value Of Stock Is :"+str())
    print("")
    SVPage = int(input("Select A Page:"))
    SVSelection(SVPage)

    

class PAsset:
    def __init__(self, name, value, quantity):
        self.name = name
        self.value = value
        self.quantity = quantity

    def __str__(self):
        return f"{self.quantity} {self.name}'s: Currently Worth £{self.value} Each"

assets = []

def PageVS():
    print("=====================")
    print("      View Stock     ")
    print("=====================")
    print("")
    with open("IMStock.txt", "r") as file:
        for line in file:
            values = line.strip().split(",")
            name = values[0]
            value = int(values[1])
            quantity = int(values[2])
            asset = PAsset(name, value, quantity)
            assets.append(asset)
            print(asset)
    
    PageReturn = input("Would you like to return to the menu y/n:")
    PRSelection(PageReturn)

def PageAS():

    newassets = []

    print("=====================")
    print("       Add Stock     ")
    print("=====================")
    print("")
    while True:
        name = input("Enter Asset Name (or 'q' to quit): ")
        if name == 'q':
            break
        value = int(input("Enter Asset Value: "))
        quantity = int(input("Enter Asset Quantity: "))
        asset = PAsset(name, value, quantity)
        newassets.append(asset)

    with open("IMStock.txt", "a") as file:
        for asset in newassets:
            file.write(f"{asset.name},{asset.value},{asset.quantity}\n")

    PageReturn = input("Would you like to return to the menu y/n:")
    PRSelection(PageReturn)

def PageES():
    print("=====================")
    print("      Edit Stock     ")
    print("=====================")
    print("")

    with open('IMStock.txt', 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            values = line.strip().split(",")
            name = values[0]
            value = int(values[1])
            quantity = int(values[2])
            print(f"{index}: {name}, {value}, {quantity}")

    editnum = int(input("What is the number of the asset you would like to edit? "))

    with open('IMStock.txt', 'r') as file:
        lines = file.readlines()
        values = lines[editnum].strip().split(",")
        name = values[0]
        value = int(values[1])
        quantity = int(values[2])
        print(f"Enter New Values For: {name}")

    new_value = int(input("Enter New Asset Value: "))
    new_quantity = int(input("Enter New Asset Quantity: "))

    values[1] = str(new_value)
    values[2] = str(new_quantity)
    lines[editnum] = ",".join(values) + "\n"

    with open("IMStock.txt", "w") as file:
        file.writelines(lines)

    PageReturn = input("Would you like to return to the menu y/n:")
    PRSelection(PageReturn)

def PageDS():
    print("=====================")
    print("     Delete Stock    ")
    print("=====================")
    print("")
    with open('IMStock.txt', 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            values = line.strip().split(",")
            name = values[0]
            value = int(values[1])
            quantity = int(values[2])
            print(f"{index}: {name}, {value}, {quantity}")

    delnum = int(input("What is the number of the asset you would like to delete? "))
    with open('IMStock.txt', 'r') as file:
        lines = file.readlines()
        temp_lines = []
        for index, line in enumerate(lines):
            if index != delnum:
                temp_lines.append(line)
        with open('IMStock.txt', 'w') as file:
            file.writelines(temp_lines)
        

    
#---------------------------------------------------------------------------------------------------
def PageAV():
    print("=====================")
    print("     Asset Value     ")
    print("=====================")
    print("")
    print("Total Value Of Assets Is :")
    print("")
    print("(1) - View Assets")
    print("(2) - Add Assets")
    print("(3) - Edit Assets")
    print("(4) - Delete Assets")
    AVPage = int(input("Select A Page:"))
    AVSelection(AVPage)


def PageVA():
    print("=====================")
    print("     View Assets     ")
    print("=====================")
    print("")

def PageAA():
    print("=====================")
    print("     Add Assets      ")
    print("=====================")
    print("")

def PageEA():
    print("=====================")
    print("     Edit Assets     ")
    print("=====================")
    print("")

def PageDA():
    print("=====================")
    print("    Delete Assets    ")
    print("=====================")
    print("")

#---------------------------------------------------------------------------------------------------

def menuSelection(Page):
    if Page == 1:
        PageIT()
    elif Page == 2:
        PageBA()
    elif Page == 3:
        PageSV()
    elif Page == 4:
        PageAV()

def BASelection(PBAPage):
    if PBAPage == 1:
        BA1()
    elif PBAPage == 2:
        BA2()
    if PBAPage == 0:
        MainMenu()

def SVSelection(SVPage):
    if SVPage == 1:
        PageVS()
    elif SVPage == 2:
        PageAS()
    elif SVPage == 3:
        PageES()
    elif SVPage == 4:
        PageDS()

def AVSelection(AVPage):
    if AVPage == 1:
        PageVA()
    elif AVPage == 2:
        PageAA()
    elif AVPage == 3:
        PageEA()
    elif AVPage == 4:
        PageDA()


def PRSelection(PageReturn):
    if PageReturn.lower() == "y":
        MainMenu()
    elif PageReturn.lower() == "n":
        exit()


MainMenu()



