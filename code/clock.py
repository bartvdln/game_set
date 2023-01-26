seconds_timer = 30
start_time = pygame.time.get_ticks()
end_time = start_time + seconds_timer * 1000

done = False

clock = pygame.time.Clock()
font = pygame.font.Font(None, 60)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    remaining_time = (end_time - pygame.time.get_ticks()) / 1000
    remaining_time = round(remaining_time, 2)
    text = font.render(str(remaining_time), True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text, (250, 250))
    pygame.display.flip()
    clock.tick(60)
    if remaining_time <= 0:
        done = True
