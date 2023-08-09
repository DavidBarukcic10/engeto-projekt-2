'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: David Barukčić
email: d.barukcic@seznam.cz
discord: David Barukcic
'''


import random

def generate_secret_number():
    digits = random.sample(range(0, 10), 4)  # Generuje 4 unikátní číslice (včetně nuly)
    if digits[0] == 0:  # Zajišťuje, že číslo nezačíná nulou
        digits[0], digits[1] = digits[1], digits[0]
    return ''.join(map(str, digits))

def evaluate_guess(secret_number, guess):
    bulls = 0
    cows = 0
    for i in range(len(secret_number)):
        if secret_number[i] == guess[i]:  # Porovnává číslice na stejných pozicích
            bulls += 1
        elif secret_number[i] in guess:  # Pokud číslo není na správném místě, ale je obsaženo v hádaném čísle
            cows += 1
    return bulls, cows

def validate_input(guess):
    if not guess.isdigit():  # Ověřuje, zda je vstup číslo
        return False
    if len(guess) != 4:  # Ověřuje, zda je vstup čtyřmístný
        return False
    if len(set(guess)) != 4:  # Ověřuje, zda jsou všechny číslice unikátní
        return False
    if guess[0] == '0':  # Zadání začínající nulou je neplatné
        return False  
    return True

# Úvodní text
print("Hi there!")
print("-" * 50)
print("I've generated a random 4-digit number for you.")
print("Let's play a bulls and cows game.")
print("-" * 50)

secret_number = generate_secret_number()
num_guesses = 0

while True:
    guess = input("Enter a number: ")
    num_guesses += 1

    if not validate_input(guess):  # Ověřuje správnost vstupu
        print("Invalid input.")
        print("-" * 50)
        continue

    bulls, cows = evaluate_guess(secret_number, guess)  # Ohodnocení hádaného čísla

    if bulls == 4:  # Pokud jsou všechny čtyři číslice uhodnuty na správných pozicích
        print("Correct, you've guessed the right number!")
        print(f"In {num_guesses} guesses!")
        break

    print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")
    print("-" * 50)

# Hodnocení výkonu hráče
if num_guesses <= 3:
    print("That's amazing!")
elif num_guesses <= 6:
    print("That's great!")
elif num_guesses <= 10:
    print("That's good!")
else:
    print("Better luck next time!")