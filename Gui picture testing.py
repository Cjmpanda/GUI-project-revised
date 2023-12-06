'''

CS1010-11 Group 3 GUI Project
'Blackjack Casino simulator'
Group Members:
    Rigo Castro
    Alan Garrido
    Kenai Lozada
    Connor Moy

'''

import tkinter as tk
from random import randint

mWin = tk.Tk() # Main Window
mWin.geometry('600x400') # Size of the screen might need to change
mWin.title("'Blackjack Casino Sim!'") # Needs a different title
mWin.configure(bg='#243b5e') # theme not important rn, current colour temporary

menuFrm = tk.Frame(mWin, bg='#22552d') # Menu Frame
bljFrm = tk.Frame(mWin, bg='#0c3b16') # Blackjack game frame

cardList = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] # List of all usable cards

cT = 0 # total of cards added up
cards = [] # Player's Hand

dCards = [] # Dealer's Hand
dT = 0 # Dealer's Total

chips = tk.IntVar # Total money player put in



image_path_for_2 = "Two.png"
image_path_for_dealer = "Two.png"

# Create PhotoImage objects directly for the card values 2 and dealer
tk_img_for_2 = tk.PhotoImage(file=image_path_for_2)
tk_img_for_dealer = tk.PhotoImage(file=image_path_for_dealer)

width, height = 50, 75

# Resize images
tk_img_for_2 = tk_img_for_2.subsample(int(tk_img_for_2.width() / width), int(tk_img_for_2.height() / height))
tk_img_for_dealer = tk_img_for_dealer.subsample(int(tk_img_for_dealer.width() / width), int(tk_img_for_dealer.height() / height))

# Create Label widgets to display the images for the card values 2 and dealer
img_label_for_2 = tk.Label(bljFrm, image=tk_img_for_2, bg='#0c3b16')
img_label_for_2.image = tk_img_for_2  # Keep a reference to the image to prevent it from being garbage collected


img_label_for_dealer = tk.Label(bljFrm, image=tk_img_for_dealer, bg='#0c3b16')
img_label_for_dealer.image = tk_img_for_dealer  # Keep a reference to the image to prevent it from being garbage collected





def gC(): # gets 1 card and puts it into the cards list
    global cards
    global cT

    cNum = randint(0, 12) # Card number value
    cFace = cardList[cNum] # gets face from list
    cards += [cFace] # Adds new cards to list

    if cFace.isnumeric(): # If its a number card it just uses that value
        cT += int(cFace)
    elif cFace == 'J' or cFace == 'Q' or cFace == 'K': # If its a face card it gives it the value 10
         cT += 10
    elif cFace == 'A': # Ace can be 1 or 11 (currently doesnt work properly)
        if cT + 11 <= 21:
            cT += 11
        else:
            cT += 1
    if cFace == '2':
        img_label_for_2.place(x=310, y=150)


def chipC(): # Fixes the bug where you need to enter a number in the chips box
    global chips

    try:
        if ((monBox.get()).isnumeric):
            chips = int(monBox.get())
            chipLbl.config(text="'Chips' -->")
            startBtn.config(state=tk.NORMAL)
    except ValueError:
        startBtn.config(state=tk.DISABLED)
        chips = 0
        chipLbl.config(text='Invalid')

def getBet(): # Fixes the bet needing to be more than the minimum
    global chips
    global bet

    try:
        if ((betBox.get()).isnumeric):
            if int(betBox.get()) >= 10 and int(betBox.get()) <= chips:
                bet = int(betBox.get())
                hitBtn.config(state=tk.NORMAL)
    except ValueError:
        hitBtn.config(state=tk.DISABLED)
        bet = 0
        betLbl.config(text='Invalid')

def dlrCard(): # Gives dealer 1 card and puts in hand
    global dCards
    global dT

    cNum = randint(0, 12)
    cFace = cardList[cNum]
    dCards += [cFace] # Adds cards to dealer's hand

    if cFace.isnumeric():
        dT += int(cFace)
    elif cFace == 'J' or cFace == 'Q' or cFace == 'K':
        dT += 10
    elif cFace == 'A':
        if dT + 11 <= 21:
            dT += 11
        else:
            dT += 1
    if cFace == '2':
        img_label_for_dealer.place(x=310, y=10)
        
def stand(): # Ends Round
    global cT
    global dT
    global bet
    global chips

    dealerPlay()
    if cT > 21: # If the cards add up to more than 21 you lose
        totalLbl.config(text='Bust!')
        cardLbl.config(text=(f'Cards: {cards}'))
        winLbl.config(text='You Lost.')
        hitBtn.config(state=tk.DISABLED)
        dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
        dTotalLbl.config(text=(f"Dealer's Total: {dT}"))    
    elif dT == 0: # If the dealer busted you win
        totalLbl.config(text=(f'Total: {cT}'))
        cardLbl.config(text=(f'Cards: {cards}'))
        winLbl.config(text='You Win!')
        hitBtn.config(state=tk.DISABLED)
        dTotalLbl.config(text="Dealer's Total: Bust!")
        chips += bet*2
        monLbl.config(text=(f"'Chips': {chips}"))
    elif cT < dT: # If the dealer has more you lose
        totalLbl.config(text=(f'Total: {cT}'))
        cardLbl.config(text=(f'Cards: {cards}'))
        winLbl.config(text='You Lost.')
        hitBtn.config(state=tk.DISABLED)
        dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
        dTotalLbl.config(text=(f"Dealer's Total: {dT}"))
    else:
        totalLbl.config(text=(f'Total: {cT}'))
        cardLbl.config(text=(f'Cards: {cards}'))
        dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
        dTotalLbl.config(text=(f"Dealer's Total: {dT}"))
        hitBtn.config(state=tk.DISABLED)
        if cT == 21: # If the cards add up to 21 its a win
            winLbl.config(text='You Win!')
            chips += bet*2
            monLbl.config(text=(f"'Chips': {chips}"))
        elif cT > dT: # If your card's are more than the dealer you win
            winLbl.config(text='You Win!')
            chips += bet*2
            monLbl.config(text=(f"'Chips': {chips}"))
        elif cT == dT:
            winLbl.config(text="It's a tie!")
            chips += bet
            monLbl.config(text=(f"'Chips': {chips}"))

def hit(): # Gives dealer and player 2 cards then 1 card to player
    global cards
    global cT
    global chips
    global bet

    if len(cards) == 0: # Gives 2 Cards first hit and takes bet from money
        for i in range(2):
            dlrCard()
            gC()
        bet = int(betBox.get())
        chips -= bet # Takes bet from chips at the start of round
        monLbl.config(text=(f"'Chips': {chips}"))
    else: # Only gives 1 card after first hit
        gC()
  
    cardLbl.config(text=(f"Cards: {cards}")) # Displays cards (currently ugly)
    totalLbl.config(text=f'Total: {cT}')   # Displays cards added up total
    dCardsLbl.config(text=(f"Dealer's Cards: ['{dCards[0]}', '*']"))

    while cT > 21: # If cards go over 21, end round
        if (cards.count('A') >= 1) and (cards.index('A') == 1 or cards.index('A') == 2): # If you get an ace in your first hit it will turn that ace into 1 
            cT -= 10
            totalLbl.config(text=(f'Total: {cT}'))
        if cT > 21:
            hitBtn.config(state=tk.DISABLED)
            stand()
            break

def dealerPlay(): # Dealer draws cards after player stands
    global cT
    global dT
    global dCards

    while cT > dT: # If you have more than the dealer it'll try to get more than you
        if cT >= 21:
            dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
            break
        elif dT >= cT: # If it has more it'll stop
            dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
            break
        else:
            dlrCard()
            dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))

        if dT > 21: # If the dealer busts you win
            dT = 0
            dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
            break

def rstBlj(): # Resets game
    global cT
    global cards
    global dCards
    global dT

    cT = 0
    cards = []

    dCards = []
    dT = 0

    totalLbl.config(text='Total:')
    cardLbl.config(text='Cards:')
    winLbl.config(text='')
    dCardsLbl.config(text="Dealer's Cards:")
    hitBtn.config(state=tk.DISABLED)
    dTotalLbl.config(text="Dealer's Total:")

def placeGame(): # Places Blackjack frame
    global chips

    bljFrm.place(x=0, y=100, relwidth=1, relheight=1)
    startBtn.config(state=tk.DISABLED)
    monBox.config(state=tk.DISABLED)

    monLbl.config(text=(f"'Chips': {chips}"))


tLbl = tk.Label(menuFrm, text="'Blackjack Casino Sim!'", bg='#22552d', fg='White') # Title label
helpLbl = tk.Label(menuFrm, text="To win get as close to 21 without going over.", bg='#22552d', fg='White') # Label explains rules
startBtn = tk.Button(menuFrm, text='Start', bg='#22552d', activebackground='#0c3b16', fg='White', activeforeground='White', command=placeGame) # Button starts blackjack (or other games in the future)
monBox = tk.Entry(menuFrm, bg='#0c3b16', fg='White') # Entry box for chips
enterBtn = tk.Button(menuFrm, text='Enter', bg='#22552d', activebackground='#0c3b16', fg='White', activeforeground='White', command=chipC)
chipLbl = tk.Label(menuFrm, text="'Chips' -->", bg='#22552d', fg='White')

startBtn.config(state=tk.DISABLED)

hitBtn = tk.Button(bljFrm, text='Hit', bg='#0c3b16', activebackground='#22552d', fg='White', activeforeground='#0c3b16', command=hit) # Hit button
totalLbl = tk.Label(bljFrm, text='Total: 0', bg='#0c3b16', fg='White') # Label that displays card total
cardLbl = tk.Label(bljFrm, text='Cards:', bg='#0c3b16', fg='White') # Displays cards
winLbl = tk.Label(bljFrm, text='', bg='#0c3b16', fg='White') # Win/Lose Label
standBtn = tk.Button(bljFrm, text='Stand', bg='#0c3b16', activebackground='#22552d', fg='White', activeforeground='#0c3b16', command=stand) # Stand Button
rstBtn = tk.Button(bljFrm, text='Restart', bg='#0c3b16', activebackground='#22552d', fg='White', activeforeground='#0c3b16', command=rstBlj) # Restart Button
dCardsLbl = tk.Label(bljFrm, text="Dealer's Cards:", bg='#0c3b16', fg='White') # Dealer's Cards
dTotalLbl = tk.Label(bljFrm, text="Dealer's Total:", bg='#0c3b16', fg='White') # Dealer's Total
betBox = tk.Entry(bljFrm, bg='#22552d', fg='White') # Bet entry box
betLbl = tk.Label(bljFrm, text='Bet:', bg='#0c3b16', fg='White')
monLbl = tk.Label(bljFrm, text="'Chips':", bg='#0c3b16', fg='White')
betBtn = tk.Button(bljFrm, text='Enter Bet', bg='#0c3b16', activebackground='#22552d', fg='White', activeforeground='#0c3b16', command=getBet)
betRul = tk.Label(bljFrm, text='Min Bet 10c', bg='#0c3b16', fg='White')

hitBtn.config(state=tk.DISABLED)





# Label and button placements (Visuals are all temporary right now)
menuFrm.place(x=0, y=0, relwidth=1, relheight=1)
tLbl.place(x=300, y=20, anchor='c') 
helpLbl.place(x=300, y=80, anchor='c')
startBtn.place(x=300, y=120, anchor='c')
monBox.place(x=350, y=50, anchor='c')
enterBtn.place(x=200, y=50, anchor='c')
chipLbl.place(x=250, y=50, anchor='c')

hitBtn.place(x=20, y=120)
totalLbl.place(x=170, y=30)
cardLbl.place(x=20, y=30)
winLbl.place(x=70, y=0)
standBtn.place(x=50, y=120)
rstBtn.place(x=95, y=120)
dCardsLbl.place(x=20, y=60)
dTotalLbl.place(x=20, y=90)
betLbl.place(x=20, y=170)
betBox.place(x=50, y=170)
monLbl.place(x=140, y=170)
betBtn.place(x=150, y=200)
betRul.place(x=50, y=200)

mWin.mainloop()


''' 

To do (feel free to add stuff):
* Boot the player to menu if they run out of chips
* Double down
* Two hands
* Multiplayer
* 
* 
* 

Make it look good (important):
* Change the title
* Fix Placements
* Fix frames and positions
* Change colours
* 
* 
* 

Bugs(If you find any put here):
* If player and dealer have 21 player always wins (should be tie)
* You can get more than 4 of the same card 
* Dealer doesn't stop if it's close to busting (It will try it's hardest to beat the player at least)
*
* 
* 

'''
