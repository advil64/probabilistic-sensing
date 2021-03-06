from heuristics import manhattan
from gridworld import Gridworld
from probability_queue import Probability_Queue
from probability_node import Probability_Node
from random import random, choice
import heapq

class Agent_6:

  def __init__(self, dim, start):
    self.dim = dim
    self.discovered_grid = Gridworld(dim)
    self.cells = {}
    self.belief_state = []
    # Initialize all cell info in belief state
    for i in range(self.dim):
      for j in range(self.dim):
        prob_node = Probability_Node(1/(self.dim**2), 1/(self.dim**2), (i,j))
        self.belief_state.append(prob_node)
        self.cells[(i,j)] = prob_node
    self.max_cell = self.cells[start]

  def execute_path(self, path, complete_grid, guess, target):
    movements = 0
    examinations = 0
    for node in path:
      curr = node.curr_block

      # check if path is blocked
      if complete_grid.gridworld[curr[0]][curr[1]] == 1:
        # update our knowledge of blocked nodes
        self.discovered_grid.update_grid_obstacle(curr, 1)
        # update the belief state after learning about this blocked cell
        self.update_belief_block(curr, node.parent_block.curr_block)
        return node.parent_block, movements, examinations, False

      # Update discovered grid with the terrain type
      self.discovered_grid.update_grid_obstacle(curr, complete_grid.gridworld[curr[0]][curr[1]])
      # Update cell's false negative rate after observing its terrain type
      self.update_false_negative_rate(curr)
      # Increment number of actions taken because of movement
      movements += 1
      
      # Check if we reached target cell
      if curr == guess:
        # Increment number of actions taken because of examination
        examinations += 1
        # Examine the cell to search for target
        if self.examine_cell(curr, target):
          return path[-1], movements, examinations, True
    return path[-1], movements, examinations, False

  # Return max cell
  def get_max_cell(self, curr):
    return self.max_cell.coord

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
    # Reset max_cell
    self.max_cell = self.belief_state[0]
    # list of max cells to break a tie
    max_cells = []

    # Update the beliefs of each cell
    for prob_node in self.belief_state:
      if not prob_node.coord == block_coord:
        # Update probabilities of all cells except the blocked cell
        prob_node.target_probability = prob_node.target_probability / (1 - block_probability)
        prob_node.priority_probability = prob_node.target_probability
      else:
        # Update probabilities of the blocked cell
        prob_node.target_probability = 0
        prob_node.priority_probability = 0
      
      # update max cell if necessary
      if prob_node.priority_probability > self.max_cell.priority_probability:
        self.max_cell = prob_node
        max_cells = []
      # if probabilities are the same use the distance to break a tie
      elif prob_node.priority_probability == self.max_cell.priority_probability:
        if manhattan(last_coord, self.max_cell.coord) > manhattan(last_coord, prob_node.coord):
          max_cells = []
          self.max_cell = prob_node
        # if distances and probabilities are the same use uniform random to break a tie
        elif manhattan(last_coord, self.max_cell.coord) == manhattan(last_coord, prob_node.coord):
          if not max_cells:
            max_cells.append(self.max_cell)
          max_cells.append(prob_node)
      
    # Uniform randomly pick a cell
    if max_cells:
      self.max_cell = choice(max_cells)
      

    # Heapify the queue so the cell with max probability is next in queue
    #heapq.heapify(self.belief_state.queue)
    #print(self.belief_state.queue)
  
  # Update probabilities of all cells if examination fails
  def update_belief_failed_examination(self, coord):
    # Probability that the examined cell contained the target
    examine_probability = self.cells[coord].target_probability
    # False negative rate of the examined cell
    examine_false_negative_rate = self.cells[coord].false_negative_rate
    # Reset max_cell
    self.max_cell = self.belief_state[0]
    # used to break ties
    max_cells = []

    # Update the beliefs of each cell
    for prob_node in self.belief_state:
      if not prob_node.coord == coord:
        # Update probabilities of all cells except the examined cell
        prob_node.target_probability = prob_node.target_probability / (examine_probability * examine_false_negative_rate + (1 - examine_probability))
        prob_node.priority_probability = prob_node.target_probability
      else:
        # Update probabilities of the examined cell
        prob_node.target_probability = (examine_probability * examine_false_negative_rate) / (examine_probability * examine_false_negative_rate + (1 - examine_probability))
        prob_node.priority_probability = prob_node.target_probability
        
      # update max cell if necessary
      if prob_node.priority_probability > self.max_cell.priority_probability:
        self.max_cell = prob_node
        max_cells = []
      # if probabilities are the same use the distance to break a tie
      elif prob_node.priority_probability == self.max_cell.priority_probability:
        if manhattan(coord, self.max_cell.coord) > manhattan(coord, prob_node.coord):
          max_cells = []
          self.max_cell = prob_node
        # if distances and probabilities are the same use uniform random to break a tie
        elif manhattan(coord, self.max_cell.coord) == manhattan(coord, prob_node.coord):
          if not max_cells:
            max_cells.append(self.max_cell)
          max_cells.append(prob_node)
      
    # Uniform randomly pick a cell
    if max_cells:
      self.max_cell = choice(max_cells)

    # Heapify the queue so the cell with max probability is next in queue
    #heapq.heapify(self.belief_state.queue)
    #print(self.belief_state.queue)