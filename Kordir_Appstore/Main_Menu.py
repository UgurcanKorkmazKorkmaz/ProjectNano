from Raad_het_getal.RaadHetGetal import game_getalraden
from Galgje.Galgje import galgje_game

#while loop wat continue checkt welke optie er gekozen is. Als er iets anders word ingevoerd dan de gegeven opties,
#breekt de loop NIET. Er zit een break if statement in de loop om deze te kunnen breken.
#de lower string functie is gebruikt om te voorkomen dat als de user Exit intypt dat de while loop deze herkent.
while True:
    # dit is een menu waarmee de gebruiker een spel uit kan kiezen
    print(f'Welkom bij de Kordir Appstore!'
          f'Je hebt de volgende keuzes:\n'
          f'    1. Raad het getal\n'
          f'    2. Galgje\n'
          f'    3. Verlaat de appstore\n'
          f'Voer aub het getal in van de gewenste applicatie'
          )
    game = input("\nWelk spel wil je?: ")
    # introductie van het spel galgje door de functie op te roepen
    if game == "1":
        print('welkom tot het spel "Raad het getal!"')
        try:
            game_getalraden(int(input('Hoeveel pogingen wil je? ')))
        except ValueError:
            print('Oops, er ging iets fout. Weetje zeker dat je invoer klopt?\n')

    # introductie van het spel galgje door de functie op te roepen
    elif game == "2":
        try:
            galgje_game(input('Welke moelijkheid wil je?: '))
        except ValueError:
            print('Oops, er ging iets fout. Weet je zeker dat je invoer klopt?')


    # Dit is de if statement waar break word toegepast om de loop uit te gaan.
    elif game == '3':
        print('Appstore is afgesloten. Vaarwel!')
        break
    else:
    # als er iets anders word ingetypt dan de opgegeven opties word de loop hierdoor niet verbroken
        print("Oops, er ging iets fouts. Deze command is niet bekend! Probeer het opnieuw\n")



