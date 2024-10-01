import random

#bepaald door een input van welke file er een random woord van gekozen word
def woord_kiezer(difficulty):
    file = open(f'Galgje/Difficultys/{difficulty}.txt')
    woorden = file.readlines()
    file.close()


    randomwoorden = []

    for woord in woorden:
        randomwoorden.append(woord)
    woord = random.choice(randomwoorden)
    return woord


#bepaald qua de moeilijkheidsgraad hoeveel pogingen de user heeft om het woord te raden
def aantal_pogingen(difficulty):
    #ik ga hier gebruik maken van een dictionary met als key de moeilijkheid en als value de aantal pogingen
    return

#main game van galgje, waar een user een willekeurig woord gekozen door woord_kiezer() kan raden.
def galgje_game(difficulty):
    woord = woord_kiezer(difficulty)
    pogingen = 1
    while True:
        poging = input('Wat raad je?: ')
        if poging == woord:
            print('Je hebt gewonnen!')
        elif pogingen == 2:
            print('Je hebt verloren')
            break
        else:
            pogingen += 1

#galgje_game(input('Welke moelijkheid wil je?: '))
















