import pygame
import random
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 

pygame.init()

(width, height) = (1330, 500)
background = (160, 200, 150)
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)
yellow = ((255,255,0))
white = ((255, 255, 255))
blue = ((0,0,255))

font_nummer = pygame.font.SysFont("arialblack", 15)
zwart = ((0, 0, 0))
kaarten_nummer = []
sets = [0]
display = pygame.display.set_mode((width, height))
display.fill(background)
pygame.display.set_caption('Sets')

kleur = ["g", "r", "p"]
vorm = ["g", "o", "r"]
vulling = ["v", "g", "l"]
aantal = ["1", "2", "3"]
kaarten = []
for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            for l in range(0, 3):
                kaarten.append(list(kleur[i] + vorm[j] + vulling[k] + aantal[l]))

random.shuffle(kaarten)

kaarten_display = []
kaarten_beeld = [kaarten[0], kaarten[1], kaarten[2], kaarten[3], kaarten[4], kaarten[5], kaarten[6], kaarten[7], kaarten[8], kaarten[9], kaarten[10], kaarten[11]]


def draw_cards():
    kaarten_display = []
    
    for i in range(0, 12):
        kaart = pygame.image.load(''.join(kaarten_beeld[i])+".gif").convert()
        kaarten_display.append(kaart)
        display.blit(kaarten_display[i], (10 + 110*(i), 20))
        pygame.display.flip() 

def draw_texts(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    display.blit(img, (x, y))
    

def controleer_set(plaats1, plaats2, plaats3):
        kaart1 = kaarten_beeld[plaats1]
        kaart2 = kaarten_beeld[plaats2]
        kaart3 = kaarten_beeld[plaats3]
        if ((kaart1[0] == kaart2[0] == kaart3[0]) or (kaart1[0] != kaart2[0] != kaart3[0])) and ((kaart1[1] == kaart2[1] == kaart3[1]) or (kaart1[1] != kaart2[1] != kaart3[1])) and ((kaart1[2] == kaart2[2] == kaart3[2]) or (kaart1[2] != kaart2[2] != kaart3[2])) and ((kaart1[3] == kaart2[3] == kaart3[3]) or (kaart1[3] != kaart2[3] != kaart3[3])):
            draw_texts("Set!", font, zwart, 500, 100)
            kaarten_beeld[plaats1] = kaarten[12]
            kaarten.pop(12)
        
            kaarten_beeld[plaats2] = kaarten[12]
            kaarten.pop(12)
            
            kaarten_beeld[plaats3] = kaarten[12]
            kaarten.pop(12)
            
            
            display.fill(background)
            draw_cards()
            select_cards.clear()
            pygame.display.flip()
            
            for i in range(0, 12):
                getal = i
                draw_texts(fr"{i + 1}", font_nummer, zwart, 15 + 110*i, 25)
        
        else:
            draw_texts("Geen set", font, zwart, 565, 240)
            select_cards.clear()
            for i in range(0, 12):
                pygame.draw.rect(display, white, [10 + 110*i, 20, 100, 200], 2)

                


run = True
game_start = False

if game_start == False:
    draw_texts("druk op SPATIE om te beginnen", font, TEXT_COL, 280, 100)


select_cards = []

while run:
    
    
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                display.fill(background)
                draw_cards()
                
                for i in range(0, 12):
                    pygame.draw.rect(display, white, [10 + 110*i, 20, 100, 200], 2)

                for i in range(0, 12):
                    getal = i
                    draw_texts(fr"{i + 1}", font_nummer, zwart, 15 + 110*i, 25)
                game_start = True
                
                
                for i in range(len(kaarten_display)):
                    for j in range(i+1, len(kaarten_display)):
                        for k in range(j+1, len(kaarten_display)):
                            if (kaarten_display[i][0] == kaarten_display[j][0] == kaarten_display[k][0] or kaarten_display[i][0] != kaarten_display[j][0] != kaarten_display[k][0] != kaarten_display[i][0]) and (kaarten_display[i][1] == kaarten_display[j][1] == kaarten_display[k][1] or kaarten_display[i][1] != kaarten_display[j][1] != kaarten_display[k][1] != kaarten_display[i][1]) and (kaarten_display[i][2] == kaarten_display[j][2] == kaarten_display[k][2] or kaarten_display[i][2] != kaarten_display[j][2] != kaarten_display[k][2] != kaarten_display[i][2]) and (kaarten_display[i][3] == kaarten_display[j][3] == kaarten_display[k][3] or kaarten_display[i][3] != kaarten_display[j][3] != kaarten_display[k][3] != kaarten_display[i][3]):
                                sets.append([kaarten_display[i], kaarten_display[j], kaarten_display[k]])

                if len(sets) == 0:
                        kaarten_beeld[0] = kaarten[12]
                        kaarten.pop[12]
                        kaarten_beeld[1] = kaarten[12]
                        kaarten.pop[12]
                        kaarten_beeld[2] = kaarten[12]
                        kaarten.pop[12]
                        
                        display.fill(background)
                        draw_cards()
                        pygame.display.flip()
                            
                
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            for i in range(0, 12):
            
                if 10 +110*i < x < 110 + 110*i  and  20 < y < 220:
                    if i in select_cards:
                        select_cards.remove(i)
                        pygame.draw.rect(display, white, [10 + 110*i, 20, 100, 200], 2)
                    else:
                        select_cards.append(i)
                        pygame.draw.rect(display, blue, [10 + 110*i, 20, 100, 200], 2)
                        
                
                        if len(select_cards) == 3:
                            controleer_set(select_cards[0], select_cards[1], select_cards[2])
                        
        
    
            
    if event.type == pygame.QUIT:
        run = False
    
    pygame.display.flip()
    
pygame.quit()
