import random

snakes = {99: 54, 70: 55, 52: 42, 25: 2}
ladders = {6: 25, 11: 40, 60: 85, 46: 90}

def roll_dice():
    return random.randint(1, 6)

num_players = int(input("Enter number of players: "))
players = {}
for i in range(1, num_players+1):
    name = input(f"Enter name of Player {i}: ")
    players[name] = 0

print("\n***# SNAKE AND LADDER GAME #***\n")

winner = None
while not winner:
    for name in players:
        input(f"{name}'s turn. Press Enter to roll dice...")
        dice = roll_dice()
        print(f"{name} rolled: {dice}")

        if players[name] + dice <= 100:
            players[name] += dice
        print(f"{name} moved to: {players[name]}")

        if players[name] in snakes:
            print(f"{name} got swallowed by a snake! Slide to {snakes[players[name]]}")
            players[name] = snakes[players[name]]
        elif players[name] in ladders:
            print(f"{name} climbed a ladder to {ladders[players[name]]}")
            players[name] = ladders[players[name]]

        print(f"{name}'s current position: {players[name]}\n")

        if players[name] == 100:
            winner = name
            break

print(f"Congratulations! {winner} wins the game!")
