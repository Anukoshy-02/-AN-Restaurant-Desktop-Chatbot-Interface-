ame=input("Enter the name:")
name1=name.upper()
phone=int(input("Enter the phone number:"))
custdetails=(name1,phone)

menu={
    "burger":100,
    "sandwich":80,
    "pineapple juice":100,
   "apple juice":200
    
    }
print("-------Menu----------")
for item in menu:
    print(item,"-",menu[item])
print("\n------------------\n")
item1=input("Enter the first item from the menu :")
item1=item1.lower()
quantity1=int(input("Enter the quantity:"))
item2=input("Enter the second item from the menu :")
item2=item2.lower()
quantity2=int(input("Enter the quantity:"))
print("\n")

print("Customer",custdetails)
print("------------------")
priceit1=menu[item1]*quantity1
price1=print(item1,"*",quantity1,"=",priceit1)
priceit2=menu[item2]*quantity2

price2=print(item2,"*",quantity2,"=",priceit2)

print("Total Price:",priceit1 + priceit2)