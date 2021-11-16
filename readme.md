# Probabilistic Sensing
### Advith Chegu (ac1771) & Naveenan Yogeswaran (nry7)
### Both group members contributed equally to the code, data collection, and report.

**Prior to any interaction with the environment, what is the probability of the target being in a given cell?**

Prior to any interaction with the environment, each cell should have equal probabilty of containing the target.
Given the dimension for the grid D, the probability for each cell is $1/(D^2)$.

**Let $P_{i,j}(t)$ be the probability that cell $(i,j)$ contains the target, given the observations collected up to time t. At time $t+1$, suppose you learn new information about cell $(x,y)$. Depending on what information you learn, the probability for each cell needs to be updated. What should the new $P_{i,j}(t+1)$ be for each cell $(i,j)$ under the following circumstances:**

- At time t + 1 you attempt to enter $(x,y)$ and find it is blocked?

$P_{i,j}(t + 1)$

= $P(\text{in (i,j) | not (x,y)})$

= $P(\text{in (i,j) and not (x,y)}) / P(\text{not (x,y)})$

Because the target can only be in one cell, we know $P(in (i,j) and not (x,y))$ is the same as $P(in (i,j))$.

= $P(\text{in (i,j)}) / P(\text{not (x,y)})$

= $P_{i,j}(t) / (1 - P_{x,y}(t))$

### Answer: For every cell except (x,y), $P_{i,j}(t + 1)$ = $P_{i,j}(t) / (1 - P_{x,y}(t))$
### For cell (x,y), $P_{x,y}(t + 1)$ = 0

- At time t + 1 you attempt to enter $(x,y)$, find it unblocked, and also learn its terrain type?

$P_{i,j}(t + 1)$

= $P_{i,j}(t)$

### Answer: $P_{i,j}(t + 1)$ = $P_{i,j}(t)$
- At time t + 1 you examine cell $(x,y)$ of terrain type flat, and fail to find the target?

$P(\text{failed at (x,y)})$

= $P(\text{failed at (x,y) and in (x,y)}) + ∑_{i,j} P(\text{failed at (x,y) and in (i,j)})$

= $P(\text{in (x,y)}) * P(\text{failed at (x,y) | in (x,y)}) + ∑_{i,j} P(\text{in (i,j)}) * P(\text{failed at (x,y) | in (i,j)})$

Because the target can only be in one cell, we know $P(failed at (x,y) | in (i,j))$ is $1$.

= $P(\text{in (x,y)}) * 0.2 + ∑_{i,j} P(\text{in (i,j)}) * 1$

= $P(\text{in (x,y)}) * 0.2 + (1 - P(\text{in (x,y)}))$

= $P_{x,y}(t) * 0.2 + (1 - P_{x,y}(t))$

New probability for every cell except (x,y).

$P_{i,j}(t + 1)$

= $P(\text{in (i,j) | failed at (x,y)})$

= $P(\text{in (i,j) and failed at (x,y)}) / P(\text{failed at (x,y)})$

= $(P(\text{in (i,j)}) * P(\text{failed at (x,y) | in (i,j)})) / P(\text{failed at (x,y)})$

Because the target can only be in one cell, we know $P(failed at (x,y) | in (i,j))$ is $1$.

= $(P(\text{in (i,j)}) * 1) / P(\text{failed at (x,y)})$

= $P(\text{in (i,j)}) / P(\text{failed at (x,y)})$

= $P_{i,j}(t) / (P_{x,y}(t) * 0.2 + (1 - P_{x,y}(t)))$

New probability for cell (x,y)

$P_{x,y}(t + 1)$

= $P(\text{in (x,y) | failed at (x,y)})$

= $P(\text{in (x,y) and failed at (x,y)}) / P(\text{failed at (x,y)})$

= $(P(\text{in (x,y)}) * P(\text{failed at (x,y) | in (x,y)})) / P(\text{failed at (x,y)})$

= $(P(\text{in (x,y)}) * 0.2) / P(\text{failed at (x,y)})$

= $(P_{x,y}(t) * 0.2) / (P_{x,y}(t) * 0.2 + (1 - P_{x,y}(t)))$

### Answer: For every cell except (x,y), $P_{i,j}(t + 1)$ = $P_{i,j}(t) / (P_{x,y}(t) * 0.2 + (1 - P_{x,y}(t)))$.
### For cell (x,y), $P_{x,y}(t + 1)$ = $(P_{x,y}(t) * 0.2) / (P_{x,y}(t) * 0.2 + (1 - P_{x,y}(t)))$.
- At time t + 1 you examine cell $(x,y)$ of terrain type hilly, and fail to find the target?
### Answer: For every cell except (x,y), $P_{i,j}(t + 1)$ = $P_{i,j}(t) / (P_{x,y}(t) * 0.5 + (1 - P_{x,y}(t)))$.
### For cell (x,y), $P_{x,y}(t + 1)$ = $(P_{x,y}(t) * 0.5) / (P_{x,y}(t) * 0.5 + (1 - P_{x,y}(t)))$.
- At time t + 1 you examine cell $(x,y)$ of terrain type forest, and fail to find the target?
### Answer: For every cell except (x,y), $P_{i,j}(t + 1)$ = $P_{i,j}(t) / (P_{x,y}(t) * 0.8 + (1 - P_{x,y}(t)))$.
### For cell (x,y), $P_{x,y}(t + 1)$ = $(P_{x,y}(t) * 0.8) / (P_{x,y}(t) * 0.8 + (1 - P_{x,y}(t)))$.
- At time t + 1 you examine cell $(x,y)$ and find the target?
### Answer: For every cell except (x,y), $P_{i,j}(t + 1)$ = $0$.
### For cell (x,y), $P_{x,y}(t + 1)$ = $1$.


**At time t, with probability $P_{i,j}(t)$ of cell $(i,j)$ containing the target, what is the probability of finding the target in cell $(x,y)$:**

- If $(x,y)$ is hilly?

$P(\text{finding target in (x,y)})$

= $P(\text{in (x,y) and finding in a hilly terrain})$ ← These two are independent events

= $P(\text{in (x,y)}) * P(\text{finding in hilly terrain})$

= $P_{x,y}(t) * (1 - 0.5)$

= $P_{x,y}(t) * 0.5$

### Answer: $P_{x,y}(t) * 0.5$
- If $(x,y)$ is flat?

$P(\text{finding target in (x,y)})$

= $P(\text{in (x,y) and finding in a flat terrain})$ ← These two are independent events

= $P(\text{in (x,y)}) * P(\text{finding in flat terrain})$

= $P_{x,y}(t) * (1 - 0.2)$

= $P_{x,y}(t) * 0.8$

### Answer: $P_{x,y}(t) * 0.8$
- If $(x,y)$ is forest?

$P(\text{finding target in (x,y)})$

= $P(\text{in (x,y) and finding in a forest terrain})$ ← These two are independent events

= $P(\text{in (x,y)}) * P(\text{finding in forest terrain})$

= $P_{x,y}(t) * (1 - 0.8)$

= $P_{x,y}(t) * 0.2$

### Answer: $P_{x,y}(t) * 0.2$
- If $(x,y)$ has never been visited?

$P(\text{finding target in (x,y)})$

= $P(\text{in (x,y) and finding in an unknown terrain})$ ← These two are independent events

= $P(\text{in (x,y)}) * P(\text{finding in unknown terrain})$

= $P(\text{in (x,y)}) * (P(\text{finding in terrain and terrain is blocked}) + P(\text{finding in terrain and terrain is flat}) + P(\text{finding in terrain and terrain is hilly}) + P(\text{finding in terrain and terrain is forest}))$

= $P(\text{in (x,y)}) * (P(\text{terrain is blocked})*P(\text{finding in terrain | terrain is blocked}) + P(\text{terrain is flat})*P(\text{finding in terrain | terrain is flat}) + P(\text{terrain is hilly})*P(\text{finding in terrain | terrain is hilly}) + P(\text{terrain is forest})*P(\text{finding in terrain | terrain is forest}))$

= $P(\text{in (x,y)}) * ((0.3) * (1-1) + (0.7) * ((1⁄3) * (1-0.2) + (1⁄3) * (1-0.5) + (1⁄3) * (1-0.8)))$

= $P(\text{in (x,y)}) * (0.7) * ((1⁄3) * 1.5)$

= $P(\text{in (x,y)}) * (0.7) * 0.5$

= $P_{x,y}(t)*0.35 $

### Answer: $P_{x,y}(t) * 0.35$


**Implement Agent 6 and 7. For both agents, repeatedly run each agent on a variety of randomly generated boards (at constant dimension) to estimate the number of actions (movement + examinations) each agent needs on average to find the target. You will need to collect enough data to determine which of these agents is superior. Do you notice anything about the movement/examinations distribution for each agent? Note, boards where the target is unreachable from the initial agent position should be discarded.**

First let's look at the results from Agent 6. This was the most naive agent because it does not take into the terrain type of the target when prioritizing it in the queue. Therefore, predictably it has the worst performance as seen by its movements/examinations histogram below. 

![Histogram](./images/question_4_agent_6.png)

Next up we have agent 7 which is a little more informed when it picks out the next target. Instead of just aiming to find the cell most likely to contain the target, it picks out the cell which is most likely to successfully find the target. This means it takes the terrain type into consideration when creating the priority queue.

![Histogram](./images/question_4_agent_7.png)

Lastly, we have agent 8 which is the smartest. This agent uses a *utility* value (described below) which guides the agent to figure out how to prioritize target cells.

![Histogram](./images/question_4_agent_8.png)

To see a more clear side by side comparison of the performance of the agents, let's look at their box plots. These plots tell us that agent 8 performed far better than the other two agents using it's smarter techniques to find the target. There was much lesser movement vs examination due to the fact that agent 8 penalizes targets that are farther away when calculating the priority.

We also see that agent 7 performed better than agent 6. This is likely because by prioritizing cells which are more likely to contain the target, the agent was able to find the target quicker and hence made fewer movements.

![Histogram](./images/question_4_box.png)

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

