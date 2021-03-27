import random
import termcolor2

true_char = []
false_char = []

names = ["sadegh", "ali", "reza", "mohsen", "sara", "mina", "mohammad", "ZAHRA", "HAMED", "SINA", "IMAN", "SADRA"]
name = random.choice(names)
name = name.lower()
score = len(name)
while True:
    for i in range(len(name)):
        if name[i] in true_char:
            print(name[i], end="")
        else:
            print("_", end="")

    char = input("\nEnter Character: ").lower()

    if char in name:
        true_char.append(char)
    else:
        false_char.append(char)
        print(termcolor2.colored(f"Is Not: {false_char}", color="red"))
        score -= 1
        print(f"Score: {score}")
        if score == 0:
            break
    if len(name) == len(true_char):
        print(termcolor2.colored(f"GoodJub {name}" , color="green"))
        break
