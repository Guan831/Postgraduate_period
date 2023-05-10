# Write a function that generates random blackjack cards
def blackjackcards():
    import random
    cards = ["Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    card = random.choice(cards)
    suit = random.choice(suits)
    print(card, "of", suit)
    return card, suit
# get datatime


def datatime():
    import datetime
    now = datetime.datetime.now()
    print("Current date and time: ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    return now


if __name__ == "__main__":
    # blackjackcards()
    datatime()
