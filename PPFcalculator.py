import matplotlib.pyplot as plt
from tkinter import *
from tkinter.ttk import *


root = Tk()
# program was created for my economics teacher, Mr. Bradshaw
root.title("Bradshaw's PPF Calculator")

'''Creating the labels and entrys to get data from user''' 
#---------------------------------------------------------------------------------

country1Label = Label(text='Enter the name of the first country for the PPF graph:', font=("Arial", 18), pad=5)
country1Label.grid(row=0,column=0, sticky=W, padx=5, pady=5)

country1 = Entry(root)
country1.grid(row=1, column=0, sticky=W, ipadx=40, ipady=6, pady=5, padx=5)

#---------------------------------------------------------------------------------

good1Label = Label(text='Enter the name of the first good you want to compare:', font=("Arial", 18), pad=5)
good1Label.grid(row=2,column=0, sticky=W, padx=5, pady=5)

good1 = Entry(root)
good1.grid(row=3, column=0, sticky=W, ipadx=40, ipady=6, pady=5, padx=5)

#---------------------------------------------------------------------------------

good2Label = Label(text='Enter the name of the second good you want to compare:', font=("Arial", 18), pad=5)
good2Label.grid(row=4,column=0, sticky=W, padx=5, pady=5)

good2 = Entry(root)
good2.grid(row=5, column=0, sticky=W, ipadx=40, ipady=6, pady=5, padx=5)

#---------------------------------------------------------------------------------

gd1ctry1qntLabel = Label(text='Enter the max amount of the first good the first country can produce: ', font=("Arial", 18), pad=5)
gd1ctry1qntLabel.grid(row=6, column=0, sticky=W, padx=5, pady=5)

gd1ctry1qnt = Entry(root)
gd1ctry1qnt.grid(row=7, column=0, sticky=W, ipadx=40, ipady=6, pady=5, padx=5)

#---------------------------------------------------------------------------------

gd2ctry1qntLabel = Label(text='Enter the max amount of the second good the first country can produce: ', font=("Arial", 18), pad=5)
gd2ctry1qntLabel.grid(row=8, column=0, sticky=W, padx=5, pady=5)

gd2ctry1qnt = Entry(root)
gd2ctry1qnt.grid(row=9, column=0, sticky=W, ipadx=40, ipady=6, pady=5, padx=5)

#---------------------------------------------------------------------------------

country2Label = Label(text='Enter the name of the second country for the PPF graph:', font=("Arial", 18), pad=5)
country2Label.grid(row=10,column=0, sticky=W, padx=5, pady=5)

country2 = Entry(root)
country2.grid(row=11, column=0, sticky=W, ipadx=40, ipady=6, pady=5, padx=5)

#---------------------------------------------------------------------------------

gd1ctry2qntLabel = Label(text='Enter the max amount of the first good the second country can produce: ', font=("Arial", 18), pad=5)
gd1ctry2qntLabel.grid(row=12, column=0, sticky=W, padx=5, pady=5)

gd1ctry2qnt = Entry(root)
gd1ctry2qnt.grid(row=13, column=0, sticky=W, ipadx=40, ipady=6, pady=5, padx=5)

#---------------------------------------------------------------------------------

gd2ctry2qntLabel = Label(text='Enter the max amount of the first good the second country can produce: ', font=("Arial", 18), pad=5)
gd2ctry2qntLabel.grid(row=14, column=0, sticky=W, padx=5, pady=5)

gd2ctry2qnt = Entry(root)
gd2ctry2qnt.grid(row=15, column=0, sticky=W, ipadx=40, ipady=6, pady=5, padx=5)


#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

show = False
count = 0 

def enter():
    
    # names changed to prevent error 
    c1 = country1.get()
    c2 = country2.get()
    
    g1 = good1.get()
    g2 = good2.get()
    
    if gd1ctry1qnt.get() != '':
        good1ctry1qnt = int(gd1ctry1qnt.get())
    else:
        good1ctry1qnt = 1
    if gd2ctry1qnt.get() != '':
        good2ctry1qnt = int(gd2ctry1qnt.get())
    else:
        good2ctry1qnt = 1
    
    if gd1ctry2qnt.get() != '':
        good1ctry2qnt = int(gd1ctry2qnt.get())
    else:
        good1ctry2qnt = 1
    if gd2ctry2qnt.get() != '':   
        good2ctry2qnt = int(gd2ctry2qnt.get())
    else:
        good2ctry2qnt = 1
    
    # if statement to prevent program from creating window before values are entered / start of program
    if c1 != '':        
        '''Creating new window for graphs'''
    
    
        newWindow = Toplevel()
 
        # sets the title of the
        # Toplevel widget
        newWindow.title("PPF " + c1 + " vs. " + c2)
 
        # sets the geometry of toplevel
        newWindow.geometry("750x420")
        
    

        '''-----logic to create output------'''
    
        #absolute advantage
        AAgood1 = ""
        AAgood2 = ""

        if (good1ctry1qnt > good1ctry2qnt):
            AAgood1 = c1
        else:
            AAgood1 = c2
    
        if (good2ctry1qnt > good2ctry2qnt):
            AAgood2 = c1
        else:
            AAgood2 = c2

        if AAgood1 == AAgood2:
            Label(newWindow, text= "" + AAgood1 + " has the absolute advantage in the production of both " + g1 + " and " + g2, pad=10, font=("Arial", 25), wraplength=700).grid(row=0, column=0, sticky=NW, pady=5, padx=5)
        else:
            Label(newWindow, text= AAgood1 + " has the absolute advantage in the production of " + g1 + ", while " + AAgood2 + " has the absolute advantage in the production of " + g2, pad=10, font=("Arial", 25), wraplength=700).grid(row=0, column=0, sticky=NW, padx=5, pady=5)
        # ratio to use for comparative advantage
        g1g2RatioC1 = round(good1ctry1qnt / good2ctry1qnt, 3)
        g1g2RatioC2 = round(good1ctry2qnt / good2ctry2qnt, 3)

        compAdG1 = ""
        compAdG2 = ""
        if g1g2RatioC1 > g1g2RatioC2:
            compAdG1 = c2
            compAdG2 = c1
            
            Label(newWindow, wraplength=700, text=compAdG2 + " has the comparative advantage in " + g1 +
                    " because the opportunity cost for 1 " + g1 + " is " + str(round(1/g1g2RatioC1, 3)) + " " + g2 +
                    ", while the opportunity cost for " + compAdG1 + " is " + str(round(1/g1g2RatioC2, 3)) + " sugars. However, " + compAdG1 + " has the comparative advantage in " + g2 +
                    " because the opportunity cost for 1 " + g2 + " is " + str(g1g2RatioC2) + " " + g1 +
                    ", while the opportunity cost for " + compAdG2 + " is " + str(g1g2RatioC1) + " " + g1, pad=10, font=("Arial", 25)).grid(row=1, column=0, sticky=NW, padx=5, pady=5)
          
        else:
            compAdG1 = c1
            compAdG2 = c2
            
            Label(newWindow, wraplength=700, text= compAdG2 + " has the comparative advantage in " + g1 +
                  " because the opportunity cost for 1 " + g1 + " is " + str(round(1/g1g2RatioC2,3)) + " " + g2 +
                  ", while the opportunity cost for " + compAdG1 + " is " + str(round(1/g1g2RatioC1,3)) + " sugars. \n\nHowever, " + compAdG1 + " has the comparative advantage in " + g2 +
                  " because the opportunity cost for 1 " + g2 + " is " + str(g1g2RatioC1) + " " + g1 +
                  ", while the opportunity cost for " + compAdG2 + " is " + str(g1g2RatioC2) + " " + g1, pad=10, font=("Arial", 25)).grid(row=1, column=0, sticky=NW, padx=5, pady=5)
     
        '''|----creating graphs----|'''
        
        # allows me to create graphs side by side within one figure (window)
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True, num="PPF for " + c1 + " and " + c2 + " with Mutually Beneficial Trades")
        
        # plotting the points of first graph
        x = [good1ctry1qnt, 0]
        y = [0, good2ctry1qnt]
        ax1.plot(x, y, linewidth=2.5)
        
        # naming the x and y axis of first graph
        ax1.set_xlabel(g1)
        ax1.set_ylabel(g2)
        
        # giving a title to first graph
        ax1.set_title('PPF ' + c1)
        
        
        # plotting the points of second graph
        x2 = [good1ctry2qnt, 0]
        y2 = [0, good2ctry2qnt]
        ax2.plot(x2, y2, linewidth=2.5)
        
        # naming the x and y axis of second graph
        ax2.set_xlabel(g1)
        ax2.set_ylabel(g2)
        
        # giving a title to second graph
        ax2.set_title('PPF ' + c2)
        
        #formatting
        plt.subplots_adjust(left=0.12,
                            bottom=0.12,
                            right=0.9,
                            top=0.9,
                            wspace=0.4,
                            hspace=0.4)
        
        # makes second graph have numbers by its axis (numbers were removed by sharing y axis)
        ax2.yaxis.set_tick_params(which='both', labelleft=True)
        
        #equation of graph 1 (country 1) ppf curve
        def c1GetG2(g1Qnt):
            # y=mx+b
            g2Qnt = -(good2ctry1qnt/good1ctry1qnt) * g1Qnt + good2ctry1qnt
            return g2Qnt
        
        #equation of graph 2 (country 2) ppf curve
        def c2GetG2(g1Qnt):
            # y=mx+b
            g2Qnt = -(good2ctry2qnt/good1ctry2qnt) * g1Qnt + good2ctry2qnt
            return g2Qnt
        
        
        # trades for when country 1 maximizes good 1, country 2 maximizes good 2
        for G1outC1 in range(1, good1ctry1qnt+1):
            for G2inC1 in range(1, good2ctry2qnt+1):
                # if y at the x amount after trade is greater than the y before trade,
                # and the same is true for the second graph, then it's mutually beneficial
                if (G2inC1 > c1GetG2(good1ctry1qnt - G1outC1) and (c2GetG2(G1outC1) < (good2ctry2qnt - G2inC1))): 
                    ax1.plot(good1ctry1qnt - G1outC1, G2inC1,'ro')           
                    ax2.plot(G1outC1, good2ctry2qnt - G2inC1,'ro') 
        
        # trades for when country 1 maximizes good 2, country 2 maximizes good 1
        for G2outC1 in range(1, good2ctry1qnt+1):
            for G1inC1 in range(1, good1ctry2qnt+1):
                # if y at the x amount after trade is greater than the y before trade,
                # and the same is true for the second graph, then it's mutually beneficial
                if (c1GetG2(G1inC1) < good2ctry1qnt - G2outC1) and ((G2outC1) > c2GetG2(good1ctry2qnt - G1inC1)): 
                    ax1.plot(G1inC1, good2ctry1qnt - G2outC1, 'ro')           
                    ax2.plot(good1ctry2qnt - G1inC1, G2outC1, 'ro') 
        
        
        plt.legend(["PPF curve","Mutually beneficial trades"])
        fig.set_size_inches(9, 6)
        plt.show()
          
        
enterButton = Button(text='Enter', pad=5, command=enter())
root.bind('<Return>', lambda e1: enter())
enterButton.bind('<Button-1>', lambda e2: enter())
enterButton.grid(row=15, column=1, ipady=10, ipadx=20)

    
root.mainloop()
