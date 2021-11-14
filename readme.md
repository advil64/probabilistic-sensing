# Probabilistic Sensing
### Advith Chegu (ac1771) & Naveenan Yogeswaran (nry7)
### Both group members contributed equally to the code, data collection, and report.

### Prior to any interaction with the environment, what is the probability of the target being in a given cell?

### Let $P_{i,j}(t)$ be the probability that cell $(i,j)$ contains the target, given the observations collected up to time t. At time $t+1$, suppose you learn new information about cell $(x,y)$. Depending on what information you learn, the probability for each cell needs to be updated. What should the new $P_{i,j}(t+1)$ be for each cell $(i,j)$ under the following circumstances:

- At time t + 1 you attempt to enter $(x,y)$ and find it is blocked?
- At time t + 1 you attempt to enter $(x,y)$, find it unblocked, and also learn its terrain type?
- At time t + 1 you examine cell $(x,y)$ of terrain type flat, and fail to find the target?
- At time t + 1 you examine cell $(x,y)$ of terrain type hilly, and fail to find the target?
- At time t + 1 you examine cell $(x,y)$ of terrain type forest, and fail to  nd the target?
- At time t + 1 you examine cell $(x,y)$ and  nd the target?


### At time t, with probability $P_{i,j}(t)$ of cell $(i,j)$ containing the target, what is the probability of finding the target in cell $(x,y)$:

- If $(x,y)$ is hilly?
- If $(x,y)$ is flat?
- If $(x,y)$ is forest?
- If $(x,y)$ has never been visited?

