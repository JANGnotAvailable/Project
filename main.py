import pygame
import animation
pygame.init()

#screen init
screen_width = 800
screen_height = screen_width * 0.8
screen = pygame.display.set_mode((screen_width, screen_height))

moving_left = False
moving_right = False

#colours
BG = (50, 50, 50)
BLACK = (0, 0, 0)

#create class for samurai commander
class Character(pygame.sprite.Sprite):
    def __init__(self, char_module, x, y, scale, action):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.action = action
        self.flip = False
        self.frame_num = animation.get_frame_num(f'{action}')

        #test code
        action = 'Idle'

        #character image
        self.img = pygame.image.load(f'figure material/{char_module}/{self.action}.png').convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)
        animation_list = animation.get_animation(self.frame_num, self.img, 128, 128, self.scale, BLACK)
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)
    
    def move(self):
        pass




#test materials


        

run = True
while run:
    screen.fill(BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True

    pygame.display.update()

pygame.quit()
