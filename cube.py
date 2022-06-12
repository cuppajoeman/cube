# Resources Used:
#  https://ruwix.com/the-rubiks-cube/notation/

r = "RED"
o = "ORANGE"
g = "GREEN"
b = "BLUE"
w = "WHITE"
y = "YELLOW"


class Cube:
    def __init__(self):

        """
        The faces are stored in a way that you rotate the cube
        horizontally to see the face directly
        """

        self.up_face = [
            [y, y, y],
            [y, y, y],
            [y, y, y]
        ]

        self.down_face = [
            [w, w, w],
            [w, w, w],
            [w, w, w]
        ]

        self.front_face = [
            [r, r, r],
            [r, r, r],
            [r, r, r]
        ]

        self.back_face = [
            [o, o, o],
            [o, o, o],
            [o, o, o]
        ]

        self.left_face = [
            [b, b, b],
            [b, b, b],
            [b, b, b]
        ]

        self.right_face = [
            [g, g, g],
            [g, g, g],
            [g, g, g]
        ]

        self.faces = [self.up_face, self.down_face, self.right_face, self.left_face, self.front_face, self.back_face]

    def __str__(self):
        return f"""
    ==== CUBE STATE ====

    UP FACE:
    {self.up_face}

    DOWN FACE:
    {self.down_face}

    LEFT_FACE: 
    {self.left_face}

    FRONT_FACE:
    {self.front_face}

    RIGHT FACE:
    {self.right_face}

    BACK_FACE:
    {self.back_face}
    """

    def rotate_cw_colors_on_face(self, face):
        self._rotate_corners(face)
        self._rotate_edges(face)

    def _rotate_corners(self, face):
        first_corner = face[0][0]
        corner_swap_map = {
            (0, 0): (2, 0),
            (2, 0): (2, 2),
            (2, 2): (0, 2)
        }

        for target_idx, other_idx in corner_swap_map.items():
            face[target_idx[0]][target_idx[1]] = face[other_idx[0]][other_idx[1]]

        face[0][2] = first_corner

    def _rotate_edges(self, face):
        first_edge = face[0][1]
        edge_swap_map = {
            (0, 1): (1, 0),
            (1, 0): (2, 1),
            (2, 1): (1, 2)
        }

        for target_idx, other_idx in edge_swap_map.items():
            face[target_idx[0]][target_idx[1]] = face[other_idx[0]][other_idx[1]]

        face[1][2] = first_edge

    def rotate_ccw_colors_on_face(self, face):
        for _ in range(3):
            self.rotate_cw_colors_on_face(face)

    def rotate_X_cw(self):
        self.front_face, \
        self.down_face, \
        self.back_face, \
        self.up_face \
            = \
            self.down_face, \
            self.back_face, \
            self.up_face, \
            self.front_face

        self.rotate_cw_colors_on_face(self.right_face)
        self.rotate_ccw_colors_on_face(self.left_face)

        self.rotate_cw_colors_on_face(self.down_face)
        self.rotate_cw_colors_on_face(self.down_face)

        self.rotate_cw_colors_on_face(self.back_face)
        self.rotate_cw_colors_on_face(self.back_face)

    def rotate_X_ccw(self):
        for _ in range(3):
            self.rotate_X_cw()

    def rotate_Y_cw(self):
        self.front_face, \
        self.left_face, \
        self.back_face, \
        self.right_face \
            = \
            self.right_face, \
            self.front_face, \
            self.left_face, \
            self.back_face

        self.rotate_cw_colors_on_face(self.up_face)
        self.rotate_ccw_colors_on_face(self.down_face)

    def rotate_Y_ccw(self):
        for _ in range(3):
            self.rotate_Y_cw()

    def rotate_Z_cw(self):
        self.up_face, \
        self.right_face, \
        self.down_face, \
        self.left_face \
            = \
            self.left_face, \
            self.up_face, \
            self.right_face, \
            self.down_face

        self.rotate_cw_colors_on_face(self.right_face)
        self.rotate_cw_colors_on_face(self.left_face)
        self.rotate_cw_colors_on_face(self.up_face)
        self.rotate_cw_colors_on_face(self.down_face)

        self.rotate_cw_colors_on_face(self.front_face)
        self.rotate_ccw_colors_on_face(self.back_face)

    def rotate_Z_ccw(self):
        for _ in range(3):
            self.rotate_Z_cw()

    def rotate_U_cw(self):
        self.front_face[0], \
        self.right_face[0], \
        self.back_face[0], \
        self.left_face[0] \
            = \
            self.right_face[0], \
            self.back_face[0], \
            self.left_face[0], \
            self.front_face[0]

        self.rotate_cw_colors_on_face(self.up_face)

    def rotate_U_ccw(self):
        for _ in range(3):
            self.rotate_U_cw()

    def rotate_D_cw(self):
        self.rotate_Z_cw()
        self.rotate_Z_cw()
        self.rotate_U_cw()
        self.rotate_Z_cw()
        self.rotate_Z_cw()

    def rotate_D_ccw(self):
        for _ in range(3):
            self.rotate_D_cw()

    def rotate_R_cw(self):
        self.rotate_Z_ccw()
        self.rotate_U_cw()
        self.rotate_Z_cw()

    def rotate_R_ccw(self):
        for _ in range(3):
            self.rotate_R_cw()

    def rotate_L_cw(self):
        self.rotate_Z_cw()
        self.rotate_U_cw()
        self.rotate_Z_ccw()

    def rotate_L_ccw(self):
        for _ in range(3):
            self.rotate_L_cw()

    def rotate_F_cw(self):
        self.rotate_Y_cw()
        self.rotate_L_cw()
        self.rotate_Y_ccw()

    def rotate_F_ccw(self):
        for _ in range(3):
            self.rotate_F_cw()

    def rotate_B_cw(self):
        self.rotate_Y_ccw()
        self.rotate_L_cw()
        self.rotate_Y_cw()

    def rotate_B_ccw(self):
        for _ in range(3):
            self.rotate_B_cw()

    def rotate_M_cw(self):
        self.rotate_R_cw()
        self.rotate_L_ccw()
        self.rotate_X_ccw()

    def rotate_M_ccw(self):
        for _ in range(3):
            self.rotate_M_cw()