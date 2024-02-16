import pygame
import animation

BLACK = (0, 0, 0)






def get_frame_num(animation_type):
    frame_num = 0
    if animation_type == 'Attack_1':
        frame_num = 4
    elif animation_type == 'Attact_2':
        frame_num = 5
    elif animation_type == 'Attack_3':
        frame_num = 4
    elif animation_type == 'Dead':
        frame_num = 6
    elif animation_type == 'Hurt':
        frame_num = 2
    elif animation_type == 'Idle':
        frame_num = 5
    elif animation_type == 'Jump':
        frame_num = 7
    elif animation_type == 'Protect':
        frame_num = 2
    elif animation_type == 'Run':
        frame_num = 8
    elif animation_type == 'Walk':
        frame_num = 9
    
    return frame_num


def return_animation(action):
    img = pygame.image.load(f'figure material/Samurai_Commander/{action}.png')
    sprite = animation.Sprite(img)
    frames = []
    for frame_number in range(get_frame_num(action)):
        frames.append(sprite.get_image(frame_number, 128, 128, 1, BLACK))
        
    return frames

