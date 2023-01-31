import pygame
import random
import os
import time
os.chdir(os.path.dirname(os.path.abspath(__file__))) # pakt kaarten uit de goede map

pygame.init()

# instellingen display
(width, height) = (1330, 500)


# kleuren voor tijdens het spel
background = (160, 200, 150)
TEXT_COL = (255, 255, 255)
yellow = ((255,255,0))
white = ((255, 255, 255))
blue = ((0,0,255))
zwart = ((0, 0, 0))


# lijsten die we gaan gebruiken
kaarten_display = []    # verwijst naar de kaarten in de map
select_cards = []       # drie kaarten die je selecteert voor een mogelijke set
score = 0               # beginscore speler
score_computer = 0
computer_move = pygame.event.Event(pygame.USEREVENT)
computer_tijd = 30 * 1000     # tijd voor de computer in milliseconden


# lettertypes
font = pygame.font.SysFont("arialblack", 40)
font_nummer = pygame.font.SysFont("arialblack", 15)
font_win = pygame.font.SysFont("comicsansms", 128)


# extra instellingen display
display = pygame.display.set_mode((width, height))
display.fill(background)
pygame.display.set_caption('Sets')


# alle mogelijkheden voor combinaties van kaarten
kleur = ["g", "r", "p"]
vorm = ["g", "o", "r"]
vulling = ["v", "g", "l"]
aantal = ["1", "2", "3"]
kaarten = [] # de pot als het ware
for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            for l in range(0, 3):
                kaarten.append(list(kleur[i] + vorm[j] + vulling[k] + aantal[l]))

random.shuffle(kaarten) # functie om kaarten te schudden


# de 12 kaarten op beeld
kaarten_beeld = []
for i in range(0,12):
    kaarten_beeld.append(kaarten[0])
    kaarten.pop(0)

# functie om tekst te laten zien op display
def draw_texts(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    display.blit(img, (x, y))

# functie om kaarten uit kaarten_beeld weer te geven op het scherm
def draw_cards():
    display.fill(background)
    kaarten_display = []

    for i in range(0, len(kaarten_beeld)):
        kaarten_display.append(pygame.image.load(''.join(kaarten_beeld[i])+".gif").convert())
        display.blit(kaarten_display[i], (10 + 110*(i), 20))
        draw_texts(fr"{i + 1}", font_nummer, zwart, 15 + 110*i, 25) # teken nummers op kaarten
        pygame.display.flip()


# functie om te controleren of de 3 geselecteerde kaarten een set zijn
def controleer_set(kaart1, kaart2, kaart3):
    set = [kaart1, kaart2, kaart3] # de potentiele set
    for i in range(0, 4):
        if set[0][i] == set[1][i] and set[0][i] == set[2][i]:
            continue
        if set[0][i] != set[1][i] and set[0][i] != set[2][i] and set[1][i] != set[2][i]:
            continue
        return False
    return True


def mogelijke_sets():
    sets = []
    if len(kaarten_beeld) == 0:
        return []
    for i in range(0, len(kaarten_beeld)):
        for j in range(i+1, len(kaarten_beeld)):
            for k in range(j+1, len(kaarten_beeld)):
                if controleer_set(kaarten_beeld[i], kaarten_beeld[j], kaarten_beeld[k]):
                    sets.append([kaarten_beeld[i], kaarten_beeld[j], kaarten_beeld[k]])
    return sets

def vervang_kaart(kaart):
    kaarten_beeld.remove(kaart)
    if len(kaarten) > 0:
        kaarten_beeld.append(kaarten[0])
        kaarten.pop(0)
    print("Cards left: " + str(len(kaarten)) + " Cards on the board: " + str(len(kaarten_beeld)))

def game_over():
    time.sleep(1)
    display.fill(background)
    draw_cards()
    if score > score_computer:
        draw_texts("YOU WIN", font_win, white, 200, 220)
    elif score_computer > score:
        draw_texts("YOU LOSE", font_win, white, 200, 220)
    else:
        draw_texts("GELIJKSPEL", font_win, white, 200, 220)
    draw_score()
    time.sleep(10)

def draw_score():
    draw_texts("Score: " + str(score) + " - " + str(score_computer), font, white, 200, 400)
    pygame.display.flip()

# beginwaarden
run = True
game_start = False

if game_start == False:
    draw_texts("Druk op de spatiebalk om te beginnen", font, TEXT_COL, 280, 100)   # startscherm
pygame.time.set_timer(computer_move, computer_tijd, loops=1) # over 10 seconden doet de computer een zet
# gameloop

while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:     # game beginnen na het indrukken van spatiebalk
                draw_cards()

                # witte kaders rondom de kaarten
                for i in range(0, 12):
                    pygame.draw.rect(display, white, [10 + 110*i, 20, 100, 200], 2)

                # de kaarten nummeren
                for i in range(0, len(kaarten_beeld)):
                    draw_texts(fr"{i + 1}", font_nummer, zwart, 15 + 110*i, 25)
                game_start = True

        # kaarten selecteerbaar maken en in de select_cards lijst zetten
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            for i in range(0, 12):
                # zorgt ervoor dat je de kaart selecteert die je aanklikt
                if 10 +110*i < x < 110 + 110*i  and  20 < y < 220:
                    if kaarten_beeld[i] in select_cards:
                        select_cards.remove(kaarten_beeld[i])
                        pygame.draw.rect(display, white, [10 + 110*i, 20, 100, 200], 2)
                    else:
                        select_cards.append(kaarten_beeld[i])
                        pygame.draw.rect(display, blue, [10 + 110*i, 20, 100, 200], 2)

                        #3 geselecteerde kaarten controleren als set
                        if len(select_cards) == 3:
                            if controleer_set(select_cards[0], select_cards[1], select_cards[2]):
                                for i in range(0, 3):
                                    vervang_kaart(select_cards[i])
                                select_cards.clear()
                                score += 1
                                if len(mogelijke_sets()) == 0: # wat als er geen sets mogelijk zijn
                                    if len(kaarten) == 0: # geen kaarten meer in de pot, game over
                                        run = False
                                        game_over()
                                    else: # voeg kaarten toe uit de pot
                                        for i in range(0, 3):
                                            kaarten_beeld.append(kaarten[0])
                                            kaarten.pop(0)

                                draw_cards()
                                draw_score()
                                pygame.time.set_timer(computer_move, computer_tijd, loops=1)

                            else: # kaarten vormen geen set
                                draw_texts("Geen set", font, zwart, 565, 240)
                                select_cards.clear()
                                for i in range(0, 12):
                                    pygame.draw.rect(display, white, [10 + 110*i, 20, 100, 200], 2)
        if event.type == pygame.USEREVENT:
            set = mogelijke_sets()[0] # aan het eind van elke zet wordt gecontroleerd of er sets zijn, hier hoeft dat niet
            print(set)
            print(controleer_set(set[0], set[1], set[2]))
            print(kaarten_beeld.index(set[0]))
            print(kaarten_beeld.index(set[1]))
            print(kaarten_beeld.index(set[2]))

            for i in range(0, 3):
                pygame.draw.rect(display, blue, [10 + 110*(kaarten_beeld.index(set[i])), 20, 100, 200], 2)
                pygame.display.flip()
                #time.sleep(0.5)
            #time.sleep(2)    # code om de computerzet te zien
            for i in range(0, 3):
                vervang_kaart(set[i])
            score_computer += 1
            if len(mogelijke_sets()) == 0: # wat als er geen sets mogelijk zijn
                if len(kaarten) == 0: # geen kaarten meer in de pot, game over
                    run = False
                    game_over()
                else: # voeg kaarten toe uit de pot
                    for i in range(0, 3):
                        kaarten_beeld.append(kaarten[0])
                        kaarten.pop(0)

            draw_cards()
            draw_score()

            pygame.time.set_timer(computer_move, computer_tijd, loops=1)
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
