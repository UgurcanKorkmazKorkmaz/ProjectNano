import random

#for loop die naloopt of het getal geraden is of dat de pogingen op zijn.
def game_getalraden(aantal_pogingen):
    # verkrijg een random getal
    getal = random.randrange(1, 11)
    print("Je hebt " + str(aantal_pogingen) + " pogingen om het juiste getal te raden. Veel succes!")
    for pogingen in range(1 , aantal_pogingen + 1):
        USER_gok = int(input("Wat is jouw gok?: "))
        if USER_gok == getal:
            print("Gefeliciteerd! , je hebt gewonnen! Het getal was: " + str(getal))
            break
        elif pogingen == aantal_pogingen:
            print("Sorry je hebt verloren, GAME OVER. Het getal was: " + str(getal))
        else:
            print("Fout, probeer opnieuw. Je hebt nog " + str(aantal_pogingen - pogingen) + " poging(en) over")









