from tkinter import *
from tkinter.messagebox import showinfo, askyesno
from PIL import ImageTk, Image
import random
import inspect
import sys

class Cards:
    canv_ids = []
    
    #i = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    win = 0
    loose = 0 
    draw = 0
    blackjack = 0
    
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
        
        self.j = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.my_score_id = 0
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

            self.draw_score()

            #gets the caller name
            caller_frame = sys._getframe(1)
            caller_name = inspect.getframeinfo(caller_frame)[3]
            caller_name = caller_name[0].strip().split('.')

            #print("in bust", caller_frame)
            again = askyesno("canvas", caller_name[0] + " got 21 want to play again?")
            if caller_name[0] == "player":
                Cards.win += 1
                Cards.blackjack += 1
            else:
                Cards.loose += 1
            
            if again:
                self.my_restart()
            else:
                root.quit()
        else:
            return 0

    def my_restart(self):
        dealer.clear_cards()
        player.reset()
        dealer.reset()
        dealer.start()

    def check_bust(self):
        if self.score > 21:
            #gets the caller name
            caller_frame = sys._getframe(1)
            caller_name = inspect.getframeinfo(caller_frame)[3]
            caller_name = caller_name[0].strip().split('.')
            #txt.replace("bananas", "apples")
            caller_name = caller_name[0].replace("if not ", "")
            caller_name = caller_name.strip()
            #again = askyesno("canvas",caller_name[0] + " BUSTED want to play again?")
            again = askyesno("canvas", caller_name + " BUSTED want to play again?")

            x = caller_name.rfind("dealer")
            if caller_name.rfind("dealer") >= 0:
                Cards.win += 1
                print("win ->",caller_name+"<-")

            else:
                print("loose ->",caller_name+"<-")
                Cards.loose += 1
                
            #self.restart()
            if again:
                self.my_restart()
                return True
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
        player.my_click()
        dealer.my_click()
        player.my_click()
        dealer.my_click(hide=True, ace=False)
        player.check_bust()
        dealer.check_bust()
        player.check21()
        dealer.check21()

    def add_card(self, ace=False):

        player.crd = 200
        dealer.crd = 10

        card = self.pickcard(ace=ace)

        self.times += 1
        # resizing image using an array to show all  cards
        img = "extra\\" + card + ".png"
        self.j[self.times] = Image.open(img)
        resized = self.j[self.times].resize((60, 75), Image.ANTIALIAS)
        self.y[self.times] = ImageTk.PhotoImage(resized)
        horr = 80 + (self.times * 20)
        my_image = my_canvas.create_image(horr, self.crd, anchor=NW,
                                          image=self.y[self.times])
        Cards.canv_ids.append(my_image)


    def my_click(self, hide=False, ace=False):
        #print("============================================")
        caller_frame = sys._getframe(1)
        #print("in my_click - 1 ", caller_frame)
        
        self.add_card(ace=ace)

        if hide:

            img = "extra\\purple_back.png"
            self.k[self.times] = Image.open(img)
            resized = self.k[self.times].resize((60, 75), Image.ANTIALIAS)
            self.z[self.times] = ImageTk.PhotoImage(resized)
            horr = 80 + (self.times * 20)
            my_image = my_canvas.create_image(horr, self.crd, anchor=NW,
                                              image=self.z[self.times])
            self.hidden = my_image
        else:
            
            self.draw_score()

        self.draw_wld()

    def click(self):
        player.my_click()
        player.check_bust()

    def draw_score(self):

        player.scr = 285
        dealer.scr = 95
        
        # delete previous text then print the new score
        my_canvas.delete(self.my_score_id)
        txt = "score: " + str(self.score)
        self.my_score_id = my_canvas.create_text(150, self.scr, text=txt)

    def draw_wld(self):
        # draw win loose draw
        my_canvas.delete(Cards.my_tally_id)
        txt = "  Win: " + str(Cards.win) + \
              "  Loose: " + str(Cards.loose) + \
              "  Draw: " + str(Cards.draw) + \
              "  Blackjack: " + str(Cards.blackjack)
        Cards.my_tally_id = my_canvas.create_text(150, 145, text=txt)

    def dlr_stay(self):

        caller_frame = sys._getframe(2)
        caller_name = inspect.getframeinfo(caller_frame)[3]
        caller_name = caller_name[0].strip().split('.')
        
        #print("--------------------------------------")
        #print("in stay - ", caller_frame)
        #print("--------------------------------------")

        my_canvas.delete(dealer.hidden)
        dealer.draw_score()

        
        while dealer.score <= 16:
            dealer.my_click()

        if not dealer.check_bust():
            self.draw_score()
            who = whowon()
            again = askyesno("canvas", who + " want to play again?")
            if again:
                self.my_restart()
            else:
                root.quit()

def whowon():
    
    if dealer.score > 21:    #ojoiooo
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

    player.my_click()
    dealer.my_click()
    player.my_click()
    player.check_bust()
    #player.mymy_click()
    dealer.my_click(hide=True)
    dealer.check_bust()
       
    mybutton = Button(root, text="hit me", command=player.click)
    mybutton.place(x=25, y=0)
    mybutton.pack()

    mybutton1 = Button(root, text="stay", command=player.dlr_stay)
    mybutton1.pack()

    player.check21()
    dealer.check21()

set_up()
root.mainloop()
