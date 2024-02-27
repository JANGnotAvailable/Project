import pygame
import animation
pygame.init()

#screen init
screen_width = 1080
screen_height = screen_width * 0.8
screen = pygame.display.set_mode((screen_width, screen_height))

moving_left = False
moving_right = False

#colours
BG = (50, 50, 50)
BLACK = (0, 0, 0)

#create class for samurai commander
class Character(pygame.sprite.Sprite):
    def __init__(self, char_module, x, y, scale, action, speed):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.action = action
        self.flip = False
        self.frame_num = animation.get_frame_num(f'{action}')
        self.speed = speed

        #test code
        action = 'Idle'

        #character image
        self.img = pygame.image.load(f'figure material/{char_module}/{self.action}.png').convert_alpha()
        self.rect = self.img.get_rect()
        self.animation_list = animation.get_animation(self.frame_num, self.img, 128, 128, self.scale, BG)
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.animation_list[3], self.flip, False), self.rect)
    
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0

        if moving_left:
            dx -= self.speed
            self.flip = True

        if moving_right:
            dx += self.speed
            self.flip = False
        
        self.rect.x += dx
        self.rect.y += dy




#test materials
player = Character('Samurai_Commander', 0, 0, 1, 'Dead', 3)

        

run = True
while run:
    screen.fill(BG)
    player.draw()
    player.move(moving_left, moving_right)

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
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
    
    pygame.display.update()


pygame.quit()
