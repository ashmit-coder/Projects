#  make this game a gui gam it can be goood
import random 
Chef_pos = random.randint(1, 10**4)
print(Chef_pos)
# Chef arguments ---------------------------------------------------------------

class Position_inc(object):
    def __init__(self):
        pass
    def appending(self, pos, num_pos):
        State = "NO one"
        num = 0
        wi_li = {}
        for n in range(num_pos):
            State = "NO one"
            play_pos = int(pos[n])
            initial_pos = int(pos[n])
            num = 0
            while(State != "WIN" ):
                
                if play_pos == Chef_pos:
                    State = "WIN"
                    x = str(n+1) 
                    wi_li[x] = num 
                    break
                if play_pos >= Chef_pos:
                    print(f"player {n+1} lost because he crossed the chef")
                    break
                play_pos += initial_pos
                num += 1
                if play_pos == Chef_pos:
                    State = "WIN"
                    x = str(n+1)
                    wi_li[x] = num
                    break
                if play_pos >= Chef_pos:
                    print(f"player {n+1} lost because he crossed the chef")
                    break
        return wi_li
        

        
#  make this game a gui gam it can be goood
            
        
# Class ------------------------------------------------------------------------
Num_play = int(input("Give me the no. of player my boy "))
Positions = []
for i in range(1, Num_play + 1):
    a = input(f"Give me your starting position player {i}(it must be within 1000) ")
    Positions.append(a)
# Inputs------------------------------------------------------------------------
class_use = Position_inc()
win_list = class_use.appending(Positions,Num_play)

# Loop --------------------------------------------------------------------------
print("Players who made it o the chef:- \n")
for x in win_list:
    print(x)
lst = []
for a in win_list:
    lst.append(win_list[a])

lst.sort()
print(lst)
for a in win_list:
    if win_list[a] == lst[0]:
        print(f"So,..... the winner is\n player {a} with {win_list[a]} moves")
        break

#  make this game a gui gam it can be goood