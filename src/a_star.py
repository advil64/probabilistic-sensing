# solves gridworld using A* algorithm
from priority_queue import Priority_Queue
from fringe_node import Fringe_Node

# returns the path found as a list of tuples
def path_planner(start, latest_block, target, grid, dim, heuristic):
    # contains nodes to be discovered
    fringe = Priority_Queue()

    # contains nodes that were visited
    visited = set()

    # total number of nodes popped from fringe for processing
    cells_processed = 0

    # create the first fringe node
    start_node = Fringe_Node((start[0], start[1]), latest_block, heuristic((0, 0), target), 0)
    fringe.enqueue(start_node)

    # loop through the unvisited nodes
    while len(fringe.queue) > 0:

        # retrieve a node from the head of the fringe queue
        curr = fringe.de_queue()
        # add the node to the visited set
        visited.add(curr.curr_block)
        cells_processed += 1

        # Check if the goal node was popped
        if curr.curr_block == target:
            print("Path Found, Processed %s cells" % cells_processed)
            path = []
            # we reached the end trace the path back to start
            x = curr
            while x.curr_block != start:
                path.append(x)
                x = x.parent_block
            path.append(x)
            # we need to start from first node to the last
            path.reverse()
            return (path, cells_processed)
        else:
            check_neighbors(grid, dim, heuristic, curr, fringe, visited, target)

    print("No Path Found")
    return ([], cells_processed)
        
            
def check_neighbors(grid, dim, heuristic, curr_node, fringe, closed, target):
    curr_coord = curr_node.curr_block

    # neighbors to check
    to_check = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    # loop through and check the neighbors
    for n in to_check:
        # the cordinates of the neighbor
        curr_neighbor = (curr_coord[0] + n[0], curr_coord[1] + n[1])
        # check bounds
        if curr_neighbor[0] >= 0 and curr_neighbor[0] < dim and curr_neighbor[1] >= 0 and curr_neighbor[1] < dim:
            # check that the neighbor is not a block
            if grid.gridworld[curr_neighbor[0]][curr_neighbor[1]] != 1 and not curr_neighbor in closed:
                new_node = Fringe_Node(curr_neighbor, curr_node, curr_node.dist_from_start + 1 + heuristic(curr_neighbor, target), curr_node.dist_from_start + 1)
                fringe.enqueue(new_node)