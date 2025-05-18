import random as rd, time
from my import valip

wins = [(i*3, i*3+1,i*3 +2) for i in range(3)] + [(i,i+3,i+6) for i in range(3)] + [(0,4,8), (2,4,6)]
cd = lambda n : (int(n) in range(1,10) and ppos[int(n)-1] == " ")
plrs = ["X","O"]
opt = [max, min]
brd ="\n¹  |²  |³\n {} | {} | {}\n___|___|___\n⁴  |⁵  |⁶\n {} | {} | {}\n___|___|___\n⁷  |⁸  |⁹\n {} | {} | {}\n   |   |"
dv = {"a":0, "b":2, "c":8} #depth value for minimax algorithm

def win(b, p):
    for j in wins:
        if(b[j[0]] == b[j[1]] == b[j[2]] == p):
            return True

def substates(s, p):
    for i in range(9):
        if(s[i] == " "):
            yield (s[:i] + [p] + s[i+1:] , i )

def utl(s, dep, r = 1): #plrt, opt are global
    if(win(s, plrt[r])):
        return 2*r - 1
    if(dep == 0 or s.count(" ") == 0):
        return 0
    return opt[r]([utl(i[0], dep-1, not r) for i in substates(s, plrt[not r])])

def game():
    for i in range(9):
        plr = plrs[i%2]
        if(plrm[plr] == "Computer opponent"):
            d = {i[1]: utl(i[0], depth) for i in substates(ppos, plr)}
            optpos = [ j for j in d if d[j] == max(d.values())]
            box = rd.choice(optpos) + 1
            print("\nComputer opponent({}) enters box {}\n".format(plr,box))
        else:
            box = int(valip("\n{} ({}) choose a box from 1 to 9 : ".format(plr, plrm[plr]), cd, "Enter a valid input!"))
        ppos[box - 1] = plr
        print(brd.format(*ppos))
        time.sleep(1)
        if(i > 4 and win(ppos,plr)):
            print("\n{} ({}) wins!".format(plr, plrm[plr]))
            return
    print("\nIt's a draw!")

while True:
    print("\nDo you want to play\n\ta. Against computer opponent\n\tb. Multiplayer")
    c = valip("\nEnter a or b : ", lambda s: s.lower() == "a" or s.lower() == "b", "Enter a or b only!").lower()
    ppos = [" " for i in range(9)]
    if(c == "a"):
        print("Choose difficulty\n\ta. Easy\n\tb. Medium\n\tc. Unbeatable\n")
        dif = valip("Enter a, b or c : ", lambda a: a.lower() in ("a", "b", "c"), "Enter a valid input!\n").lower()
        depth = dv[dif]
        st = rd.randint(0,1)
        plrt = plrs[::2*st-1]
        plrm = dict(zip(plrt,["You","Computer opponent"]))
    else:
        plrm = {"X":"Player 1","O":"Player 2"}
    print(f"\nX ({plrm['X']}) starts!\n")
    print(brd.format(*ppos))
    time.sleep(1)
    game()
    rep = valip("\nDo you want to play again(y/n) ? ", lambda a: a.lower() == "y" or a.lower() == "n", "Enter y or n only!").lower()
    if(rep == "n"):
        break


        


