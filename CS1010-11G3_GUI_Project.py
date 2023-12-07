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
mWin.geometry('750x600') # Size of the screen might need to change
mWin.title("'Blackjack Casino Sim!'") # Needs a different title
mWin.configure(bg='#243b5e') # theme not important rn, current colour temporary

menuFrm = tk.Frame(mWin, bg='#22552d') # Menu Frame
bljFrm = tk.Frame(mWin, bg='#0c3b16') # Blackjack game frame

cardList = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] # List of all usable cards

cT = 0 # total of cards added up
cards = [] # Player's Hand
numCards = 0 # Number of cards in players hand

dCards = [] # Dealer's Hand
dT = 0 # Dealer's Total
numDlr = 0 # Number of cards the dealer has

chips = tk.IntVar # Total money player put in

cImgX = 250
cImgY = 10


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f'{width}x{height}+{x}+{y}')


def center_content(window):
    content_width = window.winfo_reqwidth()
    content_height = window.winfo_reqheight()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - content_width) // 2
    y = (screen_height - content_height) // 2

    # Update the position of the frames and widgets
    menuFrm.place(x=0, y=0, relwidth=1, relheight=1)
    tLbl.place(x=window.winfo_width() // 2, y=20, anchor='c')
    helpLbl.place(x=window.winfo_width() // 2, y=80, anchor='c')
    startBtn.place(x=window.winfo_width() // 2, y=120, anchor='c')
    monBox.place(x=window.winfo_width() // 2 + 50, y=50, anchor='c')
    enterBtn.place(x=window.winfo_width() // 2 - 100, y=50, anchor='c')
    chipLbl.place(x=window.winfo_width() // 2 - 50, y=50, anchor='c')

    

    

def gC(): # gets 1 card and puts it into the cards list
    global cards, cT, cImgY
    cImgY = 25

    cNum = randint(0, 12) # Card number value
    cFace = cardList[cNum] # gets face from list
    cards += [cFace] # Adds new cards to list

    placeImage(cNum)

    if cFace.isnumeric(): # If its a number card it just uses that value
        cT += int(cFace)
    elif cFace == 'J' or cFace == 'Q' or cFace == 'K': # If its a face card it gives it the value 10
         cT += 10
    elif cFace == 'A': # Ace can be 1 or 11 (currently doesnt work properly)
        if cT + 11 <= 21:
            cT += 11
        else:
            cT += 1

def placeImage(cNum): # Places card images on screen
    global cImgX, cImgY, numCards
    
    cImgX = 300 + (50*numCards)
    numCards += 1
    cImgY = 10

    cImg = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

    image_path = f"Assets/{cImg[cNum]}.png"

    # Create a PhotoImage object directly
    tk_img = tk.PhotoImage(file=image_path)

    width, height = 100, 150
    tk_img = tk_img.subsample(int(tk_img.width() / width), int(tk_img.height() / height))

    # Create a Label widget to display the image
    img_label = tk.Label(bljFrm, image=tk_img, bg='#0c3b16')
    img_label.image = tk_img  # Keep a reference to the image to prevent it from being garbage collected

    # Place the image label on the frame
    img_label.place(x=cImgX, y=cImgY)

def dlrImage(cNum): # Places dealers cards
    global cImgX, cImgY, numDlr

    cImgX = 300 + (50*numDlr)
    numDlr += 1
    cImgY = 200

    cImg = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

    image_path = f"Assets/{cImg[cNum]}.png"

    # Create a PhotoImage object directly
    tk_img = tk.PhotoImage(file=image_path)

    width, height = 100, 150
    tk_img = tk_img.subsample(int(tk_img.width() / width), int(tk_img.height() / height))

    # Create a Label widget to display the image
    img_label = tk.Label(bljFrm, image=tk_img, bg='#0c3b16')
    img_label.image = tk_img  # Keep a reference to the image to prevent it from being garbage collected

    # Place the image label on the frame
    img_label.place(x=cImgX, y=cImgY)

def chipC(): # Fixes the bug where you need to enter a number in the chips box
    global chips

    try:
        if ((monBox.get()).isnumeric):
            chips = int(monBox.get())
            chipLbl.config(text="Chips -->")
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
    global dCards, dT

    cNum = randint(0, 12)
    cFace = cardList[cNum]
    dCards += [cFace] # Adds cards to dealer's hand

    dlrImage(cNum)

    if cFace.isnumeric():
        dT += int(cFace)
    elif cFace == 'J' or cFace == 'Q' or cFace == 'K':
        dT += 10
    elif cFace == 'A':
        if dT + 11 <= 21:
            dT += 11
        else:
            dT += 1

def stand(): # Ends Round
    global cT, dT, bet, chips

    dealerPlay()
    if cT > 21: # If the cards add up to more than 21 you lose
        totalLbl.config(text='Bust!')
        cardLbl.config(text=(f'Cards: {cards}'))
        winLbl.config(text='You Lost.', font=('Helvetica', 12, 'bold'),)
        hitBtn.config(state=tk.DISABLED)
        dCardsLbl.config(text=(f"Dealer's Cards: {dCards}"))
        dTotalLbl.config(text=(f"Dealer's Total: {dT}"))    
    elif dT == 0: # If the dealer busted you win
        totalLbl.config(text=(f'Total: {cT}'))
        cardLbl.config(text=(f'Cards: {cards}'))
        winLbl.config(text='You Win!', font=('Helvetica', 12, 'bold'))
        hitBtn.config(state=tk.DISABLED)
        dTotalLbl.config(text="Dealer's Total: Bust!")
        chips += bet*2
        monLbl.config(text=(f"'Chips': {chips}"))
    elif cT < dT: # If the dealer has more you lose
        totalLbl.config(text=(f'Total: {cT}'))
        cardLbl.config(text=(f'Cards: {cards}'))
        winLbl.config(text='You Lost.', font=('Helvetica', 12, 'bold'))
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
            winLbl.config(text='You Win!', font=('Helvetica', 12, 'bold'))
            chips += bet*2
            monLbl.config(text=(f"Chips: {chips}"))
        elif cT > dT: # If your card's are more than the dealer you win
            winLbl.config(text='You Win!',font=('Helvetica', 12, 'bold'))
            chips += bet*2
            monLbl.config(text=(f"'Chips': {chips}"))
        elif cT == dT:
            winLbl.config(text="It's a tie!", font=('Helvetica', 12, 'bold'))
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
    
    while cT > 21: # If cards go over 21, end round
        if (cards.count('A') >= 1) and (cards.index('A') == 1 or cards.index('A') == 2): # If you get an ace in your first hit it will turn that ace into 1 
            cT -= 10
            totalLbl.config(text=(f'Total: {cT}'))
        if cT > 21:
            hitBtn.config(state=tk.DISABLED)
            stand()
            break
    
    cardLbl.config(text=(f"Cards: {cards}")) # Displays cards (currently ugly)
    totalLbl.config(text=f'Total: {cT}')   # Displays cards added up total
    dCardsLbl.config(text=(f"Dealer's Cards: ['{dCards[0]}', '*']"))

   

def dealerPlay(): # Dealer draws cards after player stands
    global cT, dT, dCards

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
    global cT, cards, dCards, dT, cImgX, numCards, numDlr

    for widget in bljFrm.winfo_children():
        if isinstance(widget, tk.Label) and widget.winfo_y() == 10:
            widget.destroy()

    # Destroy the image labels for dealer's cards
    for widget in bljFrm.winfo_children():
        if isinstance(widget, tk.Label) and widget.winfo_y() == 200:
            widget.destroy()
    
    cT = 0
    cards = []
    cImgX = 250
    dCards = []
    dT = 0
    numCards = 0
    numDlr = 0

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


tLbl = tk.Label(menuFrm, text="Blackjack Casino Sim!",font=('Helvetica', 14, 'bold'), bg='#22552d', fg='White') # Title label
helpLbl = tk.Label(menuFrm, text="To win get as close to 21 without going over.",font=('Helvetica', 12, 'bold'), bg='#22552d', fg='White') # Label explains rules
startBtn = tk.Button(menuFrm, text='Start', bg='#22552d', activebackground='#0c3b16', fg='White', activeforeground='White', command=placeGame) # Button starts blackjack (or other games in the future)
monBox = tk.Entry(menuFrm, bg='#0c3b16', fg='White') # Entry box for chips
enterBtn = tk.Button(menuFrm, text='Enter', bg='#22552d', activebackground='#0c3b16', fg='White', activeforeground='White', command=chipC)
chipLbl = tk.Label(menuFrm, text="Chips -->",font=('Helvetica',10 , 'bold'), bg='#22552d', fg='White')

startBtn.config(state=tk.DISABLED)

hitBtn = tk.Button(bljFrm, text='Hit', bg='#0c3b16', activebackground='#22552d', fg='White', activeforeground='#0c3b16', command=hit) # Hit button
totalLbl = tk.Label(bljFrm, text='Total: 0',font=('Helvetica', 12, 'bold'), bg='#0c3b16', fg='White') # Label that displays card total
cardLbl = tk.Label(bljFrm, text='Cards:',font=('Helvetica', 12, 'bold'), bg='#0c3b16', fg='White') # Displays cards
winLbl = tk.Label(bljFrm, text='', bg='#0c3b16', fg='White') # Win/Lose Label
standBtn = tk.Button(bljFrm, text='Stand', bg='#0c3b16', activebackground='#22552d', fg='White', activeforeground='#0c3b16', command=stand) # Stand Button
rstBtn = tk.Button(bljFrm, text='Restart', bg='#0c3b16', activebackground='#22552d', fg='White', activeforeground='#0c3b16', command=rstBlj) # Restart Button
dCardsLbl = tk.Label(bljFrm, text="Dealer's Cards:", font=('Helvetica', 12, 'bold'), bg='#0c3b16', fg='White') # Dealer's Cards
dTotalLbl = tk.Label(bljFrm, text="Dealer's Total:",  font=('Helvetica', 12, 'bold'), bg='#0c3b16', fg='White') # Dealer's Total
betBox = tk.Entry(bljFrm, bg='#22552d', fg='White') # Bet entry box
betLbl = tk.Label(bljFrm, text='Bet:',font=('Helvetica', 11, 'bold'), bg='#0c3b16', fg='White')
monLbl = tk.Label(bljFrm, text="Chips:",font=('Helvetica', 12, 'bold'), bg='#0c3b16', fg='White')
betBtn = tk.Button(bljFrm, text='Enter Bet', bg='#0c3b16', activebackground='#22552d', fg='White', activeforeground='#0c3b16', command=getBet)
betRul = tk.Label(bljFrm, text='Min Bet 10chips',font=('Helvetica', 8, 'bold'), bg='#0c3b16', fg='White')
dlrLabel = tk.Label(bljFrm, text="DEALER'S HAND", font=('Helvetica', 14, 'bold'),  bg='#0c3b16', fg='White')
plyrLabel = tk.Label(bljFrm, text="PLAYER'S HAND", font=('Helvetica', 14, 'bold'),  bg='#0c3b16', fg='White')

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
totalLbl.place(x=20, y=40)
winLbl.place(x=70, y=0)
standBtn.place(x=50, y=120)
rstBtn.place(x=95, y=120)
dTotalLbl.place(x=20, y=80)
betLbl.place(x=15, y=170)
betBox.place(x=50, y=170)
monLbl.place(x=140, y=170)
betBtn.place(x=150, y=200)
betRul.place(x=50, y=200)
dlrLabel.place(x=350, y=370)
plyrLabel.place(x=350, y=175)

center_window(mWin, 600, 500)
center_content(mWin)

# Bind the function to window resize event
mWin.bind('<Configure>', lambda event: center_content(mWin))



mWin.mainloop()
