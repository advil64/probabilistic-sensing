# Queue to hold frings
from probability_node import Probability_Node
import heapq

# Used to determine which cell to select as a target next
class Probability_Queue:
    def __init__(self):
        self.queue = []
        self.counter = 0
    
    # checks if it is empty
    def is_empty(self):
        return True if len(self.queue) == 0 else False
    
    # adds a fringe node to the queue
    def enqueue(self, node):
        # add the new node into the queue
        heapq.heappush(self.queue, (node.priority_probability, node.distance, self.counter, node))
        self.counter += 1
    
    # removes the fringe node from list
    def remove_fringe_node(self, coord):
        for index, node in enumerate(self.queue):
            if node[3].coord == coord:
                # if node is in last index, just pop it
                if index == len(self.queue) - 1:
                    self.queue.pop()
                    return
                # replace the node to remove with the last node and heapify
                last_node = self.queue.pop()
                self.queue[index] = last_node
                heapq.heapify(self.queue)

    # pops the lowest distance node from the queue
    def de_queue(self):
        node = heapq.heappop(self.queue)
        return node[3]