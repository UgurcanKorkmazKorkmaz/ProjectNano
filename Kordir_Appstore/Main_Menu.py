from Raad_het_getal.RaadHetGetal import game_getalraden
from Galgje.Galgje import galgje_game

#dit is een menu waarmee de gebruiker een spel uit kan kiezen
print('Welkom bij Kordir Appstore! Welke app wilt u opstarten?\n'
      '1: Raad het getal, bij dit spel raad je antwoorden.\n'
      '2: Galgje, bij dit spel ga je woorden raden\n'
      '3: Dit spel bestaat nog niet :/\n'
      '4: ???\n'
      'Exit: Ik wil uit de appstore\n'
      )

#while loop wat continue checkt welke optie er gekozen is. Als er iets anders word ingevoerd dan de gegeven opties,
#breekt de loop NIET. Er zit een break if statement in de loop om deze te kunnen breken.
#de lower string functie is gebruikt om te voorkomen dat als de user Exit intypt dat de while loop deze herkent.
while True:
    game = input("Welk spel wil je?: ").lower()
    # introductie van het spel galgje door de functie op te roepen
    if game == "1":
        print('welkom tot het spel "Raad het getal!"')
        game_getalraden(int(input('Hoeveel pogingen wil je? ')))
        break
    # introductie van het spel galgje door de functie op te roepen
    elif game == "2":
        galgje_game(input('Welke moelijkheid wil je?: '))
        print('Work in progress')
        break
    # Ik wil hier het dagboek gaan verwerken.
    elif game == '3':
        pass
    # Dit is de if statement waar break word toegepast om de loop uit te gaan.
    elif game == 'exit':
        print('Kordir appstore is afgesloten')
        break
    # Bijvoorbeeld voor dagboek of om de woorden van galgje aan te passen? WIP.
    elif game == 'admin':
        print('admin console?')
        break
    else:
    # als er iets anders word ingetypt dan de opgegeven opties word de loop hierdoor niet verbroken
        print("Dit is geen bekende programma. Probeer het opnieuw")


