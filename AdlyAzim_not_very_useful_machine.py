import numpy as np
import time

##disclaimer: I haven't used python or any programming language in 4 years,
##            so my apologies if the code is messy or variable nomenclature
##            seems unorthodox!

Text = {"InputAsk":"Enter your input here: ",
        "YesNo":"Press 1 for Yes and 2 for No. ",
        "ReturnMain":"Return to main menu? ",
        "ShutDown":"Would you like to shut off the Machine? ",
        "Ad":"Follow @adly_fact_genius on Instagram!",
        "RoundAsk":"What number would you like to round? "}

##establishing Menu UI

def MenuChoice(y):
    if y == 1:
        NumRoundUI(y)
    if y == 2:
        SettingsUI(y)
    if y == 3:
        AdsUI(y)

def MenuReturn(z):
    if z == 1:
        x = 1
        MenuUI(x)
    if z == 2:
        time.sleep(5)
        x = 1
        MenuUI(x)

def MenuUI(x):
    if x == 1:
        mainUI = ["[NumRounder      Settings        Ads  ]",
                  "[                                     ]",
                  "[To access NumRounder, input 1. To    ]",
                  "[access Settings, input 2. To access  ]",
                  "[Ads, input 3.                        ]"]
        for words in mainUI:
            print(words)
        MenuChoice(y=int(input(Text["InputAsk"])))

    if x == 2:
        print("The Machine stays silent.")


##establishing NumRounder UI and calculator
def NumRoundUI(c):
    print("The NumRounder rounds your number to an integer!")
    def RoundNum():
        return np.round(float(input(Text["RoundAsk"])))
    NumAns = RoundNum()
    print(int(NumAns))

    MenuReturn(int(input(Text["ReturnMain"] + Text["YesNo"])))


##establishing Settings UI
def SettingsUI(p):
    k = int(input(Text["ShutDown"] + Text["YesNo"]))
    if k == 1:
        print("Shutting down...")
        time.sleep(5)
        MenuUI(x=int(input("Turn on Machine?" + Text["YesNo"])))
    if k == 2:
        MenuReturn(int(input(Text["ReturnMain"] + Text["YesNo"])))


##establishing Ads UI
def AdsUI(y):
    if y == 3:
        print(Text["Ad"])
        MenuReturn(int(input(Text["ReturnMain"] + Text["YesNo"])))


MenuUI(x=int(input("Turn on Machine?" + Text["YesNo"])))
