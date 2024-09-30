from Raad_het_getal import RaadHetGetal
from RaadHetGetal import game_getalraden
#from GALGJE import game_galgje

Game = input("Welk spel wil je?: ")
if Game == "Getal raden" :
    #Game introductie met een prompt voor het aantal gewenste pogingen.
    print('welkom tot het spel "Raad het getal!"')
    game_getalraden(int(input('Hoeveel pogingen wil je? ')))
elif Game == "Galgje":
    #game_galgje(input("Welke difficulty wil je?: "))
    pass
else:
    print("Dit is geen bekende GAME. Run het programma opnieuw")


