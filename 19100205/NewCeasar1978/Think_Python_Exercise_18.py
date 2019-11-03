from Card import Hand, Deck
class Hist(dict):
    def __init__(self,seq=[]):
        for x in seq:
            self.count(x)

    def count(self,x,f=1):
        self[x] = self.get(x,0) + f
        if self[x] == 0:
            del self[x]

class PokerHand(Hand):
    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
                  'straight', 'threekind', 'twopair', 'pair', 'highcard']    
    def make_histograms(self):
        self.suits = Hist()
        self.ranks = Hist()
        for c in self.cards:
            self.suits.count(c.suit)
            self.ranks.count(c.rank)
        self.sets = list(self.ranks.values())
        self.sets.sort(reverse=True)

    def has_highcard(self):
        return len(self.cards)

    def check_sets(self,*t):
        for need,have in zip(t,self.sets):
            if need > have:
                return False
        return True

    def has_pair(self):
        return self.check_sets(2)

    def has_twopair(self):
        return self.check_sets(2,2)
    
    def has_threekind(self):
        return self.check_sets(3)

    def has_fourkind(self):
        return self.check_sets(4)

    def has_fullhouse(self):
        return self.check_sets(3,2)

    def has_flush(self):
        for value in self.suits.values():
            if value >= 5:
                return True
        return False

    def has_straight(self):
        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1,0)
        return self.in_a_row(ranks,5)
    
    def in_a_row(self,ranks,n=5):
        count = 0
        for i in range(1,15):
            if ranks.get(i,0):
                count += 1
                if count == n:
                    return True
            else:
                count = 0
        return False

    def has_straightflush(self):
        return self.has_straight() and self.has_flush()
    
    
    
    
    def classify(self):
        """Classifies this hand.

        Creates attributes:
          labels:
        """
        self.make_histograms()

        self.labels = []
        for label in PokerHand.all_labels:
            f = getattr(self, 'has_' + label)
            if f():
                self.labels.append(label)


class PokerDeck(Deck):
    """Represents a deck of cards that can deal poker hands."""

    def deal_hands(self, num_cards=5, num_hands=10):
        """Deals hands from the deck and returns Hands.

        num_cards: cards per hand
        num_hands: number of hands

        returns: list of Hands
        """
        hands = []
        for i in range(num_hands):        
            hand = PokerHand()
            self.move_cards(hand, num_cards)
            hand.classify()
            hands.append(hand)
        return hands


def main():
    # the label histogram: map from label to number of occurances
    lhist = Hist()

    # loop n times, dealing 7 hands per iteration, 7 cards each
    n = 10000
    for i in range(n):
        if i % 100 == 0:
            print(i/100,'%')
            
        deck = PokerDeck()
        deck.shuffle()

        hands = deck.deal_hands(5, 7)
        for hand in hands:
            for label in hand.labels:
                lhist.count(label)
            
    # print the results
    total = 7.0 * n
    print(total, 'hands dealt:')

    for label in PokerHand.all_labels:
        freq = lhist.get(label, 0)
        if freq == 0: 
            continue
        p = total / freq
        print('%s happens one time in %.2f' % (label, p))

        
if __name__ == '__main__':
    main()
