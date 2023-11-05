# cube

to launch the program get the dependencies `pip install -r requirements. txt` launch with `python main.py`

can a

## keybinds
rotate the (f: front, b: back, l: left, r: right, u: up, d: down) face clockwise, hold shift for couter clockwise

rotate the cube 90 degrees around the (x, y, z) axis clockwise, hold shift for couter clockwise

## goal
We would like to use this program to figure out a method to solve the rubicks cube in the minimal amount of moves. The general idea is that based on the current state of the cube the solver can inspect the cube and then consider the 12 possible next moves, and there should be a way to determine which move is the correct one.

## ideas/questions
- Maybe we can come up with properties about the edges and corners and based on those properties we can determine how moves would have been required to get to that state, then we can see if any of the 12 possible next moves produce a state which requires less moves to produce

## todo
- Add full move history & Compressed move information (Potentially implement concepts from file compression theory with the goal of compressing move information)

## resources
* https://people.math.harvard.edu/~jjchen/docs/Group%20Theory%20and%20the%20Rubik%27s%20Cube.pdf
* https://www.worldcubeassociation.org/regulations/scrambles/
* https://www.ryanheise.com/cube/
