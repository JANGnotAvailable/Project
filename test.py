from tkinter import *
import pygame
pygame.init()

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

def get_frame(image, frame, width, height, scale, colour):
	''' 
	get a specific frame from spritesheet base on given values, returns the frame of the image.
	
	image: the spritesheet file, is compatible with a single image, but "frame" value has to be 0
	frame: the specific frame of the spritesheet that is required
	width/height: size of each individual frame, has to be the full block (include the empty part)
	scale: the scale of the image
	colour: colour of the empty part of the character, perferably same as background colour
	
	'''
	img = pygame.surface.Surface((width, height)).convert_alpha()
	img.blit(image, (0, 0), (128 * frame, 0, width + (128 * frame), height))
	img = pygame.transform.scale(img, (width * scale, height * scale))
	img.set_colorkey(colour)
	return img

def get_animation(total_frame, image, width, height, scale, colour):
	''' using "get_frame()" function in a for loop to collect the frames in a list, then return that list'''
	
	animation_list = []
	for i in range(total_frame):
		animation_list.append(get_frame(image, i, width, height, scale, colour))
	return animation_list

screen = Tk()
screen.geometry('1080x720')
screen.title('test window')

screen.mainloop()