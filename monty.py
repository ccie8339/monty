import random
# Randomly pick 2 losers and 1 winning card
initialCards = ["L","W","L"]

wins = 0
losses = 0
numGames = 10000
requestedNumGames = ""
while not requestedNumGames.isdecimal():
    requestedNumGames = input(F"Number of games to play? [{numGames}]: ")
    if requestedNumGames == "":
        requestedNumGames = str(numGames)
    if requestedNumGames.isdecimal():
        numGames = int(requestedNumGames)
if isinstance(requestedNumGames, int):
    numGames = requestedNumGames
print(F"Playing {numGames} games.")
for y in range(0,numGames):
    tempDeck = initialCards.copy()
    currentDeck = []
    for x in range(0,3):
        cardNum = random.randint(0, len(tempDeck) - 1)
        currentDeck.append(tempDeck[cardNum])
        del tempDeck[cardNum]
    pickedCard = currentDeck[random.randint(0,2)]
    # This is cheap honestly, the host would always open a losing door, meaning
    # The 2 doors remain are 1 winner and 1 loser. Since you always switch
    # If you picked the winner originally, you will not lose, and vice versa.
    if pickedCard == "W":
        losses += 1
    else:
        wins += 1
print(F"{wins} wins out of {wins + losses} games. {wins / (wins + losses) * 100:.2f}%")
