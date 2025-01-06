

def print_board(lst):
    a = '''
{}|{}|{}
-----
{}|{}|{}
-----
{}|{}|{}
'''.format(*lst)
    print(a)
    

choices = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
turns = "X"
print_board(choices)

while (" " in choices):
    t = int(input(f"its your turn {turns} please enter"))
    if(choices[t]==" "):
        choices[t] = turns
        turns = 'X' if turns == "0" else '0'
        print_board(choices)
    else:
        print("Your turn Dismissed")
        turns = 'X' if turns == "0" else '0'

    if((choices[0] == choices[1] == choices[2] != " " ) or (choices[3] == choices[4] == choices[5] != " " ) or (choices[6] == choices[7] == choices[8] != " " ) or (choices[0] == choices[3] == choices[6] != " " ) or (choices[1] == choices[4] == choices[7] != " " ) or (choices[2] == choices[5] == choices[8] != " " ) or (choices[0] == choices[4] == choices[8] != " " ) or (choices[0] == choices[4] == choices[6] != " " )):
        print(f"{turns} win")
        break
    else:
        print("Tie")
else:
    print("Game Ended")
