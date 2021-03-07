import random


cardvalue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

card = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suite = ["S", "C", "H", "D"]

winner = ["Tie", "Dealer", "Player"]

dlrcard = []
dlrsuite = []
playercard = []
playersuite = []

def getcardval():
    # returns 2 ints card 0-12 and suite 0-3
    newcard = random.randint(0, 12)
    return newcard

def getsuiteval():
    # return 0 to 3 for suite
    newsuite = random.randint(0, 3)
    return newsuite

def dealinit():
    global dlrcard, dlrsuite
    # this will deal initial 2 cards to dealer and player or to dealer or player
    # input who gets deal init, dealer or player

    dlrcard.append(getcardval())
    dlrcard.append(getcardval())
    dlrsuite.append(getsuiteval())
    dlrsuite.append(getsuiteval())

    playercard.append(getcardval())
    playercard.append(getcardval())
    playersuite.append(getsuiteval())
    playersuite.append(getsuiteval())
    #score = cardvalue[dlrcard[0]] + cardvalue[dlrcard[1]]

def deal(who):
    if who == 0:
        #dealer
        dlrcard.append(getcardval())
        dlrsuite.append(getsuiteval())
    else:
        #player
        playercard.append(getcardval())
        playersuite.append(getsuiteval())


def printscreen(new):
    
    #print("dealer card = ", dlrcard)
    #print("dealer suite = ", dlrsuite)
    #print("player card = ", playercard)
    #print("player suite = ", playersuite)
    print("")
    print("")

    y = 0
    score = 0
    dlrprint = ""
    playerprint = ""

    if new == 1:
        dlrprint = dlrprint + " " + card[dlrcard[0]]
        dlrprint = dlrprint + " " + "X"
        print ("         ",dlrprint)
    else:
        for x in dlrcard:
            dlrprint = dlrprint + " " + card[dlrcard[y]]
            y += 1
        print ("         ",dlrprint)
        score = getscore(0)
        print("          ", score)
    print("-----------------------------")

    y = 0
    score = 0
    for x in playercard:
        playerprint = playerprint + " " + card[playercard[y]]
        y += 1
    print ("         ",playerprint)
    score = getscore(1)
    print("          ", score)


def getscore(who):

    y = 0
    aceflag = False
    score = 0
    if who == 1:
        for x in playercard:
            score = score + cardvalue[playercard[y]]
            if cardvalue[playercard[y]] == 1:
                aceflag = True
            y += 1

            if aceflag and score <= 11:
                score += 10
    else:
        for x in dlrcard:
            score = score + cardvalue[dlrcard[y]]
            if cardvalue[dlrcard[y]] == 1:
                aceflag = True
            y += 1

        if aceflag and score <= 11:
            score += 10

    return score

def playermove():
    score = getscore(1)
    print("your score is ", score, "Do you want to hit or stay?")
    y = input()

    return y

def whowon():
    dlrscore = getscore(0)
    playerscore = getscore(1)
    
    if dlrscore == playerscore:
        return 0
        
    if dlrscore > playerscore:
        return 1
    else:
        return 2

scoretie = 0
scoredlr = 0
scoreplayer = 0
win = 0
while 1:
    score = 0
    busted = 0
    dealinit()

    printscreen(1)
    while playermove() == "h":
        deal(1)
        printscreen(1)
        if getscore(1) > 21:
            printscreen(0)
            print("You busted")
            busted = 1
            scoredlr += 1
            
            #print ("score Ties", scoretie, "dealer", scoredlr, "player", scoreplayer)
            break
    if busted == 0:
        while getscore(0) < 17:
           deal(0)

        if getscore(0) > 21:
            printscreen(0)
            print("Dealer busted")
            busted = 1
            scoreplayer += 1

        if busted == 0:
            printscreen(0)
 
            win = whowon()
            print("winner is", winner[win])

            if win == 0:
                # Tie
                scoretie += 1
            elif win == 1:
                scoredlr += 1
            else:
                scoreplayer += 1
    print ("score Ties", scoretie, "dealer", scoredlr, "player", scoreplayer)
    del dlrcard[0:len(dlrsuite)]
    del dlrsuite[0:len(dlrsuite)]
    del playercard[0:len(playercard)]
    del playersuite[0:len(playersuite)]

    y = input()