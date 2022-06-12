class CubeAnalyzer:
  def __init__(self, cube):
    self.cube = cube

  def get_number(self):
    number = 0
    for face in self.cube.faces:
      center_color = face[1][1]
      for row in face:
        for sticker_color in row:
          if sticker_color != center_color:
            number += 1
    return number