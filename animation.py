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

# test materials below
screen_width = 800
screen_height = screen_width * 0.8
screen = pygame.display.set_mode((screen_width, screen_height))

BG = (50, 50, 50)

test = get_animation(6, pygame.image.load('figure material/Samurai_Commander/Dead.png'), 128, 128, 3, (0, 0, 0))

run = True
while run:
    screen.fill(BG)
    screen.blit(test[2], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()

pygame.quit()
