import random

def get_num(prompt):
    while True:
        try:
            n = int(input(prompt))
            if 1 <= n <= 6:
                return n
            else:
                print("Choose a number between 1 and 6.")
        except:
            print("Please enter a valid number.")

print("\n*** ODD OR EVEN CRICKET ***\n")


print("TOSS TIME!")
print("1. Odd")
print("2. Even")
choice = int(input("Choose (1 or 2): "))

user_num = get_num("Enter your toss number (1-6): ")
comp_num = random.randint(1,6)

print(f"You chose {user_num}, Computer chose {comp_num}")
total = user_num + comp_num

if total % 2 == 1:
    result = 1  
else:
    result = 2  

if result == choice:
    print("You won the toss.")
    print("1. Bat first")
    print("2. Bowl first")
    play = int(input("Choose (1 or 2): "))
    user_bats_first = (play == 1)
else:
    print("Computer won the toss.")
    user_bats_first = random.choice([True, False])
    if user_bats_first:
        print("Computer chooses to bowl first.")
    else:
        print("Computer chooses to bat first.")

def play_batting(player_name):
    print(f"\n{player_name} are batting now.")
    score = 0
    while True:
        if player_name == "You":
            bat = get_num("Your run (1-6): ")
            bowl = random.randint(1,6)
            print(f"Computer bowls {bowl}")
        else:
            bowl = get_num("Your bowl (1-6): ")
            bat = random.randint(1,6)
            print(f"Computer bats {bat}")

        if bat == bowl:
            print("OUT!")
            break
        else:
            score += bat
            print(f"Runs so far: {score}")

    print(f"{player_name}'s Final Score: {score}\n")
    return score


if user_bats_first:
    user_score = play_batting("You")
    comp_score = play_batting("Computer")
else:
    comp_score = play_batting("Computer")
    user_score = play_batting("You")

print("---- MATCH RESULT ----")
print(f"Your Score: {user_score}")
print(f"Computer Score: {comp_score}")

if user_score > comp_score:
    print("You Win.")
elif comp_score > user_score:
    print("Computer Wins.")
else:
    print("Match Drawn.")

print("\nThanks for playing.\n")
