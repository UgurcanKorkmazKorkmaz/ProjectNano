import random
import datetime
import json

#deze functie leest een file met woorden, verschillend in moeilijkheid, af en returnt 1 enkele random woord.
def randomwoord(moeilijkheid):
    file = open(f'Galgje/Difficultys/{moeilijkheid}.txt')
    woorden = file.read().split()
    file.close()

    woord = random.choice(woorden)
    return woord


#deze functie returned de pogingen voor de gekozen difficulty.
def pogingen(moeilijkheid):
    pogingen = {"easy":8 , "normal": 9, "hard": 12 , "impossible": 14}
    return pogingen[moeilijkheid]

#highscore functie die de naam van de speler, het woord, het aantal pogingen, de moeilijkheid en de tijd in een json
#file noteert.
def highscore(woord , pogingen_over , naam, moeilijkheid):
    huidige_tijd = datetime.datetime.now()
    tijd_highscore = huidige_tijd.strftime('%d-%m-%Y , %H:%M')
    highscore_speler = {
        naam: {
            'random woord': woord ,
            "pogingen over": pogingen_over ,
            'tijd': tijd_highscore,
            'difficulty': moeilijkheid
        }
    }

    # Er wordt geprobeerd een json file te openen en te lezen. De data word geupdate met de speler van deze sessie.
    try:
        with open('Galgje/highscoresGalgje.json', 'r') as json_file:
            alle_highscores_spelers = json.load(json_file)

        alle_highscores_spelers.update(highscore_speler)

        # Daarna wordt de updated data geschreven in dezelfde json file.
        with open('Galgje/highscoresGalgje.json' , 'w') as json_file:
            json.dump(alle_highscores_spelers , json_file , indent=2)

    # als de json file nog niet bestaat wordt deze aangemaakt. Alleen de data van de user van deze sessie wordt geschreven
    except FileNotFoundError:
        with open('Galgje/highscoresGalgje.json' , 'w') as json_file:
            json.dump(highscore_speler , json_file , indent=2)

#dit is het spel waar de functies hierboven allemaal aangeroepen worden.
def galgje_game(moeilijkheid):
    #variablen afkomstig uit de bovenstaande functies.
    totaal_pogingen = pogingen(moeilijkheid)
    woord = randomwoord(moeilijkheid)

    #de user krijgt zijn levenspunten te zien, naast zijn pogingen. Beide zijn hetzelfde.
    levenspuntenlst = ['-'] * totaal_pogingen

    #hierdoor kan de user zien op welke plek het geraden letter zich bevind.
    legewoordlst = ['_'] * len(woord)

    #de geraden letters worden in deze list opgeslagen
    geradenletters = []

    pogingcounter = 0

    #de naam van de speler wordt in een variable opgeslagen
    naam = input('Wat is jouw naam?: ')
    print(f'Het woord is {len(woord)} letters lang. Je hebt {totaal_pogingen} pogingen. Veel succes!')

    #while loop die werkt totdat de totale pogingen niet meer groter is dan de pogingen waar de user zich bevind.
    while totaal_pogingen > pogingcounter:

        #user input voor een letter.
        poging = input('Wat raad je?: ')

        #mocht de user meerdere letters proberen te raden worden deze 1 voor 1 dmv een for loop gecheckt of deze zich in
        #het woord bevinden.
        for letter_poging in poging:

            #zorgt ervoor dat de user geen whitespaces kan invoeren
            if letter_poging == '' or letter_poging == ' ':
                print('Je hebt niks ingevoerd.')
                continue

            #de letters die geraden zijn kunnen niet opnieuw geraden worden.
            elif letter_poging in geradenletters:
                print(f'Je hebt {letter_poging} al geraden!')

            #als de letter zich in het woord bevind, wordt dit aangegeven en krijgt de user te zien op welke plek deze
            #letter zich bevind. De letter wordt dan toegevoegd aan de al geraden letters.
            elif letter_poging in woord:
                print(f'Goedzo! {letter_poging} zit in het woord.')
                for index in range(len(woord)):
                    if woord[index] == letter_poging:
                        legewoordlst[index] = letter_poging
                        geradenletters.append(letter_poging)

            #als de letter niet in het woord is wordt dit aangegeven, verliest de user een leven en wordt de letter
            #toegevoegd aan de al geraden letters.
            else:
                levenspuntenlst[pogingcounter] = 'x'
                pogingcounter += 1
                print(f'Jammer, {letter_poging} zit niet in het woord.'
                      f'Je hebt nog {totaal_pogingen - pogingcounter} poging(en) over')
                geradenletters.append(letter_poging)

        #Of het geraden letter of een levenspunt wordt bijgewerkt. Hierdoor is er bij de volgende iteratie te zien
        #of de user een leven heeft verloren of waar het geraden letter zich bevind.
        levenspunten = ''.join(levenspuntenlst)
        legewoord = ''.join(legewoordlst)
        print(f'{levenspunten} : {legewoord}\n')

        #als de pogingen op zijn, wordt alleen de while loop verbroken. We willen ook een game over screen hebben.
        if pogingcounter == totaal_pogingen:
            print(f'GAME OVER. Het woord was {woord}\n')

        #als de user alle letters heeft geraden hoeft zij niet het woord apart te raden door onderstaande code.
        #de highscore functie wordt aangeroepen om de spelerdata op te slaan.
        elif '_' not in legewoord:
            highscore(woord , (totaal_pogingen - pogingcounter) , naam , moeilijkheid)
            print(f'Goedzo! {woord} is het woord. '
                  f'Je had nog {totaal_pogingen - pogingcounter} poging(en) over.\n')
            break





