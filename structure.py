import pygame
import animation
import character

pygame.init()

screen_width = 1080
screen_height = int(screen_width * 0.8)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("sheet test")
BG = (0, 0, 0)
BLACK = (0, 0, 0)
red = (255, 0, 0)

gravity = 0.981

moving_left = False
moving_right = False
walk = False


class Samurai(pygame.sprite.Sprite):
    
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed
        self.flip = False
        self.jump = False
        self.in_air = True
        self.y_vel = 0
        self.action_list = ['Idle', 'Walk','Jump']
        self.action_type = 0
        self.model = pygame.image.load(f'new project/figure material/modle.png')
        self.animation_list = character.return_animation(f'{self.action_list[self.action_type]}')
        self.frame_index = 0
        self.rect = self.animation_list[self.frame_index].get_rect()
        self.rect.center = (x, y)
        self.update_time = pygame.time.get_ticks()


    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        
        if moving_left:
            dx = -self.speed
            self.flip = True
        if moving_right:
            dx = self.speed
            self.flip = False
        if self.jump and self.in_air:
            self.y_vel = -11
            self.jump = False
        
        self.y_vel += gravity
        if self.y_vel >= 10:
            self.y_vel = 10
        dy += self.y_vel
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            
        
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        self.animation_list = character.return_animation(self.action_list[self.action_type])
        self.image = self.animation_list[self.frame_index]
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect.center)
        pygame.draw.line(screen, red, (0, 300), (screen_width, 300))


    def update_animation(self):
        animation_cooldown = 100
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0
    
    def update_action(self, new_action_type):
        if new_action_type != self.action_type:
            self.action_type = new_action_type
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()






player = Samurai(100, 100, 5)


run = True
while run:
    
    screen.fill(BG)
    player.draw()

    if player.alive:
        if player.jump:
            player.update_action(2)
        elif moving_left or moving_right:
            player.update_action(1)
        else:
            player.update_action(0)
        player.move(moving_left, moving_right)
        player.update_animation()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_d:
                moving_right = True
            elif event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_w and player.alive:
                player.jump = True
                player.in_air = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            elif event.key == pygame.K_d:
                moving_right = False


    
    pygame.display.update()

pygame.quit()
