import argparse
from time import sleep, time
from agent_6 import Agent_6
from gridworld import Gridworld
from heuristics import manhattan
from a_star import path_planner
import json
from pprint import pprint
from random import choices, randint, random


"""
  Creates a gridworld and carrys out repeated A* based on the agent
  @param dim: dimension of the grid
  @param prob: probability of having a blocker
  @param agent: the type of visibility we have
  @param complete_grid: optional supplied grid instead of creating one 
"""
def solver(dim, prob, complete_grid=None):

  # create a start and end position randomly
  start = (randint(0, dim-1), randint(0, dim-1))
  target = (randint(0, dim-1), randint(0, dim-1))
  guess = start
  # start = (4,4)
  # target = (2,4)
  # guess = (0,1)

  # json output
  data = {"Agent 6": {}}

  # create a gridworld
  if not complete_grid:
    print("Start: " + str(start))
    print("Target: " + str(target))
    print("Guess: " + str(guess))
    # keep generating a new grid until we get a solvable one
    complete_grid = Gridworld(dim, start, target, prob, False)
    while not verify_solvability(dim, start, target, complete_grid):
      # keep generating a new grid until we get a solvable one
      complete_grid = Gridworld(dim, start, target, prob, False)
    complete_grid.print()
    print()
  
  # create agents
  agents = [Agent_6(dim, start)]
  agent_counter = 5

  for agent_object in agents:
    agent_counter += 1
    # total number of actions taken
    total_actions = 0
    # total number of cells processed
    total_cells_processed = 0
    # final path which points to last node
    final_path = None
    # number of times A* was repeated
    retries = 0
    # status of completion
    complete_status = False

    # perform repeated A* with the agent
    starting_time = time()
    # start planning a path from the starting block
    new_path, cells_processed = path_planner(
        start, final_path, guess, agent_object.discovered_grid, dim, manhattan
    )
    total_cells_processed += cells_processed
    # while A* finds a new path
    while len(new_path) > 0:
        retries += 1
        # execute the path
        last_node, actions_taken, found_target = agent_object.execute_path(new_path, complete_grid, guess, target)
        total_actions += actions_taken
        final_path = last_node
        # get the last unblocked block
        last_unblock_node = None
        if last_node:
            start = last_node.curr_block
            last_unblock_node = last_node.parent_block
        # check if target was found
        if found_target:
            complete_status = True
            break
        # Update guess cell to be next cell with highest probability
        guess = agent_object.max_cell.coord

        print("New Start: " + str(start) + " New Guess: " + str(guess))

        # create a new path from the last unblocked node
        new_path, cells_processed = path_planner(
            start,
            last_unblock_node,
            guess,
            agent_object.discovered_grid,
            dim,
            manhattan,
        )
        total_cells_processed += cells_processed
        # If there is no path to the guess, treat it as blocked and keep targeting the next cell with the highest probability
        while not new_path:
          # Treat guess as blocked and update beliefs
          agent_object.update_belief_block(guess, start)
          # Make new guess using the cell with highest probability
          guess = agent_object.max_cell.coord
          retries += 1
          # Find a path to this new guess cell
          new_path, cells_processed = path_planner(
            start,
            last_unblock_node,
            guess,
            agent_object.discovered_grid,
            dim,
            manhattan
          )
          total_cells_processed += cells_processed
    
    completion_time = time() - starting_time
    data["Agent {}".format(agent_counter)] = {"processed": total_cells_processed, "retries": retries, "time": completion_time, "actions": total_actions, "target": target, "terrain": str(complete_grid.gridworld[target[0]][target[1]])}
    
    # print("Agent %s Completed in %s seconds" % (agent_counter, completion_time))
    # print("Agent %s Processed %s cells" % (agent_counter, total_cells_processed))
    # print("Agent %s Took %s actions" % (agent_counter, total_actions))
    # print("Target found: " + str(target) + " with type " + str(complete_grid.gridworld[target[0]][target[1]]))

  print(json.dumps(data))


def verify_solvability(dim, start, target, complete_grid):
    # start planning a path from the starting block
    new_path, cells_processed = path_planner(start, None, target, complete_grid, dim, manhattan)

    # Check if a path was found
    if not new_path:
      return False
    
    return True

def main():
    p = argparse.ArgumentParser()
    p.add_argument(
      "-d", "--dimension", type=int, default=50, help="dimension of gridworld"
    )
    p.add_argument(
      "-p",
      "--probability",
      type=float,
      default=0.30,
      help="probability of a blocked square",
    )

    # parse arguments and create the gridworld
    args = p.parse_args()

    # call the solver method with the args
    solver(args.dimension, args.probability)

if __name__ == "__main__":
    main()