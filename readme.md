# Probabilistic Sensing
### Advith Chegu (ac1771) & Naveenan Yogeswaran (nry7)
### Both group members contributed equally to the code, data collection, and report.

**Prior to any interaction with the environment, what is the probability of the target being in a given cell?**

**Let $P_{i,j}(t)$ be the probability that cell $(i,j)$ contains the target, given the observations collected up to time t. At time $t+1$, suppose you learn new information about cell $(x,y)$. Depending on what information you learn, the probability for each cell needs to be updated. What should the new $P_{i,j}(t+1)$ be for each cell $(i,j)$ under the following circumstances:**

- At time t + 1 you attempt to enter $(x,y)$ and find it is blocked?
- At time t + 1 you attempt to enter $(x,y)$, find it unblocked, and also learn its terrain type?
- At time t + 1 you examine cell $(x,y)$ of terrain type flat, and fail to find the target?
- At time t + 1 you examine cell $(x,y)$ of terrain type hilly, and fail to find the target?
- At time t + 1 you examine cell $(x,y)$ of terrain type forest, and fail to  nd the target?
- At time t + 1 you examine cell $(x,y)$ and  nd the target?


**At time t, with probability $P_{i,j}(t)$ of cell $(i,j)$ containing the target, what is the probability of finding the target in cell $(x,y)$:**

- If $(x,y)$ is hilly?
- If $(x,y)$ is flat?
- If $(x,y)$ is forest?
- If $(x,y)$ has never been visited?


**Implement Agent 6 and 7. For both agents, repeatedly run each agent on a variety of randomly generated boards (at constant dimension) to estimate the number of actions (movement + examinations) each agent needs on average to  nd the target. You will need to collect enough data to determine which of these agents is superior. Do you notice anything about the movement/examinations distribution for each agent? Note, boards where the target is unreachable from the initial agent position should be discarded.**



**Describe your algorithm, be explicit as to what decisions it is making, how, and why. How does the belief state $(P_{i,j}(t))$ enter into the decision making? Do you need to calculate anything new that you didn't already have available?**

Like the initial two agents, agent 8 roughly follows the same process. It first makes a guess as to where the target is on the board and uses repeated A* to work its way towards it. 

Along the way, it updates the target probabilities of the nodes it encounters depending on the terrain type like agent 7 does. It uses the answers in the first two questions update target probabilities. 

Once it reaches the first guess, it attempts to look for the target. Each square in the grid has a varying false negative rate depending on the type of terrain. If the target does not exist in the first guess or if the search returns a false negative we take two steps which differ agent 8 from agent 7.

- First we calculate a *utility* value which is basically the priority probability (same as agent 7) but from that we subtract the distance between the agent and the cell. 
  - $value_{i,j} = p(in (i,j)) - dist(agent, (i,j)) * (\frac{1}{dim^2}) * 0.01$
  - We first normalize the distance value by dividing it by the total dimension of the grid then multiply by a weight of 0.01 to the value before subtracting it from the probability value
- Next in the event that there is a tie for the highest utility value, we look at the surroundings of all of the tied cells. The tie is broken by whichever cell has highest sum of priority probability in its surrounding cells.


**Implement Agent 8, run it sufficiently many times to give a valid comparison to Agents 6 and 7, and verify that Agent 8 is superior.**


**How could you improve Agent 8 even further? Be explicit as to what you could do, how, and what you would need.**

