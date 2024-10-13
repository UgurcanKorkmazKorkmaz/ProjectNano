import random
import datetime
import json

#highscore functie wat de naam, aantal pogingen, random getal en de tijd noteert in een json file als de user de game
#succesvol heeft behaald.
def highscore(naam , aantal_pogingen , getal):
    huidige_tijd = datetime.datetime.now()
    tijd_highscore = huidige_tijd.strftime('%d-%m-%Y , %H:%M')
    highscore_speler = {
        naam: {
            'getal':getal,
            'poging':aantal_pogingen,
            'tijd':tijd_highscore
        }
    }
    #Er wordt geprobeerd een json file te openen en te lezen. De data word geupdate met de speler van deze sessie.
    try:
        with open('Raad_het_getal/highscoresRHG.json', 'r') as json_file:
            alle_highscores_spelers = json.load(json_file)
        alle_highscores_spelers.update(highscore_speler)

        # Daarna wordt de updated data geschreven in dezelfde json file.
        with open('Raad_het_getal/highscoresRHG.json' , 'w') as json_file:
            json.dump(alle_highscores_spelers , json_file , indent=2)

    #als de json file nog niet bestaat wordt deze aangemaakt. Alleen de data van de user van deze sessie wordt geschreven
    except FileNotFoundError:
        with open('Raad_het_getal/highscoresRHG.json' , 'w') as json_file:
            json.dump(highscore_speler , json_file , indent=2)

#for loop die naloopt of het getal geraden is of dat de pogingen op zijn.
def game_getalraden(aantal_pogingen):

    #We willen het uiteraard niet te makkelijk maken. Als de user meer dan 50% van de getallen kan raden dmv pogingen,
    #word er een ValueError geraised waardoor de app weer terugkeert naar het main menu.
    if aantal_pogingen > 7:
        raise ValueError

    #de naam van de gebruiker wordt opgeslagen in een variabele.
    naam = input('Wat is je naam?: ')

    # verkrijg een random getal
    getal = random.randrange(1, 11)

    #het spel wordt uitgelegd
    print(f"\nHet getal ligt tussen 1 en 10!\n"
          f"Je hebt {aantal_pogingen} pogingen om het juiste getal te raden. Veel succes!\n")

    #for loop die bij elke loopinstantie naloopt of het juiste cijfer geraden is of niet.
    for pogingen in range(1 , aantal_pogingen + 1):

        #input van de user om het juiste getal te kunnen raden
        user_gok = int(input("Wat is jouw gok?: "))

        #als het random getal gelijk is aan de user input, wordt de for loop verbroken en de highscore func. aangeroepen
        if user_gok == getal:
            print(f"Gefeliciteerd! , je hebt gewonnen! Het getal was: {getal}\n")
            highscore(naam , pogingen , getal)
            break

        #mocht de user geen pogingen over hebben zal er een game over screen geprint worden.
        elif pogingen == aantal_pogingen:
            print(f"Sorry je hebt verloren, GAME OVER. Het getal was: {getal}\n")

        #als de user input != aan het random getal maar de user heeft nog wel pogingen over.
        else:
            print(f"Fout, probeer opnieuw. Je hebt nog {aantal_pogingen - pogingen} poging(en) over\n")









