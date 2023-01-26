import pygame
import random

pygame.init()

(width, height) = (1330, 500)
background = (160, 200, 150)
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)

font_nummer = pygame.font.SysFont("arialblack", 15)
text_col_nummer = (0, 0, 0)
kaarten_nummer = []

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
print(kaarten)

def draw_cards():
    for i in range(0, 12):
        kaart = pygame.image.load(' '.join(kaarten[i]+".gif")).convert()
        kaarten_display.append(kaart)
        display.blit(kaarten_display[i], (10 + 110*(i), 20))
        pygame.display.flip() 

def draw_texts(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    display.blit(img, (x, y))
    
kaarten_beeld = [kaarten[0], kaarten[1], kaarten[2], kaarten[3], kaarten[4], kaarten[5], kaarten[6], kaarten[7], kaarten[8], kaarten[9], kaarten[10], kaarten[11]]


def controleer_set(kaart_i, kaart_j, kaart_k):
	if ((kaart_i[0] == kaart_j[0] == kaart_k[0]) or (kaart_i[0] != kaart_j[0] != kaart_k[0])) and ((kaart_i[1] == kaart_j[1] == kaart_k[1]) or (kaart_i[1] != kaart_j[1] != kaart_k[1])) and ((kaart_i[2] == kaart_j[2] == kaart_k[2]) or (kaart_i[2] != kaart_j[2] != kaart_k[2])) and ((kaart_i[3] == kaart_j[3] == kaart_k[3]) or (kaart_i[3] != kaart_j[3] != kaart_k[3])): 
		draw_texts("Set!", font, text_col_nummer, 500, 100)
	else:
		draw_texts("Geen set", font, text_col_nummer, 500, 100)



run = True
game_start = False

if game_start == False:
    draw_texts("druk op SPATIE om te beginnen", font, TEXT_COL, 280, 100)




while run:
    
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                display.fill(background)
                draw_cards()
                for i in range(0, 12):
                    getal = i
                    draw_texts(fr"{i + 1}", font_nummer, text_col_nummer, 15 + 110*i, 25)
                game_start = True
        
    
            
    if event.type == pygame.QUIT:
        run = False
    
    pygame.display.flip()
    
pygame.quit()
