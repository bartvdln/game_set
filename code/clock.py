import pygame
import random
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 

pygame.init()

# display settings
(width, height) = (1330, 500)


# kleuren voor het spel
background = (160, 200, 150)
TEXT_COL = (255, 255, 255)
yellow = ((255,255,0))
white = ((255, 255, 255))
blue = ((0,0,255))
zwart = ((0, 0, 0))


#lijsten die we gaan gebruiken
kaarten_display = []    #kaarten display is een lijst die verwijst naar de kaarten in de map
select_cards = []       #drie kaarten die je selecteerd voor een mogelijkje set
sets = []               #alle mogelijke sets 
score = 0
score_speler = [score]

#lettertypen voor de tekst
font = pygame.font.SysFont("arialblack", 40)
font_nummer = pygame.font.SysFont("arialblack", 15)


#display instellingen
display = pygame.display.set_mode((width, height))
display.fill(background)
pygame.display.set_caption('Sets')


#alle mogelijkheden voor kaarten combinaties
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

random.shuffle(kaarten) #de kaarten schudden


#de 12 kaarten op beeld
kaarten_beeld = [kaarten[0], kaarten[1], kaarten[2], kaarten[3], kaarten[4], kaarten[5], kaarten[6], kaarten[7], kaarten[8], kaarten[9], kaarten[10], kaarten[11]]

#functie om kaarten te pakken en te weergeven op het scherm
def draw_cards():
    kaarten_display = []
    
    for i in range(0, 12):
        kaart = pygame.image.load(''.join(kaarten_beeld[i])+".gif").convert()
        kaarten_display.append(kaart)
        display.blit(kaarten_display[i], (10 + 110*(i), 20))
        pygame.display.flip() 

#functie om text te laten zien op display
def draw_texts(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    display.blit(img, (x, y))
   
#functie om te controlleren of de 3 geselecteerde kaarten een set zijn
def controleer_set(plaats1, plaats2, plaats3):
        kaart1 = kaarten_beeld[plaats1]
        kaart2 = kaarten_beeld[plaats2]
        kaart3 = kaarten_beeld[plaats3]
        if ((kaart1[0] == kaart2[0] == kaart3[0]) or (kaart1[0] != kaart2[0] != kaart3[0])) and ((kaart1[1] == kaart2[1] == kaart3[1]) or (kaart1[1] != kaart2[1] != kaart3[1])) and ((kaart1[2] == kaart2[2] == kaart3[2]) or (kaart1[2] != kaart2[2] != kaart3[2])) and ((kaart1[3] == kaart2[3] == kaart3[3]) or (kaart1[3] != kaart2[3] != kaart3[3])):
            kaarten_beeld[plaats1] = kaarten[12]
            kaarten.pop(12)
        
            kaarten_beeld[plaats2] = kaarten[12]
            kaarten.pop(12)
            
            kaarten_beeld[plaats3] = kaarten[12]
            kaarten.pop(12)
            #de lijst met alle mogelijke sets leefmaken
            sets.clear()
            score_speler[0] = score_speler[0] + 1
            #als er een set gevonden is de nieuwe kaarten weergeven
            display.fill(background)
            draw_texts("score speler: " + str(score_speler[0]), font, white, 20, 400)
            draw_cards()
            controleer_op_sets()
            select_cards.clear()
            pygame.display.flip()
            
            #nummeren van de kaarten
            for i in range(0, 12):
                getal = i
                draw_texts(fr"{i + 1}", font_nummer, zwart, 15 + 110*i, 25)
        
        #als de geselecteerde kaarten geen set is geef "geen set" op het scherm weer
        else:
            draw_texts("Geen set", font, zwart, 565, 240)
            select_cards.clear()
            for i in range(0, 12):
                pygame.draw.rect(display, white, [10 + 110*i, 20, 100, 200], 2)

def controleer_op_sets():              
        for i in range(0,12):
            for j in range(i+1, 12):
                for k in range(j+1, 12):
                    if (kaarten_beeld[i][0] == kaarten_beeld[j][0] == kaarten_beeld[k][0] or kaarten_beeld[i][0] != kaarten_beeld[j][0] != kaarten_beeld[k][0] != kaarten_beeld[i][0]) and (kaarten_beeld[i][1] == kaarten_beeld[j][1] == kaarten_beeld[k][1] or kaarten_beeld[i][1] != kaarten_beeld[j][1] != kaarten_beeld[k][1] != kaarten_beeld[i][1]) and (kaarten_beeld[i][2] == kaarten_beeld[j][2] == kaarten_beeld[k][2] or kaarten_beeld[i][2] != kaarten_beeld[j][2] != kaarten_beeld[k][2] != kaarten_beeld[i][2]) and (kaarten_beeld[i][3] == kaarten_beeld[j][3] == kaarten_beeld[k][3] or kaarten_beeld[i][3] != kaarten_beeld[j][3] != kaarten_beeld[k][3] != kaarten_beeld[i][3]):
                        sets.append([kaarten_beeld[i], kaarten_beeld[j], kaarten_beeld[k]])
                
        # 3 nieuwe kaarten pakken       
        if len(sets) == 0:
            kaarten_beeld[0] = kaarten[12]
            kaarten.pop[12]
            kaarten_beeld[1] = kaarten[12]
            kaarten.pop[12]
            kaarten_beeld[2] = kaarten[12]
            kaarten.pop[12]
            #display opnieuw inladen           
            display.fill(background)
            draw_cards()
            pygame.display.flip()


#waardes om te beginnen
run = True
game_start = False

if game_start == False:
    draw_texts("druk op SPATIE om te beginnen", font, TEXT_COL, 280, 100)   #start scherm 



#game loop
while run:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:     #game beginnen na het indrukken van spatie-balk
                display.fill(background)
                draw_cards()
                controleer_op_sets()
                
                #witte kaders rondom de kaarten
                for i in range(0, 12):
                    pygame.draw.rect(display, white, [10 + 110*i, 20, 100, 200], 2)  
                    
                #de kaarten nummeren
                for i in range(0, 12):
                    getal = i
                    draw_texts(fr"{i + 1}", font_nummer, zwart, 15 + 110*i, 25)
                game_start = True
                            
        #kaarten selecteerbaar maken en in de select_cards lijst zetten    
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            for i in range(0, 12):
                #zorgt ervoor dat je de kaart selecteert die je aanklikt
                if 10 +110*i < x < 110 + 110*i  and  20 < y < 220:
                    if i in select_cards:
                        select_cards.remove(i)
                        pygame.draw.rect(display, white, [10 + 110*i, 20, 100, 200], 2)
                    else:
                        select_cards.append(i)
                        pygame.draw.rect(display, blue, [10 + 110*i, 20, 100, 200], 2)
                        
                        #als er 3 kaarten geselecteerd zijn checken of het een set is
                        if len(select_cards) == 3:
                            controleer_set(select_cards[0], select_cards[1], select_cards[2])
                            

            
    if event.type == pygame.QUIT:
        run = False
    
    pygame.display.flip()
    
pygame.quit()
print(random.choice(sets))
