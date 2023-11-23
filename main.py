import time
import numpy as np
import sys
print("1.Charizard")
print("2.Blastoise")
print("3.Venusaur")
print("4.Charmeleon")
print("5.Wartotle")
print("6.Ivysaur")
print("7.Charmander")
print("8.Squirtle")
print("9.Bulbasaur")

pokemon_1 = int(input("what is your pokemon: "))
pokemon_2 = int(input("what is the second pokemon: "))

# Delay printing

def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars


    def fight(self, Pokemon2):
        # Allow two pokemon to fight each other

        # Print fight information
        print("-----POKEMONE BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # Both are same type
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Pokemon2 is STRONG
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Pokemon2 is WEAK
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        # Now for the actual fighting...
        # Continue while pokemon still have health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                break

            # Pokemon2s turn

            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break

        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.\n")






if __name__ == '__main__':
    #Create Pokemon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK': 3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})


    if pokemon_1 == 1 and pokemon_2 == 1:
        Charizard.fight(Charizard)
    elif pokemon_1 == 1 and pokemon_2 == 2:
        Charizard.fight(Blastoise)
    elif pokemon_1 == 1 and pokemon_2 == 3:
        Charizard.fight(Venusaur)
    elif pokemon_1 == 1 and pokemon_2 == 4:
        Charizard.fight(Charmeleon)
    elif pokemon_1 == 1 and pokemon_2 == 5:
        Charizard.fight(Wartortle)
    elif pokemon_1 == 1 and pokemon_2 == 6:
        Charizard.fight(Ivysaur)
    elif pokemon_1 == 1 and pokemon_2 == 7:
        Charizard.fight(Charmander)
    elif pokemon_1 == 1 and pokemon_2 == 8:
        Charizard.fight(Squirtle)
    elif pokemon_1 == 1 and pokemon_2 == 9:
        Charizard.fight(Bulbasaur)

    if pokemon_1 == 2 and pokemon_2 == 1:
        Blastoise.fight(Charizard)
    elif pokemon_1 == 2 and pokemon_2 == 2:
        Blastoise.fight(Blastoise)
    elif pokemon_1 == 2 and pokemon_2 == 3:
        Blastoise.fight(Venusaur)
    elif pokemon_1 == 2 and pokemon_2 == 4:
        Blastoise.fight(Charmeleon)
    elif pokemon_1 == 2 and pokemon_2 == 5:
        Blastoise.fight(Wartortle)
    elif pokemon_1 == 2 and pokemon_2 == 6:
        Blastoise.fight(Ivysaur)
    elif pokemon_1 == 2 and pokemon_2 == 7:
        Blastoise.fight(Charmander)
    elif pokemon_1 == 2 and pokemon_2 == 8:
        Blastoise.fight(Squirtle)
    elif pokemon_1 == 2 and pokemon_2 == 9:
        Blastoise.fight(Bulbasaur)

    if pokemon_1 == 3 and pokemon_2 == 1:
        Venusaur.fight(Charizard)
    elif pokemon_1 == 3 and pokemon_2 == 2:
        Venusaur.fight(Blastoise)
    elif pokemon_1 == 3 and pokemon_2 == 3:
        Venusaur.fight(Venusaur)
    elif pokemon_1 == 3 and pokemon_2 == 4:
        Venusaur.fight(Charmeleon)
    elif pokemon_1 == 3 and pokemon_2 == 5:
        Venusaur.fight(Wartortle)
    elif pokemon_1 == 3 and pokemon_2 == 6:
        Venusaur.fight(Ivysaur)
    elif pokemon_1 == 3 and pokemon_2 == 7:
        Venusaur.fight(Charmander)
    elif pokemon_1 == 3 and pokemon_2 == 8:
        Venusaur.fight(Squirtle)
    elif pokemon_1 == 3 and pokemon_2 == 9:
        Venusaur.fight(Bulbasaur)

    if pokemon_1 == 4 and pokemon_2 == 1:
        Charmeleon.fight(Charizard)
    elif pokemon_1 == 4 and pokemon_2 == 2:
        Charmeleon.fight(Blastoise)
    elif pokemon_1 == 4 and pokemon_2 == 3:
        Charmeleon.fight(Venusaur)
    elif pokemon_1 == 4 and pokemon_2 == 4:
        Charmeleon.fight(Charmeleon)
    elif pokemon_1 == 4 and pokemon_2 == 5:
        Charmeleon.fight(Wartortle)
    elif pokemon_1 == 4 and pokemon_2 == 6:
        Charmeleon.fight(Ivysaur)
    elif pokemon_1 == 4 and pokemon_2 == 7:
        Charmeleon.fight(Charmander)
    elif pokemon_1 == 4 and pokemon_2 == 8:
        Charmeleon.fight(Squirtle)
    elif pokemon_1 == 4 and pokemon_2 == 9:
        Charmeleon.fight(Bulbasaur)

    if pokemon_1 == 5 and pokemon_2 == 1:
        Wartortle.fight(Charizard)
    elif pokemon_1 == 5 and pokemon_2 == 2:
        Wartortle.fight(Blastoise)
    elif pokemon_1 == 5 and pokemon_2 == 3:
        Wartortle.fight(Venusaur)
    elif pokemon_1 == 5 and pokemon_2 == 4:
        Wartortle.fight(Charmeleon)
    elif pokemon_1 == 5 and pokemon_2 == 5:
        Wartortle.fight(Wartortle)
    elif pokemon_1 == 5 and pokemon_2 == 6:
        Wartortle.fight(Ivysaur)
    elif pokemon_1 == 5 and pokemon_2 == 7:
        Wartortle.fight(Charmander)
    elif pokemon_1 == 5 and pokemon_2 == 8:
        Wartortle.fight(Squirtle)
    elif pokemon_1 == 5 and pokemon_2 == 9:
        Wartortle.fight(Bulbasaur)

    if pokemon_1 == 6 and pokemon_2 == 1:
        Ivysaur.fight(Charizard)
    elif pokemon_1 == 6 and pokemon_2 == 2:
        Ivysaur.fight(Blastoise)
    elif pokemon_1 == 6 and pokemon_2 == 3:
        Ivysaur.fight(Venusaur)
    elif pokemon_1 == 6 and pokemon_2 == 4:
        Ivysaur.fight(Charmeleon)
    elif pokemon_1 == 6 and pokemon_2 == 5:
        Ivysaur.fight(Wartortle)
    elif pokemon_1 == 6 and pokemon_2 == 6:
        Ivysaur.fight(Ivysaur)
    elif pokemon_1 == 6 and pokemon_2 == 7:
        Ivysaur.fight(Charmander)
    elif pokemon_1 == 6 and pokemon_2 == 8:
        Ivysaur.fight(Squirtle)
    elif pokemon_1 == 6 and pokemon_2 == 9:
        Ivysaur.fight(Bulbasaur)

    if pokemon_1 == 7 and pokemon_2 == 1:
        Charmander.fight(Charizard)
    elif pokemon_1 == 7 and pokemon_2 == 2:
        Charmander.fight(Blastoise)
    elif pokemon_1 == 7 and pokemon_2 == 3:
        Charmander.fight(Venusaur)
    elif pokemon_1 == 7 and pokemon_2 == 4:
        Charmander.fight(Charmeleon)
    elif pokemon_1 == 7 and pokemon_2 == 5:
        Charmander.fight(Wartortle)
    elif pokemon_1 == 7 and pokemon_2 == 6:
        Charmander.fight(Ivysaur)
    elif pokemon_1 == 7 and pokemon_2 == 7:
        Charmander.fight(Charmander)
    elif pokemon_1 == 7 and pokemon_2 == 8:
        Charmander.fight(Squirtle)
    elif pokemon_1 == 7 and pokemon_2 == 9:
        Charmander.fight(Bulbasaur)

    if pokemon_1 == 8 and pokemon_2 == 1:
        Squirtle.fight(Charizard)
    elif pokemon_1 == 8 and pokemon_2 == 2:
        Squirtle.fight(Blastoise)
    elif pokemon_1 == 8 and pokemon_2 == 3:
        Squirtle.fight(Venusaur)
    elif pokemon_1 == 8 and pokemon_2 == 4:
        Squirtle.fight(Charmeleon)
    elif pokemon_1 == 8 and pokemon_2 == 5:
        Squirtle.fight(Wartortle)
    elif pokemon_1 == 8 and pokemon_2 == 6:
        Squirtle.fight(Ivysaur)
    elif pokemon_1 == 8 and pokemon_2 == 7:
        Squirtle.fight(Charmander)
    elif pokemon_1 == 8 and pokemon_2 == 8:
        Squirtle.fight(Squirtle)
    elif pokemon_1 == 8 and pokemon_2 == 9:
        Squirtle.fight(Bulbasaur)

    if pokemon_1 == 9 and pokemon_2 == 1:
        Bulbasaur.fight(Charizard)
    elif pokemon_1 == 9 and pokemon_2 == 2:
        Bulbasaur.fight(Blastoise)
    elif pokemon_1 == 9 and pokemon_2 == 3:
        Bulbasaur.fight(Venusaur)
    elif pokemon_1 == 9 and pokemon_2 == 4:
        Bulbasaur.fight(Charmeleon)
    elif pokemon_1 == 9 and pokemon_2 == 5:
        Bulbasaur.fight(Wartortle)
    elif pokemon_1 == 9 and pokemon_2 == 6:
        Bulbasaur.fight(Ivysaur)
    elif pokemon_1 == 9 and pokemon_2 == 7:
        Bulbasaur.fight(Charmander)
    elif pokemon_1 == 9 and pokemon_2 == 8:
        Bulbasaur.fight(Squirtle)
    elif pokemon_1 == 9 and pokemon_2 == 9:
        Bulbasaur.fight(Bulbasaur)
