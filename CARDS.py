import random
class Card(object):
    def __init__(self,suits,vals):
        self.suits=suits
        self.value=vals
    def show(self):
        print("{} of {}".format(self.value,self.suits) )

class Deck(object):
    def __init__(self):
        self.cards=[]
        self.build()
    def build(self):
         for s in ["spades".upper(),"clubs".upper(),"diamonds".upper(),"hearts".upper()]:
             for v in range(1,14):
                 self.cards.append(Card(s,v))
                 # print("{} of {}".format(v,s))
                  # print(v)
    def shows(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r=random.randint(0,i)
            self.cards[i],self.cards[r]=self.cards[r],self.cards[i]
            # print(i)
    def draw_card(self):
        return self.cards.pop()

class Player(object):
    def __init__(self,name):
        self.name=name
        self.hand=[]
    def draw(self,Deck):
        self.hand.append(Deck.draw_card())
        return self

    def showHand(self):
        for c in self.hand:
            c.show()

    def discard(self):
        return self.hand.pop()


# card=Card("spade".upper(),5)
# print(card.show())

d=Deck()
# print(d.build())
# print(d.shows())

print(d.shuffle())
# print(d.build())
print(d.shows())

# car=d.draw()
# print(car.show())

# bob=Player("Bob")  ######   3
# print(bob.draw(d).draw(d)) #### 4
# print(bob.showHand()) ##### 5
# bob.draw(d).draw(d)   #####    JOL JAAL    ####










