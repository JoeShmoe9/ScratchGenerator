import random


def GenerateTiny():
    mainNum = random.randrange(10)
    ANum = random.randrange(10)
    BNum = random.randrange(10)
    CNum = random.randrange(10)
    DNum = random.randrange(10)
    ENum = random.randrange(10)
    FNum = random.randrange(10)
    GNum = random.randrange(10)
    HNum = random.randrange(10)
    INum = random.randrange(10)
    JNum = random.randrange(10)
    WinnerNum = random.randrange(10)
    winner = None
    if mainNum == ANum:
        winner = True
    if mainNum == BNum:
        winner = True
    if mainNum == CNum:
        winner = True
    if mainNum == DNum:
        winner = True
    if mainNum == ENum:
        winner = True
    if mainNum == FNum:
        winner = True
    if mainNum == GNum:
        winner = True
    if mainNum == HNum:
        winner = True
    if mainNum == INum:
        winner = True
    if mainNum == JNum:
        winner = True
    if winner != True:
        winner = False

    #printit
    print("-------------TINY------------")
    print("------------- " + str(mainNum) + " -------------")
    print("--- " + str(ANum) + " -- " + str(BNum) + " -- " + str(CNum) + " -- " + str(DNum) + " -- " + str(ENum) + " --- ")
    print("--- " + str(FNum) + " -- " + str(GNum) + " -- " + str(HNum) + " -- " + str(INum) + " -- " + str(JNum) + " --- ")
    print("----AMOUNT--- " + str(WinnerNum) + " ---AMOUNT----")
    if winner == True:
        print("------------WINNER-----------")
    else:
        print("-------------NOPE------------")      

def GenerateLarge():
    mainNum = random.randrange(10, 25)
    ANum = random.randrange(10, 25)
    BNum = random.randrange(10, 25)
    CNum = random.randrange(10, 25)
    DNum = random.randrange(10, 25)
    ENum = random.randrange(10, 25)
    FNum = random.randrange(10, 25)
    GNum = random.randrange(10, 25)
    HNum = random.randrange(10, 25)
    INum = random.randrange(10, 25)
    JNum = random.randrange(10, 25)
    WinnerNum = random.randrange(10, 25)
    winner = None
    if mainNum == ANum:
        winner = True
    if mainNum == BNum:
        winner = True
    if mainNum == CNum:
        winner = True
    if mainNum == DNum:
        winner = True
    if mainNum == ENum:
        winner = True
    if mainNum == FNum:
        winner = True
    if mainNum == GNum:
        winner = True
    if mainNum == HNum:
        winner = True
    if mainNum == INum:
        winner = True
    if mainNum == JNum:
        winner = True
    if winner != True:
        winner = False
    print("------------Large------------")
    print("------------- " + str(mainNum) + " ------------")
    print("-- " + str(ANum) + " -- " + str(BNum) + " - " + str(CNum) + " - " + str(DNum) + " -- " + str(ENum) + " - ")
    print("-- " + str(FNum) + " -- " + str(GNum) + " - " + str(HNum) + " - " + str(INum) + " -- " + str(JNum) + " - ")
    print("----AMOUNT--- " + str(WinnerNum) + " ---AMOUNT---")
    if winner == True:
        print("------------WINNER-----------")
    else:
        print("-------------NOPE------------")  




print("options - tiny, large,")
while True:
    for i in range(1):
        type = input("")
    if type == "tiny":
        GenerateTiny()
    if type == "large":
        GenerateLarge()