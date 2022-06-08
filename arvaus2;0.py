import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'arvaa numero 1 ja {x} väliltä: '))
        print(guess)
        if guess < random_number:
            print("väärin, oikea luku on suurempi: ")
        elif guess > random_number:
            print("väärin, oikea luku on pienempi: ")
    print(f'Jee, arvasit luvun {random_number} oikein!')

guess (10)