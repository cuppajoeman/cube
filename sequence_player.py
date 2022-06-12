import constants
from analysis import CubeAnalyzer


class SequencePlayer:
    def __init__(self, cube, sequence=""):
        self.cube = cube
        self.time_per_move = 0.5  # seconds
        self.time_since_last_move = 0
        self.sequence = sequence

        self.cube_analyzer = CubeAnalyzer(cube)

    def load_sequence(self, sequence: str):
        self.sequence = sequence

    def perform_move(self, move: str):
        if move == "U":
            self.cube.rotate_U_cw()
        elif move == "U'":
            self.cube.rotate_U_ccw()
        elif move == "D":
            self.cube.rotate_D_cw()
        elif move == "D'":
            self.cube.rotate_D_ccw()
        elif move == "R":
            self.cube.rotate_R_cw()
        elif move == "R'":
            self.cube.rotate_R_ccw()
        elif move == "L":
            self.cube.rotate_L_cw()
        elif move == "L'":
            self.cube.rotate_L_ccw()
        elif move == "F":
            self.cube.rotate_F_cw()
        elif move == "F'":
            self.cube.rotate_F_ccw()
        elif move == "B":
            self.cube.rotate_B_cw()
        elif move == "B'":
            self.cube.rotate_B_ccw()

    def run_sequence(self, time_since_last_frame: float) -> None:
        """
        This method is called every frame of the simulation
        """

        if self.time_since_last_move >= self.time_per_move:
            print(self.cube_analyzer.get_number())

            split_sequence = self.sequence.split(" ")

            current_move = split_sequence[0]

            self.perform_move(current_move)

            self.sequence = " ".join(split_sequence[1:])

            self.time_since_last_move = 0

        self.time_since_last_move += time_since_last_frame




