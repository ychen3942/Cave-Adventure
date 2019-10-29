#Yu Feng Chen
#Adventure_V2

import time
import math
from random import randint

def timer():
    begin = time.perf_counter()
    Action = input("Enter your action:")
    end = time.perf_counter()
    t = (end - begin)
    return (t,Action)

def Event(N):
    E = randint(1,7)
    if E == 1:
        return split(N)
    if E == 2:
        return secret(N)
    if E == 3:
        return chest(N)
    if E == 4:
        return monster(N)
    if E == 5:
        return arrow(N)
    if E == 6:
        return floor(N)
    if E == 7:
        return stone(N)

def invalid():
    print("That's not a valid action... and the time runs out.")
    return "invalid"

def oot():
    print("You ran out of time, the floor collapse below you.") 
    return "out of time"
    
def split(N):
    print("You had come to an end of a path, there was a way to the left and there was another way to the right.")
    time.sleep(3)
    print("Now, choose a path to proceed. 'left' or 'right'.")
    time.sleep(2)
    t,Action = timer()
    if t > N:
        return oot()
    elif t <= N:
        if Action == "back":
            print("You don't quiet remeber where you came from, plus time is runing out!")
            return "invalid"
        elif Action == "left" or "right":
            Path = randint(0,1)
            if Path == 0:
                print("This path leads to a dead end. You then went back and take on the other path.")
                return "hold"
            elif Path == 1:
                print("This path doesn't seems leading to a dead end. You are on your way again.")
                return "pass"
        else :
            return invalid()

def secret(N):
    print("You accidently stepped onto a stone, then there was a secret path opened for you on the wall.")
    time.sleep(3)
    print("Would you take on the secret path? 'yes' or 'no'")
    time.sleep(2)
    t,Action = timer()
    if t > N:
        return oot()
    elif t <= N:
        if Action == "no":
            print("You continue on your original path.")
            return "pass"
        elif Action == "yes":
            Secret = randint(0,3)
            if Secret == 0:
                print("This path leads to a dead end. You then went back and take on the original path.")
                return "hold"
            elif Secret == 1:
                print("This path doesn't seems leading to a dead end. You are on your way again.")
                return "pass"
            elif Secret == 2:
                print("The entrance is closed behind you as you entered into a room without any other exit, you are now trapped inside.")
                return "dead"
            elif Secret == 3:
                return chest(N)
        else :
            return invalid()

def chest(N):
    print("On your way, you discovered a shiny chest at the far end around the corner.")
    time.sleep(3)
    print("Would you approach and open the chest? 'yes' or 'no'")
    time.sleep(2)
    t,Action = timer()
    if t > N:
        return oot()
    elif t <= N:
        if Action == "no":
            print("You continue on your path.")
            return "pass"
        elif Action == "yes":
            Chest = randint(0,1)
            if Chest == 0:
                print("Congratuation! You have found a treasure chest, you brought the treasures along and continue on your way.")
                return "treasure"
            elif Chest == 1:
                print("Oh no, it turns out to be a Mimic monster. And it start to approaching you.")
                time.sleep(2.5)
                print("Please enter 'burn' and wave your torch at the Mimic.")
                time.sleep(2)
                t,Action = timer()
                if t > N:
                    return oot()
                elif t <= N:
                    if Action == "burn":
                        print("The Mimic is scared off, and you resume on your way.")
                        return "pass"
                    else :
                        return invalid()
        else :
            return invalid()

def monster(N):
    print("On your way, you discovered a gaint monster who was asleep on the side of your path.")
    time.sleep(3)
    print("Would you 'sneak' around the monster or 'take' another path?")
    time.sleep(3)
    t,Action = timer()
    if t > N:
        return oot()
    elif t <= N:
        if Action == "take":
            print("You went back and take on an other path.")
            return "hold"
        elif Action == "sneak":
            Monster = randint(0,1)
            if Monster == 0:
                print("You carefully sneaked around the monster without waking it. You are on your path again.")
                return "pass"
            elif Monster == 1:
                print("Oh no, the monster sunddenly awakes as you try to get over.")
                time.sleep(2.5)
                print("Please enter 'fight' and use your weapon to fight off the monster.")
                time.sleep(2)
                t,Action = timer()
                if t > N:
                    return oot()
                elif t <= N:
                    if Action == "fight":
                        Fight = randint(0,3)
                        if Fight == 0:
                            print("You had try your best, but the monster is too strong to beat and you are injured severely.")
                            return "dead"
                        else :
                            print("You successfully injured the monster, and you resume on your way.")
                            return "slay"
                    else :
                        return invalid()
        else :
            return invalid()

def arrow(N):
    print("You accidently activated a trap, you saw arrows shooting out from the wall towards you")
    time.sleep(3)
    print("Please enter 'duck' to avoid the arrows.")
    time.sleep(2)
    t,Action = timer()
    if t > N:
        return oot()
    elif t <= N:
        if Action == "duck":
            print("You dodged the arrows in time, and you are on your path again.")
            return "pass"
        else :
            return invalid()

def floor(N):
    print("You accidently activated a trap, the floor below you starts to collapse.")
    time.sleep(3)
    print("Please enter 'leap' to leap over the falling ground.")
    time.sleep(2)
    t,Action = timer()
    if t > N:
        return oot()
    elif t <= N:
        if Action == "leap":
            print("You successfully leap over the falling ground, and you are on your path again.")
            return "pass"
        else :
            return invalid()

def stone(N):
    print("You accidently activated a trap, there is a huge stone dropped down from the ceiling and rolling toward you.")
    time.sleep(3.5)
    print("Please enter 'turn' to turn around over the corner of the path.")
    time.sleep(2.5)
    t,Action = timer()
    if t > N:
        return oot()
    elif t <= N:
        if Action == "turn":
            print("You made the turn in time, and you are on your path again.")
            return "pass"
        else :
            return invalid()


          
inf = float('inf')
Again = "yes"
while Again == "yes":

    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("Welcome to The Adventure 2.0, Adventurer! You are in a large maze deep inside an ancient tomb, seeking for fortune. Suddenly, the floor shakes beneath your feet, and particles start to fall from the ceiling.")
    print("It seems that the tomb is going to collapse. Oh no, you are in great danger! In order to survive, you must escape the tomb! NOW!")
    print("When you are on your way to escape, you will have to reacto to different scenarios. You need to enter specific commands and/or decisions within a specific time frame according to the situation.") 
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("The level of difficulty determines the limit on time you have to enter your action within the scenarios.")
    Level = input("Select the level of difficulty: (B)eginner - 7 sec, (I)ntermediate - 5 sec, or (E)xpert - 3.5 sec.")
    print("The mode determines the number of scenarios you will encounter.")
    Mode = input("Select a game mode: (D)efault - 10 scenarios, (I)nfinity, or Determine (Y)our Own.")
    
    if Level == "B":
        L = 7
    elif Level == "I":
        L = 5
    elif Level == "E":
        L = 3.5

    if Mode == "D":
        Limit = 10
    elif Mode == "I":
        Limit = inf
    elif Mode == "Y":
        Limit = int(input("Enter the limit:"))
        
    Scenario=0
    Hold=0
    Treasure=0
    Slay=0
    i=0

    print("Warning: Be aware that you only had one chance to enter the action, so enter it carefully.")
    Game = input("Prepare yourself! When you are ready, enter 'proceed' to begin your escape!")
    while i < Limit:
        if Game == "proceed":
            time.sleep(3)
            print("-----------------------------------------------------------------------------------------------------------------------------------------")
            Status = Event(L)

            if Status == "pass":
                Scenario+=1
                i+=1
            elif Status == "hold":
                Hold+=1
                i+=1
            elif Status == "treasure":
                Treasure+=1
                i+=1
            elif Status == "slay":
                Slay+=1
                i+=1
            elif Status == "out of time" or "invalid" or "dead":
                print("Unfortunately, you had failed to overcome the challenge presented in the scenario... The game is over.")
                print("-----------------------------------------------------------------------------------------------------------------------------------------")
                print("In this run, you have completed",Scenario,"scenarios. Including",Hold," times returning to a different path,",Treasure,"treasures found,and",Slay,"monster slayed. Congratulation!")
                Game = "over"
                break

    if Game == "over":
        Again = input("Do you wish to use the spell - Time Warp, and return to the starting point and attempt your escape once again? Enter 'yes' or 'no'")          

    if Again == "no":
        print("Ok. You may now Rest in Peace :)")
        Again = "done"
    if Again == "done":
        print("Thank you for participating in this wonderful adventure!!! :)")
            
            
            




