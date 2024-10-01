# Nano

Dit is mijn _Project Nano_, met erin:
- Raad het getal
- Galgje
- Main Menu

Ik zal hieronder mijn progressie, aanpassingen in mijn code en bronnen met timestamps toelichten:


**30-09-2024:**
- Mijn Main Menu functie doet het niet meer omdat de py.file waaruit ik de functie wil callen 
- niet in dezelfde directory ziet. Hiervoor zal ik informatie zoeken over import en from.
- Ik wil meer comments toevoegen in Main Menu en Galgje moet ook comments krijgen.

-Ik had galgje al af maar de vereiste blijkt dus dat het uit een file gelezen moet worden. Ik zal 
-moeten ombouwen zodat hij i.p.v. een list in de file afleest dat dit gebeurd met een list vanuit een file.

Ik heb deze link: https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file
gebruikt om te kijken hoe ik functies oproep die in een andere directory zitten. Ik heb deze informatie bij
main menu.py toegepast.

**01-10-2024:**

Ik heb de Main Menu aangepast + galgje aangepast zodat je een moeilijkheid kan invoeren en de bijhorende file
met woorden zal gaan openen. Deze zijn easy, normal , hard, impossible.
Als je iets anders invoert krijg je wel een error. Ik zou dit kunnen voorkomen met een While loop, maar
ik wil proberen om een exception toe te kunnen passen die wij bij PROG 9 gaan leren.

Ik heb voor galgje de open() functie aangepast. Eerst verwees ik naar de difficultys directory, maar omdat
ik de app via main menu wil runnen moet ik ook het galgje directory verwijzen. Dit heb ik gedaan.
Galgje werkt nu op het minimale. Ik ga het nu uitwerkend door moeilijkheden toe te voegen en/of een api
wat random woorden van het internet afhaalt. 



