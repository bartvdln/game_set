# game_set
Code van Jorik en Barthil voor het spel set.

We gaan het spel Set namaken in pygame en spelen tegen een computer. 
Dit doen we in de volgende volgorde:
1. Schrijf een klasse voor SET-kaarten, die in ieder geval vergelijking van de eigenschappen ondersteunt. Ook kun je een manier van visualiseren inbouwen.
2, Schrijf een algoritme die controleert of een gegeven verzameling van 3 kaarten een SET is.
3. Schrijf een algoritme om uit een gegeven verzameling van 12 kaarten alle mogelijke sets te vinden.
4. Schrijf ook een algoritme die één set vindt.
5. Bouw een spel om deze algoritmen heen. Je programma moet 12 kaarten op het scherm tonen (genummerd) en de gebruiker vragen om een SET in te voeren (bijvoorbeeld 1, 5, 10 als kaarten 1, 5 en 10 samen een set vormen). Als de gebruiker na een gegeven tijd nog geen SET heeft gevonden en de computer heeft er wel een, dan krijgt de computer een punt. Je kunt de moeilijkheid van het spel aanpassen door deze tijd korter of langer te maken. Als er na een vooraf bepaalde tijd helemaal geen set is gevonden, verwijder dan de bovenste 3 kaarten en vul aan met 3 nieuwe kaarten. Je mag de python module pygame gebruiken.

Laten we allereerst onze klassen definieren. 
Iedere kaart uit het spel Set heeft vier eigenschappen: kleur, vorm, opvulling en aantal. Elke eigenschap heeft drie verschillende opties.
Kleuren: rood (r), groen (g) en paars (p). 
Vormen: ruit (r), ovaal (o) en golf (g). 
Opvulling: vol (v), gestreept (g) en leeg (l). 
Aantal: 1, 2 en 3. 
We kunnen een kaart beschrijven door de eerste letter van de optie te gebruiken in volgorde kleur-vorm-opvulling-aantal. 
Voorbeelden van kaarten zijn dan: rol1, grv2 en pgl3.
Op deze manier kunnen we gemakkelijk per letter een hele eigenschap afleiden. 

De code kun je in de map 'code' vinden. Hier staat een code om een set te controleren, om sets te vinden en om een random set daaruit te halen.

We bouwen ons spel in Pygame. De link naar dit spel staat in onze groepsomschrijving. 
