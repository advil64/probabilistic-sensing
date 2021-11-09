class Probability_Node:

    # priority_probability: probability that will be used by probability_queue for ordering 
    #                       (prob of cell containing target for agent 6, prob of finding target in cell for agent 7)
    # target_probability: probabilty of cell containing target
    # distance: Distance from cell to target
    # coord: The coordinates of this cell
    def __init__(self, priority_probability, target_probability, coord):
        self.priority_probability = priority_probability
        self.target_probability = target_probability
        self.coord = coord
        self.false_negative_rate = 1