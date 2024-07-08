import random

def rock_sci_paper(user_choice, comp_choice):
    global user_point, comp_point
    if user_choice == comp_choice:
        return f'Even! Current score - Mine: {comp_point}, Yours: {user_point}'
    elif (user_choice == 'rock' and comp_choice == 'scissor') or \
            (user_choice == 'scissor' and comp_choice == 'paper') or \
            (user_choice == 'paper' and comp_choice == 'rock'):
        user_point += 1
        return "You win this hand!"
    else:
        comp_point += 1
        return "I win this hand!"


def score_ev(user_point, comp_point):
    if user_point == 3:
        return 'You won the game!'
    elif comp_point == 3:
        return 'I won the game! Cry about it!'
    else:
        return None


def oyun():
    global user_point, comp_point
    user_point = 0
    comp_point = 0

    print("Welcome to Rock, Scissors, Paper game!")

    while user_point < 3 and comp_point < 3:
        user_choice = input("Make your choice (rock, scissor, paper): ").lower()
        if user_choice not in ["rock", "scissor", "paper"]:
            print("Make a valid choice!")
            continue

        options = ["rock", "scissor", "paper"]
        comp_choice = random.choice(options)
        print(f"My choice is {comp_choice}")

        result = rock_sci_paper(user_choice, comp_choice)
        print(result)

        score_message = score_ev(user_point, comp_point)
        if score_message:
            print(score_message)
            break


oyun()
