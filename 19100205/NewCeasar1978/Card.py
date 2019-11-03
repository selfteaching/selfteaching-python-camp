import random
class Card:
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]
    def __init__(self,suit = 0,rank = 2):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return '%s of %s'%(self.rank_names[self.rank],self.suit_names[self.suit])
    def __eq__(self,other):
        t1 = self.suit,self.rank
        t2 = other.suit,other.rank
        return  t1 == t2
    def __lt__(self,other):
        t1 = self.suit,self.rank
        t2 = other.suit,other.rank
        return t1 < t2

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def add_card(self,card):
        self.cards.append(card)
    
    def remove_card(self,card):
        self.cards.remove(card)

    def pop_card(self,i=-1):
        return self.cards.pop(i)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self,hand,number):
        for i in range(number):
            hand.add_card(self.pop_card())

class Hand(Deck):
    def __init__(self,lable=''):
        self.cards = []
        self.lable = lable



'''
deck = Deck()
hand = Hand()
deck.shuffle()
deck.move_cards(hand,5)
hand.sort()
print(hand)
'''