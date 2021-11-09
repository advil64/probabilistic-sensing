from random import choices, randint, random

class Gridworld:

    # NOTE: 1 -> blocked, 2 -> flat, 3 -> hilly, 4 -> forest
    def __init__(self, start, target, dim, prob=0, empty=True):

        # gridworld is an object attribute
        self.gridworld = []

        # start filling in grids by rows and columns
        if empty:
            for x in range(dim):
                self.gridworld.append([9 for i in range(dim)])
        else:
            for x in range(dim):
                row = []
                for y in range(dim):
                    # start and target squares are guaranteed empty
                    if (x, y) == start or (x, y) == target:
                        # randomly pick type of terrain for square
                        row.append(self.pickTerrain())
                    else:
                        if random() > 0.3:
                            # randomly pick type of terrain for square
                            row.append(self.pickTerrain())
                        else:
                            # pick block for this square
                            row.append(1)
                # append the row to the gridworld
                self.gridworld.append(row)

    def print(self):
        for row in self.gridworld:
            print(row)

    def update_grid_with_path(self, path):
        trajectory_length = 0
        while path:
            self.gridworld[path.curr_block[0]][path.curr_block[1]] = 2
            path = path.parent_block
            trajectory_length += 1
        return trajectory_length

    def update_grid_obstacle(self, coord, value):
        self.gridworld[coord[0]][coord[1]] = value

    def pickTerrain(self):
        return randint(2,4)