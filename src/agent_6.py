from heuristics import manhattan
from gridworld import Gridworld
from probability_queue import Probability_Queue
from probability_node import Probability_Node
from random import random
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
        prob_node = Probability_Node(1/(self.dim**2), 1/(self.dim**2), (i,j))
        self.belief_state.enqueue(prob_node)
        self.cells[(i,j)] = prob_node

  def execute_path(self, path, complete_grid, guess, target):
    actions = 0
    for node in path:
      curr = node.curr_block
      # check if path is blocked
      if complete_grid.gridworld[curr[0]][curr[1]] == 1:
        # update our knowledge of blocked nodes
        self.discovered_grid.update_grid_obstacle(curr, 1)
        # update the belief state after learning about this blocked cell
        self.update_belief_block(curr, node.parent_block.curr_block)
        return node.parent_block, actions, False
      # Update discovered grid with the terrain type
      self.discovered_grid.update_grid_obstacle(curr, complete_grid.gridworld[curr[0]][curr[1]])
      # Update cell's false negative rate after observing its terrain type
      self.update_false_negative_rate(curr)
      # Increment number of actions taken because of movement
      actions += 1
      # Check if we reached target cell
      if curr == guess:
        # Increment number of actions taken because of examination
        actions += 1
        # Examine the cell to search for target
        if self.examine_cell(curr, target):
          return path[-1], actions, True
    return path[-1], actions, False

  # Update given cell's false negative rate based off its terrain type
  def update_false_negative_rate(self, coord):
    # Observe the terrain at this cell and update its false negative rate appropriately
    if self.discovered_grid.gridworld[coord[0]][coord[1]] == 2:
      self.cells[coord].false_negative_rate = 0.2
    elif self.discovered_grid.gridworld[coord[0]][coord[1]] == 3:
      self.cells[coord].false_negative_rate = 0.5
    elif self.discovered_grid.gridworld[coord[0]][coord[1]] == 4:
      self.cells[coord].false_negative_rate = 0.8
  
  # Examine this cell to see if target is here
  def examine_cell(self, coord, target):
    # Check if target is even contained in coord
    if coord != target:
      self.update_belief_failed_examination(coord)
      return False
    # If we are in the cell with the target, simulate a search
    prob_node = self.cells[coord]
    if random() > prob_node.false_negative_rate:
      return True
    else:
      self.update_belief_failed_examination(coord)
      return False

  # Update probabilities of all cells after learning about the blocked cell
  def update_belief_block(self, block_coord, last_coord):
    # Probabilty that the blocked cell contained the target
    block_probability = self.cells[block_coord].target_probability
    # Update the beliefs of each cell
    for index, prob_node in enumerate(self.belief_state.queue):
      if not prob_node[3].coord == block_coord:
        # Update probabilities of all cells except the blocked cell
        prob_node[3].target_probability = prob_node[3].target_probability / (1 - block_probability)
        prob_node[3].priority_probability = prob_node[3].target_probability
        # Update the priority and distance of this cell in the priority queue
        self.belief_state.queue[index] = (prob_node[3].priority_probability * -1, manhattan(last_coord, prob_node[3].coord), prob_node[2], prob_node[3])
      else:
        # Update probabilities of the blocked cell
        prob_node[3].target_probability = 0
        prob_node[3].priority_probability = 0
        # Update the priority and distance of this cell in the priority queue
        self.belief_state.queue[index] = (0, manhattan(last_coord, prob_node[3].coord), prob_node[2], prob_node[3])

    # Heapify the queue so the cell with max probability is next in queue
    heapq.heapify(self.belief_state.queue)
    #print(self.belief_state.queue)
  
  # Update probabilities of all cells if examination fails
  def update_belief_failed_examination(self, coord):
    # Probability that the examined cell contained the target
    examine_probability = self.cells[coord].target_probability
    # False negative rate of the examined cell
    examine_false_negative_rate = self.cells[coord].false_negative_rate
    # Update the beliefs of each cell
    for index, prob_node in enumerate(self.belief_state.queue):
      if not prob_node[3].coord == coord:
        # Update probabilities of all cells except the examined cell
        prob_node[3].target_probability = prob_node[3].target_probability / (examine_probability * examine_false_negative_rate + (1 - examine_probability))
        prob_node[3].priority_probability = prob_node[3].target_probability
        # Update the priority and distance of this cell in the priority queue
        self.belief_state.queue[index] = (prob_node[3].priority_probability * -1, manhattan(coord, prob_node[3].coord), prob_node[2], prob_node[3])
      else:
        # Update probabilities of the examined cell
        prob_node[3].target_probability = (examine_probability * examine_false_negative_rate) / (examine_probability * examine_false_negative_rate + (1 - examine_probability))
        prob_node[3].priority_probability = prob_node[3].target_probability
        # Update the priority and distance of this cell in the priority queue
        self.belief_state.queue[index] = (prob_node[3].priority_probability * -1, manhattan(coord, prob_node[3].coord), prob_node[2], prob_node[3])

    # Heapify the queue so the cell with max probability is next in queue
    heapq.heapify(self.belief_state.queue)
    #print(self.belief_state.queue)