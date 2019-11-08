
"""!--BLACKJACK--!"""
import random
import os
#top = tkinter.Tk()


class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = '♥♦♣♠'[suit-1] # 1,2,3,4 = ♥♦♣♠

    def print(self, bool):
        if bool == 0:
            print('┌───────┐')
            print(f'| {self.value:<2}    |')
            print('|       |')
            print(f'|   {self.suit}   |')
            print('|       |')
            print(f'|    {self.value:>2} |')
            print('└───────┘')

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, "A"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
special = ["J", "Q", "K"]
taken = []
i = 1
sum1 = 0
sum2 = 0
hit = 0
status = 0
nohit = 0
p1cards = []
p2cards = []
while(i!=0):
    i+=1
    if i % 2 == 0:
        print("Player1, Your score is ", str(sum1))
        print("Your Cards:")
        for a in p1cards:
            a.print(0)
    else:
        print("Player2, Your score is ", str(sum2))
        print("Your Cards:")
        for a in p2cards:
            a.print(0)
    print("Do you want to hit?[Yes/No]", end = " ")
    hit = input()
    if hit == "Yes":
        allow = True
        while(allow):
            x = random.choice(cards)
            y = random.choice(suits)
            if x == 10:
                z = random.choice(special)
            else:
                z = x
            s = str(z) + " of " + y
            if s not in taken:
                allow = False
                taken.append(s)
            card = Card(z, suits.index(y) + 1)
            if i % 2 == 0:
                p1cards.append(card)
            else:
                p2cards.append(card)
        print("You got ", s)
        card.print(0)
        if x != 'A':
            if i%2 == 0:
                sum1 += x
            else:
                sum2 += x
        else:
            print("What do you want to set as the value of A?", end = " ")
            player_choice = int(input())
            if i%2 == 0:
                sum1 += player_choice
            else:
                sum2 += player_choice
        if sum1 > 21:
            print("Busted")
            status = 2
            i = 0
        if sum2 > 21:
            print("Busted")
            status = 1
            i = 0
        if sum2 == 21:
            print("Blackjack!")
            status = 2
            i = 0
        if sum1 == 21 and sum2 == 21:
            status = 3
            i = 0
    else:
        nohit += 1
        if nohit == 3:
            i = 0
            if sum2 > sum1:
                status = 2
            elif sum1 > sum2:
                status = 1
            else:
                status = 3
    print("\n")
    print("Type C to continue...")
    if(input() == 'C'):
        os.system('cls')
