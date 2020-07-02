import random


class card():
    def __init__(self):
        self.num = random.randint(2, 14)
        if self.num == 12 or self.num == 13 or self.num == 14:
            self.num = 10

    def getnum(self):
        return(self.num)
    
    def __str__(self):
        return(str(self.num))

def game():
    play = "j"
    sum_ = 0
    dsum = 0
    while play == "j":
        while sum_ < 21 and dsum < 21:
            card1 = card()
            card2 = card()
            sum_ = card1.getnum() + card2.getnum()
            print("Your cards are:", card1, "and", card2)
            d_card1 = card()
            d_card2 = card()
            dsum = d_card1.getnum() + d_card2.getnum()
            if dsum > 17:
                d_card3 = card()
                dsum += d_card3.getnum()
            if dsum > 17:
                d_card4 = card()
                dsum += d_card4.getnum()
            if dsum > 17:
                d_card4 = card()
                dsum += d_card4.getnum()
            if dsum > 17:
                d_card5 = card()
                dsum += d_card5.getnum()
            if dsum > 17:
                d_card6 = card()
                dsum += d_card6.getnum()
            hit = input("hit? J/N ").lower
            if hit == "j":
                card3 = card()
                sum_ += card3.getnum()
                print("Your cards are:", card1, card2, "and", card3)
            hit = input("hit? J/N ").lower
            if hit == "j":
                card4 = card()
                sum_ += card4.getnum()
                print("Your cards are:", card1, card2, card3, "and", card4)
            hit = input("hit? J/N ").lower
            if hit == "j":
                card5 = card()
                sum_ += card5.getnum()
                print("Your cards are:", card1, card2, card3, card4, "and", card5)



a = card()
print(a)
