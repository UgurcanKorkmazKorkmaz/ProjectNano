import random

#deze functie leest een moeilijkheid file als een list en returned hieruit een willekeurige woord.
def randomwoord(moeilijkheid):
    file = open(f'Difficultys/{moeilijkheid}.txt')
    woorden = file.read().split()
    file.close()

    woord = random.choice(woorden)
    return woord

#deze functie returned de pogingen voor de gekozen difficulty.
def pogingen(moeilijkheid):
    pogingen = {"easy":2 , "normal":3 , "hard":4 , "impossible":5}
    return pogingen[moeilijkheid]

def galgje_game(moeilijkheid):
    totaal_pogingen = pogingen(moeilijkheid)
    woord = randomwoord(moeilijkheid)
    pogingcounter = 0
    print(woord)
    geradenletterscorrect = []
    geradenlettersfout = []

    while totaal_pogingen > pogingcounter:
        poging = input('Wat raad je?: ')
        if poging in (geradenletterscorrect or geradenlettersfout):
            print('Je hebt deze letter al geraden!')
        elif poging == woord:
            print(f'Goedzo! {woord} was het woord. '
                  f'Je had nog {totaal_pogingen - pogingcounter} pogingen over.')
            break
        elif poging in woord:
            print(f'Goedzo! {poging} zit in het woord.\n')
            geradenletterscorrect.append(poging)
        else:
            print(f'Jammer, {poging} zit niet in het woord.'
                  f'Je hebt nog {totaal_pogingen - pogingcounter - 1} poging(en) over')
            pogingcounter += 1
            geradenlettersfout.append(poging)

galgje_game(input('Welke moeilijkheid kies je?: '))