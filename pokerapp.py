import math
import random

class Card:
    pass

class Poker:
    def __init__(self, num_players):
        if num_players > 9:
            raise Exception("Too Many Players. 9 is the maximum")
        suits = ['S', 'C', 'H', 'D']
        val = ['2', '3', '4','5','6','7','8','9','10','J', 'Q', 'K', 'A']
        self.cards = []
        self.num_players = num_players
        for suit in suits:
            for v in val:
                self.cards.append((v, suit))
        return 
    
    def Deal(self):
        self.total_cards = {i:{"suit":{}, "val":{}} for i in range(self.num_players)}
        self.avail_cards = self.cards
        random.shuffle(self.avail_cards)
        for j in range(2):
            for i in range(self.num_players):
                val, suit = self.avail_cards.pop()
                if suit not in self.total_cards[i]["suit"]:
                    self.total_cards[i]["suit"][suit] = set()
                self.total_cards[i]["suit"][suit].add(val)
                if val not in self.total_cards[i]["val"]:
                    self.total_cards[i]["val"][val] = set()
                self.total_cards[i]["val"][val].add(suit)
        self.my_cards = self.total_cards[0]
        return print(f'Cards Dealt. Your cards are {self.my_cards}')
    
    def Flop(self):
        self.community_cards = {"suit":{}, "val":{}}
        for i in range(3):
            self.AddCommunityCard()
        return print(f'The Flop is {self.community_cards}')
    
    def Turn(self):
        self.AddCommunityCard()
        return print(f'The Turn is {self.community_cards}')

    def River(self):
        self.AddCommunityCard()
        return print(f'The River is {self.community_cards}')    
    
    def AddCommunityCard(self):
        val, suit = self.avail_cards.pop()
        if suit not in self.community_cards["suit"]:
            self.community_cards["suit"][suit] = set()
        self.community_cards["suit"][suit].add(val)
        if val not in self.community_cards["val"]:
            self.community_cards["val"][val] = set()
        self.community_cards["val"][val].add(suit)
        return
    
    def BoardWetness(self):
        pass

    def CalculateHand(self, hand):
        pass
    def CheckForPair(self):
        pass
    def CheckForTwoPair(self):
        pass
    def CheckForThree(self):
        pass
    def CheckForStraight(self):
        pass
    def CheckForFlush(self):
        pass
    def CheckForHouse(self):
        pass
    def CheckForFour(self):
        pass
    def CheckForStraightFlush(self):
        pass
    def CheckForRoyal(self, hand):
        if self.CheckForStraightFlush(hand):
            pass



    def YourTurn(self):
        strength, outs = self.CalculateHand()
        
        

p = Poker(num_players=6)
p.Deal()
p.Flop()
p.Turn()
p.River()