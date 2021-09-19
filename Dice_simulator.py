import random
no_of_remaning_chance = 0
print("Dice Rolling Game")
print("How many chance you need\n")
n=input()
while no_of_remaning_chance<int(n):
    roll_dice = input("Write start to roll the dice: ")
    if roll_dice == "start":
       posible_results = [1, 2, 3, 4, 5, 6]
       result = random.choice(posible_results)
       print("Result of dice rolling is : " + str(result))
       no_of_remaning_chance = no_of_remaning_chance + 1
