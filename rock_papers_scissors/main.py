import random


class RPS:
    def throw(self):
        choices = ["rock", "papers", "scissors"]
        choice = random.choice(choices)
        return choice


scores = {
    "player": 0,
    "comp": 0
}

p2 = RPS()
print("Welcome to the game!!")
while True:
    p2choice = p2.throw()
    p1choice = input("choose rock papers or scissors: ").lower()
    if p1choice == "exit":
        break
    print("> "+p2choice)
    if (p1choice == "rock" and p2choice == "rock") or (p1choice == "papers" and p2choice == "papers") or (p1choice == "scissors" and p2choice == "scissors"):
        print("draw!")
    elif (p1choice == "rock" and p2choice == "papers") or (p1choice == "papers" and p2choice == "scissors") or (p1choice == "scissors" and p2choice == "rock"):
        print("you loose!")
        scores["comp"] += 1
    elif (p1choice == "rock" and p2choice == "scissors") or (p1choice == "papers" and p2choice == "rock") or (p1choice == "scissors" and p2choice == "papers"):
        print("you win!")
        scores["player"] += 1
    else:
        print("Please choose rock, papers or scissors!")
    print(scores)
print("Thanks for playing!")
