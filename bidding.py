import os, logo

def clearscreen():
 os.system('cls')

def addBid(bidDict, name, bid):
    bidDict[name] = bid

bidDict = {}
loopCtrl = True

while loopCtrl:
    print(logo.logo)
    name = input("\nPlease enter your name: ")
    bid = input("Please enter your bid amount: ")
    addBid(bidDict, name, bid)

    resp = input("\n Do you want to enter another bid (y/n) : ")
    if resp.lower() == 'n':
       loopCtrl = False
    else:
        clearscreen()

highestBidder = ""
highestBid = 0.0

print(bidDict)

for k, v in bidDict.items():
  if float(v) > highestBid:
     highestBidder = k
     highestBid = float(v)     

print(f"Highest Bidder is {highestBidder}")

maxBidder = max(bidDict, key=bidDict.get)
minBidder = min(bidDict, key=bidDict.get)

print(f"Max Bidder is {maxBidder}")
print(f" Min bidder is {minBidder}")

print(type(logo.logo))

