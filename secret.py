import pygame
pygame.init()

#windows setting
windoww = 800
windowh = int(windoww * 0.8)
window = pygame.display.set_mode((windoww, windowh))
pygame.display.set_caption('secret project')



run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        


pygame.quit()