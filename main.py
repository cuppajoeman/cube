from cube import Cube
import constants
import controls
from sequence_player import SequencePlayer

rubicks_cube = Cube()
sequence_player = SequencePlayer(rubicks_cube)

# sequence_player.load_sequence("R U " * 200)

# Visual Representation

import pygame

pygame.init()
infoObject = pygame.display.Info()
SCREEN_X, SCREEN_Y = infoObject.current_w, infoObject.current_h

FACE_SIZE = 30
STICKER_MARGIN = 2
FACE_MARGIN = 2
TOTAL_FACE_WIDTH = 2 * FACE_MARGIN + 2 * STICKER_MARGIN + 3 * FACE_SIZE
CUBE_REPRESENTATION_VERTICAL_CENTER = (3 * TOTAL_FACE_WIDTH) / 2 - TOTAL_FACE_WIDTH
CUBE_REPRESENTATION_HORIZONTAL_CENTER = (4 * TOTAL_FACE_WIDTH) / 2
BG_COLOR = (100, 100, 100)

window = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
clock = pygame.time.Clock()

SHIFT_HELD = False

ticks_since_last_frame = 0

run = True
while run:
    clock.tick(constants.FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        controls.read_player_input_and_operate_on_cube(event, rubicks_cube)

    window.fill(BG_COLOR)

    # Drawing cube
    UP_CORNER_X, UP_CORNER_Y = TOTAL_FACE_WIDTH, 0
    for y, row in enumerate(rubicks_cube.up_face):
        y = UP_CORNER_Y + y * (FACE_SIZE + STICKER_MARGIN)
        for x, sticker in enumerate(row):
            x = UP_CORNER_X + x * (FACE_SIZE + STICKER_MARGIN)
            sticker_rect = pygame.Rect(x, y, FACE_SIZE, FACE_SIZE)
            pygame.draw.rect(window, pygame.color.THECOLORS[sticker.lower()], sticker_rect)

    DOWN_CORNER_X, DOWN_CORNER_Y = TOTAL_FACE_WIDTH, TOTAL_FACE_WIDTH * 2
    for y, row in enumerate(rubicks_cube.down_face):
        y = DOWN_CORNER_Y + y * (FACE_SIZE + STICKER_MARGIN)
        for x, sticker in enumerate(row):
            x = DOWN_CORNER_X + x * (FACE_SIZE + STICKER_MARGIN)
            sticker_rect = pygame.Rect(x, y, FACE_SIZE, FACE_SIZE)
            pygame.draw.rect(window, pygame.color.THECOLORS[sticker.lower()], sticker_rect)

    LEFT_CORNER_X, LEFT_CORNER_Y = 0, TOTAL_FACE_WIDTH
    for y, row in enumerate(rubicks_cube.left_face):
        y = LEFT_CORNER_Y + y * (FACE_SIZE + STICKER_MARGIN)
        for x, sticker in enumerate(row):
            x = LEFT_CORNER_X + x * (FACE_SIZE + STICKER_MARGIN)
            sticker_rect = pygame.Rect(x, y, FACE_SIZE, FACE_SIZE)
            pygame.draw.rect(window, pygame.color.THECOLORS[sticker.lower()], sticker_rect)

    FRONT_CORNER_X, FRONT_CORNER_Y = TOTAL_FACE_WIDTH, TOTAL_FACE_WIDTH
    for y, row in enumerate(rubicks_cube.front_face):
        y = FRONT_CORNER_Y + y * (FACE_SIZE + STICKER_MARGIN)
        for x, sticker in enumerate(row):
            x = FRONT_CORNER_X + x * (FACE_SIZE + STICKER_MARGIN)
            sticker_rect = pygame.Rect(x, y, FACE_SIZE, FACE_SIZE)
            pygame.draw.rect(window, pygame.color.THECOLORS[sticker.lower()], sticker_rect)

    RIGHT_CORNER_X, RIGHT_CORNER_Y = TOTAL_FACE_WIDTH * 2, TOTAL_FACE_WIDTH
    for y, row in enumerate(rubicks_cube.right_face):
        y = RIGHT_CORNER_Y + y * (FACE_SIZE + STICKER_MARGIN)
        for x, sticker in enumerate(row):
            x = RIGHT_CORNER_X + x * (FACE_SIZE + STICKER_MARGIN)
            sticker_rect = pygame.Rect(x, y, FACE_SIZE, FACE_SIZE)
            pygame.draw.rect(window, pygame.color.THECOLORS[sticker.lower()], sticker_rect)

    BACK_CORNER_X, BACK_CORNER_Y = TOTAL_FACE_WIDTH * 3, TOTAL_FACE_WIDTH
    for y, row in enumerate(rubicks_cube.back_face):
        y = BACK_CORNER_Y + y * (FACE_SIZE + STICKER_MARGIN)
        for x, sticker in enumerate(row):
            x = BACK_CORNER_X + x * (FACE_SIZE + STICKER_MARGIN)
            sticker_rect = pygame.Rect(x, y, FACE_SIZE, FACE_SIZE)
            pygame.draw.rect(window, pygame.color.THECOLORS[sticker.lower()], sticker_rect)

    current_ticks = pygame.time.get_ticks()
    delta_time = (current_ticks - ticks_since_last_frame) / 1000.0
    ticks_since_last_frame = current_ticks

    sequence_player.run_sequence(delta_time)

    temp_surf = window.copy()
    window.fill(
        BG_COLOR)  # here, you can fill the screen with whatever you want to take the place of what was there before
    window.blit(temp_surf, (CUBE_REPRESENTATION_HORIZONTAL_CENTER, CUBE_REPRESENTATION_VERTICAL_CENTER))
    pygame.display.flip()

pygame.quit()
exit()