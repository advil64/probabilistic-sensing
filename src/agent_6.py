from heuristics import manhattan
from gridworld import Gridworld
from probability_queue import Probability_Queue
from probability_node import Probability_Node
import heapq

class Agent_6:

  def __init__(self, dim):
    self.dim = dim
    self.discovered_grid = Gridworld(dim)
    self.cells = {}
    self.belief_state = Probability_Queue()
    # Initialize all cell info in belief state
    for i in range(self.dim):
        for j in range(self.dim):
            prob_node = Probability_Node(1/(self.dim**2), 1/(self.dim**2), manhattan((0,0), (self.dim-1, self.dim-1)), (i,j))
            self.belief_state.enqueue(prob_node)
            self.cells[(i,j)] = prob_node

  def execute_path(self, path, complete_grid):
    explored = 0
    for node in path:
      curr = node.curr_block
      # check if path is blocked
      if complete_grid.gridworld[curr[0]][curr[1]] == 1:
        # update our knowledge of blocked nodes
        self.discovered_grid.update_grid_obstacle(curr, 1)
        return node.parent_block, explored
      # Update discovered grid with the terrain type
      self.discovered_grid.update_grid_obstacle(curr, complete_grid.gridworld[curr[0]][curr[1]])
      explored += 1
    return path[-1], explored

  def update_belief_block(self, block_coord):
    for prob_node in self.belief_state:
      if not prob_node[3].coord == block_coord:
        prob_node[3].target_probability = prob_node[3].target_probability / (1 - self.cells[block_coord].target_probability)
        prob_node[3].priority_probability = prob_node[3].target_probability
        prob_node[0] = prob_node[3].priority_probability
      else:
        prob_node[3].target_probability = 0
        prob_node[3].priority_probability = 0
        prob_node[0] = 0

    heapq.heapify(self.belief_state.queue)