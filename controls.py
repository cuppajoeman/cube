import pygame


def read_player_input_and_operate_on_cube(event, cube):
    if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
        if event.mod == pygame.KMOD_NONE:
            SHIFT_HELD = False
        else:
            if event.mod & pygame.KMOD_SHIFT:
                SHIFT_HELD = True
            else:
                SHIFT_HELD = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_u:
            if not SHIFT_HELD:
                cube.rotate_U_cw();
            else:
                cube.rotate_U_ccw();

        if event.key == pygame.K_d:
            if not SHIFT_HELD:
                cube.rotate_D_cw();
            else:
                cube.rotate_D_ccw();

        if event.key == pygame.K_m:
            if not SHIFT_HELD:
                cube.rotate_M_cw();
            else:
                cube.rotate_M_ccw();

        if event.key == pygame.K_r:
            if not SHIFT_HELD:
                cube.rotate_R_cw();
            else:
                cube.rotate_R_ccw();

        if event.key == pygame.K_l:
            if not SHIFT_HELD:
                cube.rotate_L_cw();
            else:
                cube.rotate_L_ccw();

        if event.key == pygame.K_f:
            if not SHIFT_HELD:
                cube.rotate_F_cw();
            else:
                cube.rotate_F_ccw();

        if event.key == pygame.K_b:
            if not SHIFT_HELD:
                cube.rotate_B_cw();
            else:
                cube.rotate_B_ccw();

        if event.key == pygame.K_x:
            if not SHIFT_HELD:
                cube.rotate_X_cw();
            else:
                cube.rotate_X_ccw();

        if event.key == pygame.K_y:
            if not SHIFT_HELD:
                cube.rotate_Y_cw();
            else:
                cube.rotate_Y_ccw();

        if event.key == pygame.K_z:
            if not SHIFT_HELD:
                cube.rotate_Z_cw();
            else:
                cube.rotate_Z_ccw();