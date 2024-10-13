from Raad_het_getal.RaadHetGetal import game_getalraden
from Galgje.Galgje import galgje_game
import json

#while loop wat continue checkt welke optie er gekozen is. Als er iets anders word ingevoerd dan de gegeven opties,
#breekt de loop NIET. Er zit een break if statement in de loop om deze te kunnen breken.
#de lower string functie is gebruikt om te voorkomen dat als de user Exit intypt dat de while loop deze herkent.
while True:

    # dit is een menu waarmee de gebruiker een spel uit kan kiezen
    print(f'Welkom bij de Kordir Appstore!'
          f'Je hebt de volgende keuzes:\n'
          f'    1. Raad het getal\n'
          f'    2. Galgje\n'
          f'    3. Highscores bekijken\n'
          f'    4. Verlaat de appstore\n'
          f'Voer aub het getal in van de gewenste applicatie\n'
          )
    game = input("Welke applicatie wil je?: ")

    # introductie van het spel raad het getal door de functie op te roepen
    if game == "1":
        print('\nWelkom tot het spel "Raad het getal!"')

        #als de datatype anders is dan int wordt de ValueError op deze manier behandelt.
        try:
            game_getalraden(int(input('Je hebt maximaal 7 pogingen.\n'
                                      'Hoeveel pogingen wil je?: ')))
        except ValueError:
            print('\nOops, er ging iets fout. Weetje zeker dat je invoer klopt?\n')

    # introductie van het spel galgje. Roept ook de functie op.
    elif game == "2":
        print(f'\nWelkom bij Galgje! Je hebt de keuze voor de volgende 4 moeilijkheiden.\n'
              f'    1. easy\n'
              f'    2. normal\n'
              f'    3. hard\n'
              f'    4. impossible\n'
              f'Voer aub de gewenste moeilijkheid in.')

        #in de func. galgje_game word er gebruik gemaakt van een dict. . Om te voorkomen dat de programma stopt vanwege
        #een nonexistent key, wordt de KeyError als een print behandelt.
        try:
            galgje_game(input('Welke moelijkheid wil je?: '))
        except KeyError:
            print('\nOops, er ging iets mis. Je hebt geen bestaande moeilijkheid ingevoerd.\n')

    #leest vanuit een json file opgeslagen highscores op van spelers.
    elif game == '3':
        highscore_game = input("\nEr zijn highscores voor de volgende spellen.\n"
                               "1. Raad het getal\n"
                               "2. Galgje.\n"
                               "Voer aub het getal in van de game om de highscores te kunnen zien: ")

        #deze block code is voor de game Raad het getal
        if highscore_game == '1':

            #we proberen een file te opening in dir Raad_het_getal. Als deze bestaat en geldige json data bevat wordt
            #er dmv een for-loop een print uitgedraaid van alle spelers en hun data.
            try:
                with open('Raad_het_getal/highscores.json', 'r') as json_file:
                    data = json.load(json_file)
                    for speler in data:
                        print(f'\nSpeler {speler}\n. '
                              f'Getal         = {data[speler]['getal']}\n. '
                              f'Poging        = {data[speler]['poging']}\n. '
                              f'Tijd en Datum = {data[speler]['tijd']}\n')

                    #als er nog geen highscores zijn wordt dit aangegeven.
                    if data == {}:
                        print('\nEr zijn nog geen highscores voor deze game. Tijd om er 1 te maken!\n')

            #mocht de json file niet bestaan dan zorgt onderstaande code ervoor dat de file wordt aangemaakt.
            except FileNotFoundError:
                with open('Raad_het_getal/highscores.json', 'w') as json_file:
                    json.dump({}, json_file, indent=2)

        #deze block code is voor de game Galgje
        elif highscore_game == '2':

            # we proberen een file te opening in dir Raad_het_getal. Als deze bestaat en geldige json data bevat wordt
            # er dmv een for-loop een print uitgedraaid van alle spelers en hun data.
            try:
                with open('Galgje/highscores.json' , 'r') as json_file:
                    data = json.load(json_file)
                    for speler in data:
                        print(f'\nSpeler {speler}\n. '
                              f'Woord                = {data[speler]['random woord']}\n. '
                              f'Aantal pogingen over = {data[speler]['pogingen over']}\n. '
                              f'Difficulty           = {data[speler]['difficulty']}\n. '
                              f'Tijd en Datum        = {data[speler]['tijd']}\n')

                    # als er nog geen highscores zijn wordt dit aangegeven.
                    if data == {}:
                        print('\nEr zijn nog geen highscores voor deze game. Tijd om er 1 te maken!\n')

            # mocht de json file niet bestaan dan zorgt onderstaande code ervoor dat de file wordt aangemaakt.
            except FileNotFoundError:
                with open('Galgje/highscores.json', 'w') as json_file:
                    json.dump({} , json_file , indent=2)

    # Dit is de if statement waar break wordt toegepast om de loop uit te gaan.
    elif game == '4':
        print('Appstore is afgesloten. Vaarwel!')
        break

    else:
    # als er iets anders wordt ingetypt dan de opgegeven opties wordt de loop hierdoor niet verbroken.
    # ik hoef hierdoor niet meerdere exceptions uit te draaien.
        print("\nOops, er ging iets fouts. Deze command is niet bekend! Probeer het opnieuw\n")



