import random

#for loop die naloopt of het getal geraden is of dat de pogingen op zijn.
def game_getalraden(aantal_pogingen):
    #We willen het uiteraard niet te makkelijk maken. Als de user meer dan 50% van de getallen kan raden dmv pogingen,
    #word er een ValueError geraised waardoor de app weer terugkeert naar het main menu.
    if aantal_pogingen > (10/2):
        raise ValueError
    # verkrijg een random getal
    getal = random.randrange(1, 11)
    print("Het getal ligt tussen 1 en 10!."
          "Je hebt " + str(aantal_pogingen) + " pogingen om het juiste getal te raden. Veel succes!")
    for pogingen in range(1 , aantal_pogingen + 1):
        USER_gok = int(input("Wat is jouw gok?: "))
        if USER_gok == getal:
            print("Gefeliciteerd! , je hebt gewonnen! Het getal was: " + str(getal))
            break
        elif pogingen == aantal_pogingen:
            print("Sorry je hebt verloren, GAME OVER. Het getal was: " + str(getal))
        else:
            print("Fout, probeer opnieuw. Je hebt nog " + str(aantal_pogingen - pogingen) + " poging(en) over")









