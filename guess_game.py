import random

# ------------------- input validation -------------------
def input_num(mx, mn):
    while True:
        try:
            num = int(input('enter number ' + str(mn) + '~' + str(mx) + ':'))
            if not mn <= num <= mx:
                print('the number should be between ' + str(mn) + '~' + str(mx))
            else:
                break
        except ValueError:
            print('it should be integer')
            continue
    return num

# -------------------- game configuration -----------------
maximum = 25
minimum = 1
final_round = 5

# --------------------- initialize game data ---------------
comp_max = maximum
comp_min = minimum
comp_num = random.randint(minimum,maximum)
comp_guess_history = list()
you_win = False
comp_win = False

# -------------------- start game -----------------------
your_num = input_num(maximum, minimum)
for i in range(final_round):
    print('-------------------------------')
    print('Round', str(i + 1) + '/' + str(final_round))

    your_guess_num = input_num(maximum, minimum)

    # --------------------- evaluate your guess -----------------
    if your_guess_num == comp_num:
        print('computer: you win')
        you_win = True
        break
    elif your_guess_num > comp_num:
        print('computer: down')
    else:
        print('computer: up')

    # ----------------------- computer guess (binary search) -----------------
    if (comp_max + comp_min) // 2 == 0 and minimum != 0:
        comp_guess_num = 1
    elif i + 1 == final_round:
        print('computer: this is my final guess')
        print('computer: let me see... i guessed', str(comp_guess_history))
        while True:
            comp_guess_num = random.randint(comp_min, comp_max)
            if comp_guess_num not in comp_guess_history:
                break
    else:
        comp_guess_num = (comp_max + comp_min) // 2

    print('comp guessed', str(comp_guess_num), '(your num:', str(your_num) + ')')
    comp_guess_history.append(comp_guess_num)

    # -------------------- evaluate computer guess ----------------------
    if comp_guess_num == your_num:
        print('computer: I win')
        print('computer: my guess history is', str(comp_guess_history))
        print('computer: my number was', str(comp_num))
        comp_win = True
        break
    elif comp_guess_num > your_num:
        comp_max = comp_guess_num
    else:
        comp_min = comp_guess_num

# -------------- end game ------------------------
if you_win is False and comp_win is False:
    print('\ncomputer: draw')
    print('computer: my number was', str(comp_num))