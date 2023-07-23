import random

def choose_area():
    print("choose are to invest in")
    while True:
        print("[I]nshore  [R]eef  [D]eep sea")
        invest_choice = input()
        if invest_choice == "I" or invest_choice == "R" or invest_choice == "D":
            return invest_choice
        print("Invalid choice ")


money = 0
pots = 5
day = 1
inshore_pots = 0
reef_pots = 0
deep_sea_pots = 0

for X in range(15):
    while pots > 0:
        invest_choice = choose_area()
        print("how much do you want to invest?")
        invest_amount = int(input())
        if invest_choice == "I":
            pots = pots - invest_amount
            inshore_pots = inshore_pots + invest_amount
            print("you invested " + str(inshore_pots) + " in inshore")
            print("you have " + str(pots) + " remaining")
        elif invest_choice == "R":
            pots = pots - invest_amount
            reef_pots = reef_pots + invest_amount
            print("you invested " + str(reef_pots) + " in the reef")
            print("you have " + str(pots) + " remaining")
        elif invest_choice == "D":
            pots = pots - invest_amount
            deep_sea_pots = deep_sea_pots + invest_amount
            print("you invested " + str(deep_sea_pots) + " in the deep sea")
            print("you have " + str(pots) + " remaining")

    print("to start the day press [Y]es or type [N]o to quite")
    day_start = input()
    if day_start == "Y":
        weather = (random.randint(1, 6))
        if weather == 1 or weather == 2:
            print("calm waters all pots were retrieved")
        elif weather == 3 or weather == 4:
            print("rought waters lose deep sea pots")
            deep_sea_pots = 0
        elif weather == 5 or weather == 6:
            print("storm reef and deep sea pots lost")
            deep_sea_pots = 0
            reef_pots = 0
    elif day_start == "N":
        quit()

    money += inshore_pots * 2
    money += reef_pots * 5
    money += deep_sea_pots * 10

    pots += inshore_pots
    pots += reef_pots
    pots += deep_sea_pots

    inshore_pots = 0
    reef_pots = 0
    deep_sea_pots = 0

    print("you have $" + str(money) + " money")
