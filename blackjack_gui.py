from tkinter import *
from tkinter.messagebox import showinfo, askyesno
from PIL import ImageTk, Image
import random
import time
import inspect
import sys

class Cards:
    canv_ids = []

    j = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    win = 0
    loose = 0 
    draw = 0
    blackjack = 0
    my_score_id = 0
    my_tally_id = 0
    dlr_score_id = 0

    def __init__(self):

        self.score = 0
        self.times = 0
        self.ace_flag = False
        self.ace_used = False
        self.hidden = 0    
        self.position = 0
        self.txt_posit = 0

    def getcardval(self):
        newcard = random.randint(0, 12)
        return newcard

    def getsuiteval(self):
        newsuite = random.randint(0, 3)
        return newsuite

    def getscore(self, value):

        cardvalue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.score += cardvalue[value]

        if cardvalue[value] == 1:
            self.ace_flag = True

        if self.ace_flag and self.score <= 11:
            cardvalue[value] = 10
            self.score += cardvalue[value]
            self.ace_used = True

        elif self.ace_used and self.score > 21:
            self.score -= 10
            self.ace_used = False

        return self.score

    def pickcard(self, ace=False):
        card = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suite = ["S", "C", "H", "D"]

        spin = self.getcardval()
        if ace:
            spin = 0
            
        self.getscore(spin)
        spin2 = self.getsuiteval()
        card_val = card[spin]
        suite_val = suite[spin2]
        
        return card_val + suite_val

    def check21(self):
        
        if self.score == 21:
            my_canvas.delete(dealer.hidden)

            my_canvas.delete(Cards.dlr_score_id)
            txt = "score: " + str(dealer.score)
            Cards.dlr_score_id = my_canvas.create_text(200, 105, text=txt)
            
            #gets the caller name
            caller_frame = sys._getframe(1)
            caller_name = inspect.getframeinfo(caller_frame)[3]
            caller_name = caller_name[0].strip().split('.')

            #player.myClick()
            #player.myClick()

            again = askyesno("canvas", caller_name[0] + " got 21 want to play again?")
            if caller_name[0] == "player":
                Cards.win += 1
                Cards.blackjack += 1
            else:
                Cards.loose += 1
            
            if again:
                dealer.clear_cards()
                player.reset()
                dealer.reset()
                dealer.start()
            else:
                root.quit()
        else:
            return 0

    def check_score(self):
        if self.score > 21:

            again = askyesno("canvas", "YOU BUSTED want to play again?")
            Cards.loose += 1
            if again:
                dealer.clear_cards()
                player.reset()
                dealer.reset()
                dealer.start()
            else:
                root.quit()
        
    def clear_cards(self):
        for ids in Cards.canv_ids:
            my_canvas.delete(ids)
        Cards.canv_ids = []
        
    def reset(self):
        self.times = 0
        self.score = 0
        self.ace_flag = False
        self.ace_used = False

    def start(self, hide=False):
        #print("------------------------------")
        player.myClick()
        dealer.youClick()
        player.myClick()
        dealer.youClick(hide=True, ace=False)
        player.check21()
        dealer.check21()

        
    def youClick(self, hide=False, ace=False):

        card = self.pickcard(ace=ace)

        self.times += 1
        # resizing image using an array to show all  cards 
        img = "extra\\" + card + ".png"
        Cards.j[self.times] = Image.open(img)
        resized = Cards.j[self.times].resize((60, 75), Image.ANTIALIAS)
        Cards.y[self.times] = ImageTk.PhotoImage(resized)
        horr = 80 + (self.times * 20)
        my_image = my_canvas.create_image(horr, 10, anchor=NW,
                                          image=Cards.y[self.times])
        Cards.canv_ids.append(my_image)

        if hide:

            img = "extra\\purple_back.png"
            Cards.k[self.times] = Image.open(img)
            resized = Cards.k[self.times].resize((60, 75), Image.ANTIALIAS)
            Cards.z[self.times] = ImageTk.PhotoImage(resized)
            horr = 80 + (self.times * 20)
            my_image = my_canvas.create_image(horr, 10, anchor=NW,
                                              image=Cards.z[self.times])
            self.hidden = my_image
        else:
            my_canvas.delete(Cards.dlr_score_id)
            txt = "score: " + str(self.score)
            Cards.dlr_score_id = my_canvas.create_text(150, 95, text=txt)

    def myClick(self, ace=False):
        
        #gets the caller name
        caller_frame = sys._getframe(2)
        caller_name = inspect.getframeinfo(caller_frame)[3]
        caller_name = caller_name[0].strip().split('.')
        #print("myClick - ", caller_frame)
        
        
        card = self.pickcard(ace=ace)
        self.times += 1

        # resizing image using an array to show all  cards 
        img = "extra\\" + card + ".png"
        Cards.i[self.times] = Image.open(img)
        resized = Cards.i[self.times].resize((60, 75), Image.ANTIALIAS)
        Cards.x[self.times] = ImageTk.PhotoImage(resized)
        horr = 80 + (self.times * 20)
        my_image = my_canvas.create_image(horr, 200, anchor=NW, image=Cards.x[self.times])
        Cards.canv_ids.append(my_image)

        # delete previous text then print the new score
        my_canvas.delete(Cards.my_score_id)
        txt = "score: " + str(self.score)
        Cards.my_score_id = my_canvas.create_text(150, 285, text=txt)
        
        my_canvas.delete(Cards.my_tally_id)
        txt = "  Win: " + str(Cards.win)+ \
              "  Loose: "+ str(Cards.loose)+ \
              "  Draw: "+  str(Cards.draw)+ \
              "  Blackjack: "+  str(Cards.blackjack)
        Cards.my_tally_id = my_canvas.create_text(150, 145, text=txt)
        
        self.check_score()

    def stay(self):

        caller_frame = sys._getframe(2)
        caller_name = inspect.getframeinfo(caller_frame)[3]
        caller_name = caller_name[0].strip().split('.')
        #print("in stay - ", caller_frame)

        my_canvas.delete(dealer.hidden)
        my_canvas.delete(Cards.dlr_score_id)
        txt = "score: " + str(dealer.score)
        Cards.dlr_score_id = my_canvas.create_text(150, 95, text=txt)

        while dealer.score <= 16:
            dealer.youClick()
        who = whowon()
        again = askyesno("canvas", who + " want to play again?")
        if again:
            dealer.clear_cards()
            player.reset()
            dealer.reset()
            dealer.start()
            
        else:
            root.quit()

def whowon():
    
    if dealer.score > 21:
        Cards.win += 1
        return "You won! "
        
    elif dealer.score == player.score:
        Cards.draw += 1
        return "Game was a tie."
        
    elif dealer.score > player.score:
        Cards.loose += 1
        return "Dealer won. "
        
    else:
        Cards.win += 1
        return "You won! "

def set_up():
    global dealer, player, my_canvas, root
    dealer = Cards()
    player = Cards()
    w = 300
    h = 300
    root = Tk()
    my_canvas = Canvas(root, width=w, height=h, bg="white")
    my_canvas.pack(pady=20)

    player.myClick()
    dealer.youClick()
    player.myClick()
    dealer.youClick(hide=True)
       
    mybutton = Button(root, text="hit me", command=player.myClick)
    mybutton.place(x=25, y=0)
    mybutton.pack()

    mybutton1 = Button(root, text="stay", command=player.stay)
    mybutton1.pack()

    player.check21()
    dealer.check21()

set_up()
root.mainloop()
