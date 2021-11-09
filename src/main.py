import argparse
from time import sleep, time
from agent_6 import Agent_6
from gridworld import Gridworld
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

  # create a gridworld
  if not complete_grid:
    complete_grid = Gridworld(start, target, dim, prob, False)
    complete_grid.print()
    print()
  
  # create agents
    agents = [Agent_6(dim)]
    agent_counter = 0



def main():
    p = argparse.ArgumentParser()
    p.add_argument(
      "-d", "--dimension", type=int, default=5, help="dimension of gridworld"
    )
    p.add_argument(
      "-p",
      "--probability",
      type=float,
      default=0.33,
      help="probability of a blocked square",
    )

    # parse arguments and create the gridworld
    args = p.parse_args()

    # call the solver method with the args
    solver(args.dimension, args.probability)

if __name__ == "__main__":
    main()