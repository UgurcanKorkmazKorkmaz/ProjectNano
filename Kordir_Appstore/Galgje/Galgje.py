import random

easy = open("easy.txt")
normal = open("normal.txt")
hard = open("hard.txt")
impossible = open("impossible.txt")


print("Welkom tot galgje! Je kan kiezen tussen de volgende 4 moeilijkheden.\n "
      "Easy , Normal , Hard , Impossible")


def woordkieser(difficulty):
    difficulty = difficulty + ".txt"
    file = open(difficulty)
    lijstwoorden = file.readlines()
    lijstwoorden
    lst = []
    for woord in lijstwoorden:
        woord.split(" ")
        lst.append(woord)
        print(woord)
    print(lst)
    woord = random.choice(lst)


    return woord

def difficultysetter(difficulty):
   if difficulty == "Easy":
       aantalpogingen = 3
   elif difficulty == "Normal":
       aantalpogingen = 3
   elif difficulty == "Hard":
       aantalpogingen = 0
   elif difficulty == "Impossible":
       aantalpogingen = 0
   return aantalpogingen



def game_galgje(difficulty):
    woord = woordkieser(difficulty)
    aantalpogingen = difficultysetter(difficulty)
    while aantalpogingen < 6:
        poging = input(f"Je hebt {6 - aantalpogingen} kansen om letters te onthullen!"
                       f" Welke letter raad je?: ")
        if poging in woord:
            print(f"Ja! {poging} zit in het woord! Je kan nog {5 - aantalpogingen} letters onthullen")
            aantalpogingen += 1
        else:
            print(f"Nee! {poging} zit niet in het woord. Je kan nog {5 - aantalpogingen} letters onthullen!")
            aantalpogingen += 1
        if aantalpogingen == 6:
            pogingwoord = input("""
Tijd is om!
Wat is het woord?
                         """)
            if pogingwoord == woord:
                print(f"Goedzo! Het woord was {woord}")
            else:
                print(f"GAME OVER. Het woord was {woord}")
            break


game_galgje(input("Welke difficulty wil je?: "))











