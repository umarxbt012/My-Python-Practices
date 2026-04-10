import os
def find_winner(bidder_details):
    highest_bid=0
    for bidder in bidder_details:
        bidder_price=bidder_details[bidder]
        if bidder_price>highest_bid:
            highest_bid=bidder_price
            winner=bidder
    print(f"{winner} is the winner with the price of {bidder_price}$!!")



bidder_data={}
print("welcome to my silent auction program".upper())
active = True
while active:
    name=input("enter the name of the bidder: ".title())
    price=int(input("enter the price: ".title()))
    #
    bidder_data[name]=price
    choice=input("do you wish to continue Y/N: ").lower()
    if choice=="n":
        not active
        find_winner(bidder_data)
        break
    else:
        os.system("cls")
    