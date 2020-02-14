import random
import sys

try: color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

class warrior:
    name = ""
    level = 1
    maxHealth = 10
    health = 10
    strength = 2
    experience = 0
    maxExperience = 30
    numberOfPotions = 0
    energy = 10
    totalEnergy = 10
    equippedWeapon = None
    equippedArmour = None
    weaponsInventory = []
    armourInventory = []
class monster1:
    level = 1
    health = 1
    strength = 1
    experienceGiven = 1
class monster2:
    level = 1
    health = 10
    strength = 1
    experienceGiven = 1
class bossMonster:
    level = 7
    health = 20
    strength = 7
    experienceGiven = 50
    
def continue1():
    continue1 = input()

def levelUp(warrior):
    warrior.level += 1
    if (warrior.health >= (warrior.maxHealth - 5)):
        warrior.heatlh = warrior.maxHealth
    else:
        warrior.health += 5
    warrior.experience -= newPlayer.maxExperience
    warrior.maxExperience += 10
    if (warrior.energy >= (warrior.totalEnergy - 5)):
        warrior.energy = warrior.totalEnergy
    else:
        warrior.energy += 5
    print("Level: " + str(warrior.level))
    print("HP: " + str(warrior.health))
    print("Strength: " + str(warrior.strength))
    print("Experience: " + str(warrior.experience))
    print("Energy: " + str(warrior.energy))
    print("Max Health: " + str(warrior.maxHealth))
    print("Total Energy: " + str(warrior.totalEnergy))
    print("You have two level points. What stat would you like to increase?")
    while True:
        choice1 = input("'Max Health', 'Strength', or 'Total Energy': ")
        if (choice1 == "Max Health"):
            warrior.maxHealth += 5
            break
        elif (choice1 == "Strength"):
            warrior.strength += 1
            break
        elif (choice1 == "Total Energy"):
            warrior.totalEnergy += 5
            break
    print("Level: " + str(warrior.level))
    print("HP: " + str(warrior.health))
    print("Strength: " + str(warrior.strength))
    print("Experience: " + str(warrior.experience))
    print("Energy: " + str(warrior.energy))
    print("Max Health: " + str(warrior.maxHealth))
    print("Total Energy: " + str(warrior.totalEnergy))
    print("You have one level points. What stat would you like to increase?")
    while True:
        choice2 = input("'Max Health', 'Strength', or 'Total Energy': ")
        if (choice2 == "Max Health"):
            warrior.maxHealth += 5
            break
        elif (choice2 == "Strength"):
            warrior.strength += 1
            break
        elif (choice2 == "Total Energy"):
            warrior.totalEnergy += 5
            break
    print("Level: " + str(warrior.level))
    print("HP: " + str(warrior.health))
    print("Strength: " + str(warrior.strength))
    print("Experience: " + str(warrior.experience))
    print("Energy: " + str(warrior.energy))
    print("Max Health: " + str(warrior.maxHealth))
    print("Total Energy: " + str(warrior.totalEnergy))
    
def stats(warrior):
    print("Level: " + str(warrior.level))
    print("HP: " + str(warrior.health))
    print("Strength: " + str(warrior.strength))
    print("Experience: " + str(warrior.experience))
    print("To Next Level: " + str(warrior.maxExperience - warrior.experience))
    print("Number of Potions: " + str(warrior.numberOfPotions))
    print("Energy: " + str(warrior.energy))
    print("Equipped Weapon: " + str(warrior.equippedWeapon))
    print("Equipped Armour: " + str(warrior.equippedArmour))
    print("Weapons Inventory: " + str(warrior.weaponsInventory))
    print("Armour Inventory: " + str(warrior.armourInventory))
def battle(monster1):
    if (monster1.level <= 2):
        monster1.health = 2
        monster1.strength = 1
        monster1.experienceGiven = 10
    elif (monster1.level <= 4):
        monster1.health = 4
        monster1.strength = 3
        monster1.experienceGiven = 15
    elif (monster1.level >= 5):
        monster1.health = 5
        monster1.strength = 4
        monster1.experienceGiven = 20
    while (monster1.health >= 0):
        print("Monster's Health: " + str(monster1.health), "Monster's Strength: " + str(monster1.strength), sep = " and ")
        print("\n")
        print("Your Health: " + str(newPlayer.health), "Your Strength: " + str(newPlayer.strength), "Number of Potions: " + str(newPlayer.numberOfPotions), sep = ", ")
        print("\n")
        print("What would you like to do?")
        move = input("'Attack', 'Drink a Potion', or 'Flee': ")
        print("\n")
        if (move == "Attack"):
            monster1.health -= newPlayer.strength
        elif (move == "Flee"):
            chance = random.randint(1, 10)
            if (chance <= 4):
                print("You have successfully run away!")
            return "Flee"
        elif (move == "Drink a Potion"):
            if (newPlayer.numberOfPotions > 0):
                if (newPlayer.health >= newPlayer.maxHealth - 5):
                    newPlayer.health = newPlayer.maxHealth
                else:
                    newPlayer.health += 5
                newPlayer.numberOfPotions -= 1
            else:
                print("You reach into your bag, but you don't find anything.")
        newPlayer.energy -= 1
        if (monster1.health > 0):
            newPlayer.health -= monster1.strength
            if (newPlayer.health <= 0):
                  return "Dead"
        else:
            return "Win"

def battle2(monster2):
    if (monster2.level <= 9):
        monster2.health = 7
        monster2.strength = 4
        monster2.experienceGiven = 15
    elif (monster2.level <= 13):
        monster2.health = 9
        monster2.strength = 6
        monster2.experienceGiven = 20
    elif (monster2.level <= 15):
        monster2.health = 10
        monster2.strength = 8
        monster2.experienceGiven = 25
    while (monster2.health >= 0):
        print("Monster's Health: " + str(monster2.health), "Monster's Strength: " + str(monster2.strength), sep = " and ")
        print("\n")
        print("Your Health: " + str(newPlayer.health), "Your Strength: " + str(newPlayer.strength), "Number of Potions: " + str(newPlayer.numberOfPotions), sep = ", ")
        print("\n")
        print("What would you like to do?")
        move = input("'Attack', 'Drink a Potion', or 'Flee': ")
        if (move == "Attack"):
            monster2.health -= newPlayer.strength
        elif (move == "Flee"):
            chance = random.randint(1, 10)
            if (chance <= 4):
                print("You have successfully run away!")
            return "Flee"
        elif (move == "Drink a Potion"):
            if (newPlayer.numberOfPotions > 0):
                newPlayer.health += 5
                newPlayer.numberOfPotions -= 1
            else:
                print("You reach into your bag, but you don't find anything.")
        newPlayer.energy -= 1
        if (monster2.health > 0):
            newPlayer.health -= monster1.strength
            if (newPlayer.health <= 0):
                  return "Dead"
        else:
            return "Win"


        
color.write("King: Hello Adventurer! What is your name? \n","STRING")  
newPlayer = warrior()
newPlayer.name = input("Enter Your Name: ")
color.write("King: Well, " + newPlayer.name + ", welcome to Pexon, the realm of Humans. \n","STRING")
print("\n")
color.write("King: Here, all people coexist peacefully. However, recently, there has been a problem. \n","STRING")
print("\n")
color.write("King: You see, the king of the Shadow realm has been ordering his army to invade our land.  \n","STRING")
print("\n")
color.write("King: That is why we have been enlisting the help of adventurers, like you, to help us defeat him. You will help us, won't you?  \n","STRING")
while True:
    answer = input("Type Yes or No: ")
    if (answer == "Yes"):
        break
    elif (answer == "No"):
        color.write("Please reconsider...  \n","STRING")
    else:
        color.write("Is that a yes or a no?  \n","STRING")
color.write("King: Great. Then, let's get you ready.  \n","STRING")
continue1()
color.write("King: First, let me tell you your stats. Right now, you are lvl. 1 and have 10 HP.  \n","STRING")
print("\n")
color.write("King: Different monsters do different amounts of damage, so you must be careful not to lose all your health.  \n","STRING")
continue1()
color.write("King: If your health is ever too low, then you can drink a potion, which will restore 5 health points.  \n","STRING")
continue1()
color.write("King: You currently have 2 strength, which means that every hit you land on an enemy will do 2 damage.  \n","STRING")
print("\n")
color.write("King: As you progress, you will get stronger, allowing you to defeat monsters easier.  \n","STRING")
continue1()
color.write("King: Finally, before you go I would like to give something to you:  \n","STRING")
print("\n")
print("You got a potion!")
newPlayer.numberOfPotions += 1
continue1()
color.write("King: That is all the wisdom I can give to you. Good luck, Adventurer " + newPlayer.name + ".  \n","STRING")
continue1()
color.write("As you leave the kingdom and enter the forest, the trees begin to block the light of the castle until you find yourself surrounded by almost complete darkness. \n","KEYWORD")
continue1()
print("Now you have three options: 'Explore,' 'Sleep,' and 'Look At Stats'.")
print("\n")
print("The 'Explore' option allows you to move, which will allow you to fight monsters and pick up items.")
print("\n")
print("The 'Sleep' option allows you to rest and heal, but be careful because a monster might creep up on you while you are sleeping.")
print("\n")
print("And the 'Look At Stats' option allows you to check you character's information, like HP, strength, and level.")
print("\n")
print("What would you like to do?")
while (newPlayer.level < 5):
    if (newPlayer.energy <= 0):
        print("You don't have energy. You need to sleep.")
        newPlayer.energy += 3
        num = random.randint(0, 50)
        if (num < 15):
            newGoblin = monster1()
            newGoblin.level = random.randint(1, 5)
            print("You have encountered a level " + str(newGoblin.level) + " goblin!")
            continue1()
            result = battle(newGoblin)
            if (result == "Win"):
                newPlayer.experience += newGoblin.experienceGiven
                print("You have gained " + str(newGoblin.experienceGiven) + " experience!")
                if (newPlayer.experience >= newPlayer.maxExperience):
                    print("You have leveled up!")
                    levelUp(newPlayer)
            elif (result == "Flee"):
                newPlayer.experience += 5
                print("You have gained 5 experience!")
                if (newPlayer.experience >= newPlayer.maxExperience):
                    print("You have leveled up!")
                    levelUp(newPlayer)
            elif (result == "Dead"):
                print("You have died.")
                sys.exit()
        elif (num < 30):
            newDemon = monster1()
            newDemon.level = random.randint(1, 5)
            print("You have encountered a level " + str(newDemon.level) + " Class C Demon!")
            continue1()
            result = battle(newDemon)
            if (result == "Win"):
                newPlayer.experience += newDemon.experienceGiven
                print("You have gained " + str(newDemon.experienceGiven) + " experience!")
                if (newPlayer.experience >= newPlayer.maxExperience):
                    print("You have leveled up!")
                    levelUp(newPlayer)
            elif (result == "Flee"):
                newPlayer.experience += 5
                print("You have gained 5 experience!")
                if (newPlayer.experience >= newPlayer.maxExperience):
                    print("You have leveled up!")
                    levelUp(newPlayer)
            elif (result == "Dead"):
                print("You have died.")
                sys.exit()
        elif (num <= 50):
            print("A good rest has restored your health by 3 HP.")
            if (newPlayer.health >= newPlayer.maxHealth - 2):
                newPlayer.health = newPlayer.maxHealth
            else:
                newPlayer.health += 3
    else:
        action = input("Action: ")
        if (action == "Explore"):
            num = random.randint(0, 100)
            if (num < 30):
                print("Nothing has been seen...")
                newPlayer.energy -= 1
            elif (num < 50):
                newGoblin = monster1()
                newGoblin.level = random.randint(1, 5)
                print("You have encountered a level " + str(newGoblin.level) + " goblin!")
                continue1()
                result = battle(newGoblin)
                if (result == "Win"):
                    newPlayer.experience += newGoblin.experienceGiven
                    print("You have gained " + str(newGoblin.experienceGiven) + " experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Flee"):
                    newPlayer.experience += 5
                    print("You have gained 5 experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(warrior)
                elif (result == "Dead"):
                    print("You have died.")
                    sys.exit()
            elif (num < 70):
                print("You have found a potion!")
                newPlayer.numberOfPotions += 1
                newPlayer.energy -= 1
            elif (num < 90):
                newDemon = monster1()
                newDemon.level = random.randint(1, 5)
                print("You have encountered a level " + str(newDemon.level) + " Class C Demon!")
                continue1()
                result = battle(newDemon)
                if (result == "Win"):
                    newPlayer.experience += newDemon.experienceGiven
                    print("You have gained " + str(newDemon.experienceGiven) + " experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Flee"):
                    newPlayer.experience += 5
                    print("You have gained 5 experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Dead"):
                    print("You have died.")
                    sys.exit()
            elif (num <= 100):
                print("You found a good spot to train. You have gained experience!")
                newPlayer.experience += 5
                print("You have gained 5 experience!")
                newPlayer.energy -= 1
                if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
        if (action == "Sleep"):
            num = random.randint(0, 50)
            newPlayer.energy += 3
            if (num < 15):
                newGoblin = monster1()
                newGoblin.level = random.randint(1, 5)
                print("You have encountered a level " + str(newGoblin.level) + " goblin!")
                continue1()
                result = battle(newGoblin)
                if (result == "Win"):
                    newPlayer.experience += newGoblin.experienceGiven
                    print("You have gained " + str(newGoblin.experienceGiven) + " experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Flee"):
                    newPlayer.experience += 5
                    print("You have gained 5 experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Dead"):
                    print("You have died.")
                    sys.exit()
            elif (num < 30):
                newDemon = monster1()
                newDemon.level = random.randint(1, 5)
                print("You have encountered a level " + str(newDemon.level) + " Class C Demon!")
                continue1()
                result = battle(newDemon)
                if (result == "Win"):
                    newPlayer.experience += newDemon.experienceGiven
                    print("You have gained " + str(newDemon.experienceGiven) + " experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Flee"):
                    newPlayer.experience += 5
                    print("You have gained 5 experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Dead"):
                    print("You have died.")
                    sys.exit()
            elif (num <= 50):
                print("A good rest has restored your health by 3 HP.")
                if (newPlayer.health >= newPlayer.maxHealth - 2):
                    newPlayer.health = newPlayer.maxHealth
                else:
                    newPlayer.health += 3
        if (action == "Look At Stats"):
            stats(newPlayer)

while (newPlayer.level == 5):
    color.write("After venturing through the forest outside the for a while, you come out the other end and find yourself in front of a huge cave. \n","KEYWORD")
    continue1()
    color.write("As you walk toward the entrance, you hear an ground-shaking roar. When you turn around, you see a giant ogre walk out of the forest. \n","KEYWORD")
    continue1()
    color.write("Ogre: What do you think you are doing? You are not allowed to pass through there.")
    continue1()
    color.write(newPlayer.name + ": I have to. I have been sent by the human king to defeat the king of the shadow realm.")
    continue1()
    color.write("Ogre: Very well. But, if you wish to pass, you must first defeat me!")
    ogre = bossMonster()
    while (ogre.health >= 0):
        print("Monster's Health: " + str(ogre.health), "Monster's Strength: " + str(ogre.strength), sep = " and ")
        print("Your Health: " + str(newPlayer.health), "Your Strength: " + str(newPlayer.strength), "Number of Potions: " + str(newPlayer.numberOfPotions), sep = ", ")
        print("What would you like to do?")
        move = input("'Attack' or 'Drink a Potion': ")
        if (move == "Attack"):
            ogre.health -= newPlayer.strength
        elif (move == "Drink a Potion"):
            if (newPlayer.numberOfPotions > 0):
                newPlayer.health += 5
                newPlayer.numberOfPotions -= 1
            else:
                print("You reach into your bag, but you don't find anything.")
        if (ogre.health > 0):
            newPlayer.health -= ogre.strength
            if (newPlayer.health <= 0):
                  print("You have died.")
                  sys.exit()
        newPlayer.energy -= 1
    newPlayer.experience += ogre.experienceGiven
    color.write("Ogre: I see that you have the strength of a true warrior. As a prize, I give you my club. This weapon increases your strength by 2.")
    continue1()
    color.write("Ogre: You might need this to handle what is coming.")
    continue1()
    color.write("You have received the Club.")
    newPlayer.weaponsInventory.append("Club")
    print("Would you like to equip this weapon?")
    equip = input("'Yes' or 'No': ")
    if (equip == "Yes"):
        i = newPlayer.weaponsInventory.index("Club")
        newPlayer.equippedWeapon = newPlayer.weaponsInventory[i]
        del newPlayer.weaponsInventory[i]
        print("You have equipped the " + str(newPlayer.equippedWeapon))
        newPlayer.strength += 2
    else:
        print("The Club has been placed in you inventory.")
    color.write("You continue through the cave until you see an exit. Upon exiting, you find yourself at the entrance of a labryinth. \n","KEYWORD")
    continue1()
    color.write("Having just defeated the ogre and coming one step closer to the king of the shadow realm, you continue through the maze.\n","KEYWORD")
    continue1()
    break

print("You now have the option to equip and remove weapons and armor. Anything item that is not equipped can be found in your inventory.")
continue1()
print("If you would like to equip or remove and item, simply type 'Equip' or 'Remove' followed by the name of the item.")
while (newPlayer.level < 10):
    if (newPlayer.energy <= 0):
        print("You don't have energy. You need to sleep.")
        newPlayer.energy += 3
        num = random.randint(0, 50)
        if (num < 15):
            newWarrior = monster2()
            newWarrior.level = random.randint(5, 15)
            print("You have encountered a level " + str(newWarrior.level) + " Fire Warrior!")
            continue1()
            result = battle2(newWarrior)
            if (result == "Win"):
                newPlayer.experience += newWarrior.experienceGiven
                print("You have gained " + str(newWarrior.experienceGiven) + " experience!")
                if (newPlayer.experience >= newPlayer.maxExperience):
                    print("You have leveled up!")
                    levelUp(newPlayer)
            elif (result == "Flee"):
                newPlayer.experience += 5
                print("You have gained 5 experience!")
                if (newPlayer.experience >= newPlayer.maxExperience):
                    print("You have leveled up!")
                    levelUp(newPlayer)
            elif (result == "Dead"):
                print("You have died.")
                sys.exit()
        elif (num < 30):
            newDragon = monster1()
            newDragon.level = random.randint(5, 15)
            print("You have encountered a level " + str(newDragon.level) + " baby Dragon!")
            continue1()
            result = battle2(newDragon)
            if (result == "Win"):
                newPlayer.experience += newDragon.experienceGiven
                print("You have gained " + str(newDragon.experienceGiven) + " experience!")
                if (newPlayer.experience >= newPlayer.maxExperience):
                    print("You have leveled up!")
                    levelUp(newPlayer)
            elif (result == "Flee"):
                newPlayer.experience += 5
                print("You have gained 5 experience!")
                if (newPlayer.experience >= newPlayer.maxExperience):
                    print("You have leveled up!")
                    levelUp(newPlayer)
            elif (result == "Dead"):
                print("You have died.")
                sys.exit()
        elif (num <= 50):
            print("A good rest has restored your health by 3 HP.")
            if (newPlayer.health >= newPlayer.maxHealth - 2):
                newPlayer.health = newPlayer.maxHealth
            else:
                newPlayer.health += 3
    else:
        action = input("Action: ")
        if (action == "Explore"):
            num = random.randint(0, 100)
            if (num < 30):
                print("Nothing has been seen...")
                newPlayer.energy -= 1
            elif (num < 50):
                newWarrior = monster2()
                newWarrior.level = random.randint(5, 15)
                print("You have encountered a level " + str(newWarrior.level) + " Fire Warrior!")
                continue1()
                result = battle2(newWarrior)
                if (result == "Win"):
                    newPlayer.experience += newWarrior.experienceGiven
                    print("You have gained " + str(newWarrior.experienceGiven) + " experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Flee"):
                    newPlayer.experience += 5
                    print("You have gained 5 experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Dead"):
                    print("You have died.")
                    sys.exit()
            elif (num < 70):
                print("You have found a potion!")
                newPlayer.numberOfPotions += 1
                newPlayer.energy -= 1
            elif (num < 90):
                newDragon = monster2()
                newDragon.level = random.randint(5, 15)
                print("You have encountered a level " + str(newDragon.level) + " baby Dragon!")
                continue1()
                result = battle2(newDragon)
                if (result == "Win"):
                    newPlayer.experience += newDragon.experienceGiven
                    print("You have gained " + str(newDragon.experienceGiven) + " experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Flee"):
                    newPlayer.experience += 5
                    print("You have gained 5 experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Dead"):
                    print("You have died.")
                    sys.exit()
            elif (num <= 100):
                print("You found a good spot to train. You have gained experience!")
                newPlayer.experience += 5
                print("You have gained 5 experience!")
                newPlayer.energy -= 1
                if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
        if (action == "Sleep"):
            num = random.randint(0, 50)
            newPlayer.energy += 3
            if (num < 15):
                newWarrior = monster2()
                newWarrior.level = random.randint(5, 15)
                print("You have encountered a level " + str(newWarrior.level) + " Fire Warrior!")
                continue1()
                result = battle2(newWarrior)
                if (result == "Win"):
                    newPlayer.experience += newWarrior.experienceGiven
                    print("You have gained " + str(newWarrior.experienceGiven) + " experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Flee"):
                    newPlayer.experience += 5
                    print("You have gained 5 experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Dead"):
                    print("You have died.")
                    sys.exit()
            elif (num < 30):
                newDragon = monster1()
                newDragon.level = random.randint(5, 15)
                print("You have encountered a level " + str(newDragon.level) + " baby Dragon!")
                continue1()
                result = battle2(newDragon)
                if (result == "Win"):
                    newPlayer.experience += newDragon.experienceGiven
                    print("You have gained " + str(newDragon.experienceGiven) + " experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Flee"):
                    newPlayer.experience += 5
                    print("You have gained 5 experience!")
                    if (newPlayer.experience >= newPlayer.maxExperience):
                        print("You have leveled up!")
                        levelUp(newPlayer)
                elif (result == "Dead"):
                    print("You have died.")
                    sys.exit()
            elif (num <= 50):
                print("A good rest has restored your health by 3 HP.")
                if (newPlayer.health >= newPlayer.maxHealth - 2):
                    newPlayer.health = newPlayer.maxHealth
                else:
                    newPlayer.health += 3
        if (action == "Look At Stats"):
            stats(newPlayer)
        if (action == "Remove"):
            print("What would you like to place in the inventory?")
            answer = input("'Weapon', 'Armour', or 'Cancel': ")
            if (answer == "Weapon"):
                if (newPlayer.equippedWeapon == ""):
                    print("You do not have any weapon equipped.")
                else:
                    if (newPlayer.equippedWeapon == "Club"):
                        newPlayer.strength -= 2
                    newPlayer.weaponsInventory.append(newPlayer.equippedWeapon)
                    print("Your " + str(newPlayer.equippedWeapon) + " has been placed in your inventory.")
                    newPlayer.equippedWeapon = None
            if (answer == "Armour"):
                if (newPlayer.equippedArmour == ""):
                    print("You do not have any armour equipped.")
                else:
                    newPlayer.armourInventory.append(newPlayer.equippedArmour)
                    print("Your " + str(newPlayer.equippedArmour) + " has been placed in your inventory.")
                    newPlayer.equippedArmour = None
        if (action == "Equip"):
            if (len(newPlayer.weaponsInventory) == 0 and len(newPlayer.armourInventory) == 0):
                print("You have no items that you can equip at this time.")
            else:
                print("Would you like to equip a weapon or armour?")
                answer = input("'Weapon', 'Armour', or 'Cancel': ")
                if (answer == "Weapon"):
                    print("Weapons Inventory: " + str(newPlayer.weaponsInventory))
                    print("Which weapon would you like to equip?")
                    answer = input("Name of Weapon: ")
                    i = newPlayer.weaponsInventory.index(answer)
                    if (newPlayer.equippedWeapon != None):
                        newPlayer.weaponsInventory.append(newPlayer.equippedWeapon)
                    newPlayer.equippedWeapon = newPlayer.weaponsInventory[i]
                    del newPlayer.weaponsInventory[i]
                    print("You have equipped the " + str(newPlayer.equippedWeapon))
                    if (answer == "Club"):
                        newPlayer.strength += 2
                if (answer == "Armour"):
                    print("Armour Inventory: " + str(newPlayer.armourInventory))
                    print("Which armour would you like to equip?")
                    answer = input("Name of Armour: ")
                    i = newPlayer.armourInventory.index(answer)
                    if (newPlayer.equippedArmour != None):
                        newPlayer.armourInventory.append(newPlayer.equippedArmour)
                    newPlayer.equippedArmour = newPlayer.armourInventory[i]
                    del newPlayer.armourInventory[i]
                    print("You have equipped the " + str(newPlayer.equippedArmour))
while True:
    Dragon = bossMonster()
    bossMonster.level = 20 
    
                    

        
            


                
