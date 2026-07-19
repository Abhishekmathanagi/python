import random 



cards=[]

suits =["Hearts","clubs","spades","diamond"]
ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
suit=suits[2]
rank ="K"
value=10
print("your card is:"+rank+"of"+suit)
suits.append("snakes")
for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])
        
        
def shuffle():
    random.shuffle(cards)   
    
    
    
def deal(number):
    card_dealt=[]
    for x in range(number):
        card=cards.pop()        
        card_dealt.append(card)
    return card_dealt

    
    
shuffle()

cards_dealt=deal(2)
card=cards_dealt[0]
rank=card[1]

if rank=="A":
    value=11
elif rank=="J" or rank=="Q" or rank=="K":
    value=10
else:
    value=rank
    
print(rank,value)


print(card)

