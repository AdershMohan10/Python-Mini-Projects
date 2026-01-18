import random
import sys
import time

def rnd(a, b):
    return random.randint(a, b)

def pause(msg="Press Enter to continue..."):
    input(msg)

def print_sep():
    print("-" * 50)

drops_table = [
    ("Common", 60, ("Iron Sword", 10)),
    ("Rare",   25, ("Silver Daggers", 20)),
    ("Super Rare", 10, ("Dragon Spear", 40)),
    ("Legendary", 5, ("Mighty Excalibur", 80))
]

def roll_drop():
    r = random.randint(1, 100)
    acc = 0
    for rarity, chance, item in drops_table:
        acc += chance
        if r <= acc:
            name, bonus = item
            return {"rarity": rarity, "name": name, "bonus": bonus}
   
    name, bonus = drops_table[0][2]
    return {"rarity": "Common", "name": name, "bonus": bonus}


POTIONS = {
    "Small Potion": {"heal": 20, "price": 10},
    "Medium Potion": {"heal": 50, "price": 25},
    "Super Potion": {"heal": 100, "price": 50}
}


class Character:
    def __init__(self, name, hp, atk_range, def_range):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atk_range = atk_range  
        self.def_range = def_range  

    def roll_atk(self):
        return random.randint(self.atk_range[0], self.atk_range[1])

    def roll_def(self):
        return random.randint(self.def_range[0], self.def_range[1])

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, (1,10), (1,10))
        self.level = 1
        self.xp = 0
        self.xp_to_level = 100
        self.weapon = {"name":"Regular Sword", "bonus":5}
        self.potions = {"Small Potion":1, "Medium Potion":0, "Super Potion":0}
        self.gold = 0

    def total_atk(self):
        base = random.randint(self.atk_range[0], self.atk_range[1])
        return base + self.weapon["bonus"]

    def total_def(self):
        return random.randint(self.def_range[0], self.def_range[1])

    def heal(self, potion_name):
        if self.potions.get(potion_name, 0) <= 0:
            print("You don't have that potion.")
            return False
        heal_amt = POTIONS[potion_name]["heal"]
        self.potions[potion_name] -= 1
        old_hp = self.hp
        self.hp = min(self.max_hp, self.hp + heal_amt)
        print(f"{self.name} used {potion_name} and healed {self.hp - old_hp} HP (now {self.hp}/{self.max_hp})")
        return True

    def gain_xp(self, amt):
        self.xp += amt
        print(f"Gained {amt} XP. ({self.xp}/{self.xp_to_level} to next level)")
        while self.xp >= self.xp_to_level:
            self.xp -= self.xp_to_level
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.atk_range = (self.atk_range[0], self.atk_range[1] + 5)
        self.def_range = (self.def_range[0], self.def_range[1] + 5)
        self.xp_to_level = int(self.xp_to_level * 1.5)
        print_sep()
        print(f"*** LEVEL UP! You are now level {self.level} ***")
        print(f"Max HP increased to {self.max_hp}. ATK range now {self.atk_range}. DEF range now {self.def_range}.")
        print_sep()

    def show_stats(self):
        print_sep()
        print(f"Player: {self.name} | Level: {self.level} | XP: {self.xp}/{self.xp_to_level} | Gold: {self.gold}")
        print(f"HP: {self.hp}/{self.max_hp} | Weapon: {self.weapon['name']} (+{self.weapon['bonus']} ATK)")
        print(f"Potions: {self.potions}")
        print_sep()

class Enemy(Character):
    def __init__(self, level):
        hp = 50 + (level-1) * 20 + random.randint(0, 20)
        atk_high = min(10 + (level-1)*5, 40)
        def_high = min(10 + (level-1)*5, 40)
        super().__init__(f"Goblin L{level}", hp, (1, atk_high), (1, def_high))
        self.level = level
        self.xp_reward = 20 + level * 15
        self.gold_reward = 5 + level * 5


def compute_damage(attacker_atk, defender_def):
    rand_bonus = random.randint(0, 5)
    raw = attacker_atk - defender_def + rand_bonus
    return max(1, raw)

def attempt_critical(damage):
    if random.random() < 0.15:
        mult = random.uniform(1.3, 1.5)
        return int(damage * mult), True
    return damage, False

def player_turn(player, enemy):
    while True:
        print("\nChoose action:")
        print("1) Attack")
        print("2) Defend (reduce incoming damage in this turn)")
        print("3) Use Potion")
        print("4) Show Stats")
        action = input("Enter 1-4: ").strip()
        if action == "1":
            atk = player.total_atk()
            enemy_def = enemy.roll_def()
            dmg = compute_damage(atk, enemy_def)
            dmg, crit = attempt_critical(dmg)
            enemy.hp -= dmg
            print(f"You attack! ATK roll + weapon = {atk}. Enemy DEF roll = {enemy_def}. Damage dealt = {dmg}{' (CRITICAL!)' if crit else ''}. Enemy HP: {max(enemy.hp,0)}/{enemy.max_hp}")
            return "attack", dmg
        elif action == "2":
            print("You brace for impact. DEF increased this turn.")
            return "defend", 0
        elif action == "3":
            print("Potions:", player.potions)
            potion_choice = input("Enter potion name or press Enter to cancel: ").strip()
            if potion_choice in POTIONS:
                used = player.heal(potion_choice)
                if used:
                    return "potion", 0
            else:
                print("Invalid potion name.")
        elif action == "4":
            player.show_stats()
        else:
            print("Invalid input. Try again.")

def enemy_turn(player, enemy, player_defending):
    atk = enemy.roll_atk()
    pdef = player.total_def() if not player_defending else int(player.total_def() * 1.5)
    dmg = compute_damage(atk, pdef)
    dmg, crit = attempt_critical(dmg)
    player.hp -= dmg
    print(f"{enemy.name} attacks! Enemy ATK roll = {atk}. Your DEF roll = {pdef}. Damage taken = {dmg}{' (CRITICAL!)' if crit else ''}. Your HP: {max(player.hp,0)}/{player.max_hp}")
    return dmg


def shop(player):
    print_sep()
    print("Welcome to the Shop!")
    print(f"Gold: {player.gold}")
    for i, (pname, pdata) in enumerate(POTIONS.items(), start=1):
        print(f"{i}) {pname} - Heals {pdata['heal']} HP - Price {pdata['price']} gold")
    print("4) Exit Shop")
    choice = input("Choose item to buy (1-4): ").strip()
    if choice in ("1","2","3"):
        idx = int(choice)-1
        name = list(POTIONS.keys())[idx]
        price = POTIONS[name]["price"]
        if player.gold >= price:
            player.gold -= price
            player.potions[name] = player.potions.get(name,0) + 1
            print(f"Bought {name}. You now have {player.potions[name]}. Gold left: {player.gold}")
        else:
            print("Not enough gold.")
    else:
        print("Leaving shop.")
    print_sep()

def main():
    print("=== Python RPG Challenge — The Dungeon Adventure ===")
    name = input("Enter player name: ").strip() or "Hero"
    player = Player(name)

    level_counter = 1
    while True:
        print_sep()
        print(f"Entering dungeon floor {level_counter}. Enemy level roughly {level_counter}.")
        
        if level_counter % 5 == 0:
            print("A Boss approaches!")
            enemy = Enemy(level_counter + 2)
            enemy.name = f"Boss L{level_counter}"
            enemy.max_hp += 80
            enemy.hp = enemy.max_hp
            enemy.xp_reward += 100
            enemy.gold_reward += 50
        else:
            enemy = Enemy(level_counter)

        print(f"Enemy: {enemy.name} | HP: {enemy.hp} | ATK range: {enemy.atk_range} | DEF range: {enemy.def_range}")
        pause()

        while player.hp > 0 and enemy.hp > 0:
            print(f"\n[{player.name} HP: {player.hp}/{player.max_hp}]  vs  [{enemy.name} HP: {enemy.hp}/{enemy.max_hp}]")
            action, _ = player_turn(player, enemy)
            player_defending = (action == "defend")
            if enemy.hp <= 0:
                break
            enemy_turn(player, enemy, player_defending)
            if player.hp <= 0:
                break

        if player.hp <= 0:
            print("You have been defeated...")
            print(f"You reached level {player.level} with {player.xp} XP and {player.gold} gold.")
            print("Game Over.")
            break
        else:
            print(f"\n{enemy.name} defeated!")
            xp_gain = enemy.xp_reward
            gold_gain = enemy.gold_reward + random.randint(0,10)
            player.gain_xp(xp_gain)
            player.gold += gold_gain
            print(f"You looted {gold_gain} gold. Current gold: {player.gold}")
            drop = roll_drop()
            print(f"Drop found: {drop['name']} ({drop['rarity']}) - +{drop['bonus']} ATK")
            equip = input(f"Do you want to equip {drop['name']}? (y/n): ").strip().lower()
            if equip == "y":
                print(f"Equipped {drop['name']}. Weapon bonus is now +{drop['bonus']}")
                player.weapon = {"name": drop['name'], "bonus": drop['bonus']}
            else:
                print("You left the item.")
            
            player.show_stats()
            choice = input("Do you want to visit the shop? (y/n): ").strip().lower()
            if choice == "y":
                shop(player)

            level_counter += 1
            print("Resting... HP restored to max by 30% between fights.")
            heal_amount = int(player.max_hp * 0.30)
            player.hp = min(player.max_hp, player.hp + heal_amount)
            print(f"HP restored by {heal_amount}. Current HP: {player.hp}/{player.max_hp}")
            pause()

if __name__ == "__main__":
    main()
