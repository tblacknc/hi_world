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
    newcard = random.randint(0, 12)
    return newcard

def getsuiteval():
    newsuite = random.randint(0, 3)
    return newsuite

def dealinit():
    global dlrcard, dlrsuite

    dlrcard.append(getcardval())
    dlrcard.append(getcardval())
    #dlrcard.append(0)
    #dlrcard.append(10)
    dlrsuite.append(getsuiteval())
    dlrsuite.append(getsuiteval())
    #playercard.append(0)
    #playercard.append(10)
    playercard.append(getcardval())
    playercard.append(getcardval())
    
    playersuite.append(getsuiteval())
    playersuite.append(getsuiteval())

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

def check21():
    dlrscore = getscore(0)
    playerscore = getscore(1)
    if dlrscore == 21 and dlrscore == playerscore:
        return 3        
    elif dlrscore == 21:
        return 1
    elif playerscore == 21:
        return 2
    else:
        return 0

def listreset():
    del dlrcard[0:len(dlrsuite)]
    del dlrsuite[0:len(dlrsuite)]
    del playercard[0:len(playercard)]
    del playersuite[0:len(playersuite)]

scoretie = 0
scoredlr = 0
scoreplayer = 0
win = 0
playermove1 = "h"
while 1:
    twentyone = False
    score = 0
    busted = 0
    dealinit()
    STOP = False

    blackjack = check21()
    printscreen(1)
    if blackjack != 0:
        if blackjack == 1:
            printscreen(0)
            print("dealer has blackjack!")
            scoredlr += 1
            listreset()
            STOP = True
        elif blackjack == 2:
            printscreen(0)
            print("player has blackjack!")
            scoreplayer += 1
            listreset()
            STOP = True
        else:
            printscreen(0)
            print("both players have blackjack!")
            scoretie += 1
            listreset()
            STOP = True
    if not  STOP:    
        while playermove() == 'h':
            deal(1)
            printscreen(1)
            if getscore(1) > 21:
                printscreen(0)
                print("You busted")
                scoredlr += 1
                STOP = True
                break
                
    if not STOP:
        while getscore(0) < 17 and getscore(1) > getscore(0):
            deal(0)
            if getscore(0) > 21:
                printscreen(0)
                print("Dealer busted")
                busted = 1
                scoreplayer += 1
                STOP = True

            if busted == 0:
                printscreen(0)
                win = whowon()
                print("winner is", winner[win])
                STOP = True

    if not STOP:  
        if win == 0:
            # Tie
            scoretie += 1
            printscreen(0)
            print("winner is", winner[win])
        elif win == 1:
            scoredlr += 1
            printscreen(0)
            print("winner is", winner[win])
            
        else:
            scoreplayer += 1
            printscreen(0)
            print("winner is", winner[win])
    print ("score Ties", scoretie, "dealer", scoredlr, "player", scoreplayer)
    listreset()

    print("Play again?")
    y = input()
