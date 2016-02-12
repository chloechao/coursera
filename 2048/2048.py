"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    new_line = []
    #removed all zero item
    new_line += [ item for item in line if item != 0 ]

    #replaced with a tile of twice the value
    index = 0
    while index < len(new_line)-1:
        if new_line[index] == new_line[index+1]:
            new_line[index] = int(new_line[index]) * 2
            new_line.pop(index+1)
        index += 1

    #appended zero to the new list
    new_line += [ 0 for dummy_i in range(len(new_line),len(line)) ]
    return new_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid_panle = [[0 for dummy_col in range(self._grid_width)]
                           for dummy_row in range(self._grid_height)]           

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        index = 0
        while index < 2:
            row = random.randint(0, self._grid_height-1)
            col = random.randint(0, self._grid_width-1)
            if self._grid_panle[row][col] == 0:
                self.set_tile(row, col, self.new_tile())
                index += 1

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "Game Over!"

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        merged = []
        if direction == 1:
            for steps in range(self._grid_width):
                merged = merge(self.traverse_grid((0, steps), OFFSETS[direction], self._grid_height))
                self.replace_grid((0, steps), OFFSETS[direction], self._grid_height, merged)

        if direction == 2:
            for steps in range(self._grid_width):
                merged = merge(self.traverse_grid((self._grid_height - 1, steps), OFFSETS[direction], self._grid_height)) 
                self.replace_grid((3, steps), OFFSETS[direction], self._grid_height, merged)

        if direction == 3:
            for steps in range(self._grid_height):
                merged = merge(self.traverse_grid((steps, 0), OFFSETS[direction], self._grid_width)) 
                self.replace_grid((steps, 0), OFFSETS[direction], self._grid_height, merged)
            
        if direction == 4:
            for steps in range(self._grid_height):
                merged = merge(self.traverse_grid((steps, self._grid_width - 1), OFFSETS[direction], self._grid_width)) 
                self.replace_grid((steps, 3), OFFSETS[direction], self._grid_height, merged)
        
        dummy_conuter = self._grid_height * self._grid_width
        while True:
            row = random.randint(0, self._grid_height-1)
            col = random.randint(0, self._grid_width-1)
            if self._grid_panle[row][col] == 0:
                self.set_tile(row, col, self.new_tile())
                break
            else:
                dummy_conuter -= 1
                if dummy_conuter == 0:
                    self.__str__()
                    break
                      
        
    def traverse_grid(self, start_cell, direction, num_steps):
        """ Traverse grid raws """
        line = []
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            line.append(self._grid_panle[row][col])  
        return line
    
    def replace_grid(self, start_cell, direction, num_steps, merged_line):
        """ Replace raw data by merged data """
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            self._grid_panle[row][col] = merged_line[step]


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        val = 4
        if random.randint(1,10) != 10: 
            val = 2
        return val


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        try:
            if self._grid_panle[row][col] == 0:
                self._grid_panle[row][col] = value
        except IndexError:
            self.__str__()


    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid_panle[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
