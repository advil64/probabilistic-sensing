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

    **Answer:** For every cell except (x,y), $P_{i,j}(t + 1)$ = $P_{i,j}(t) / (1 - P_{x,y}(t))$

    **For cell (x,y), $P_{x,y}(t + 1)$ = 0**

- At time t + 1 you attempt to enter $(x,y)$, find it unblocked, and also learn its terrain type?

    $P_{i,j}(t + 1)$

    = $P_{i,j}(t)$

    **Answer:** $P_{i,j}(t + 1)$ = $P_{i,j}(t)$

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

    **Answer:** For every cell except (x,y), $P_{i,j}(t + 1)$ = $P_{i,j}(t) / (P_{x,y}(t) * 0.2 + (1 - P_{x,y}(t)))$.

    **For cell (x,y), $P_{x,y}(t + 1)$ = $(P_{x,y}(t) * 0.2) / (P_{x,y}(t) * 0.2 + (1 - P_{x,y}(t)))$.**

- At time t + 1 you examine cell $(x,y)$ of terrain type hilly, and fail to find the target?
  
    **Answer:** For every cell except (x,y), $P_{i,j}(t + 1)$ = $P_{i,j}(t) / (P_{x,y}(t) * 0.5 + (1 - P_{x,y}(t)))$.

    **For cell (x,y), $P_{x,y}(t + 1)$ = $(P_{x,y}(t) * 0.5) / (P_{x,y}(t) * 0.5 + (1 - P_{x,y}(t)))$.**

- At time t + 1 you examine cell $(x,y)$ of terrain type forest, and fail to find the target?
  
    **Answer:** For every cell except (x,y), $P_{i,j}(t + 1)$ = $P_{i,j}(t) / (P_{x,y}(t) * 0.8 + (1 - P_{x,y}(t)))$.

    **For cell (x,y), $P_{x,y}(t + 1)$ = $(P_{x,y}(t) * 0.8) / (P_{x,y}(t) * 0.8 + (1 - P_{x,y}(t)))$.**

- At time t + 1 you examine cell $(x,y)$ and find the target?

    **Answer:** For every cell except (x,y), $P_{i,j}(t + 1)$ = $0$.

    **For cell (x,y), $P_{x,y}(t + 1)$ = $1$.**


**At time t, with probability $P_{i,j}(t)$ of cell $(i,j)$ containing the target, what is the probability of finding the target in cell $(x,y)$:**

- If $(x,y)$ is hilly?

    $P(\text{finding target in (x,y)})$

    = $P(\text{in (x,y) and finding in a hilly terrain})$ ← These two are independent events

    = $P(\text{in (x,y)}) * P(\text{finding in hilly terrain})$

    = $P_{x,y}(t) * (1 - 0.5)$

    = $P_{x,y}(t) * 0.5$

    **Answer:** $P_{x,y}(t) * 0.5$

- If $(x,y)$ is flat?

    $P(\text{finding target in (x,y)})$

    = $P(\text{in (x,y) and finding in a flat terrain})$ ← These two are independent events

    = $P(\text{in (x,y)}) * P(\text{finding in flat terrain})$

    = $P_{x,y}(t) * (1 - 0.2)$

    = $P_{x,y}(t) * 0.8$

    **Answer:** $P_{x,y}(t) * 0.8$

- If $(x,y)$ is forest?

    $P(\text{finding target in (x,y)})$

    = $P(\text{in (x,y) and finding in a forest terrain})$ ← These two are independent events

    = $P(\text{in (x,y)}) * P(\text{finding in forest terrain})$

    = $P_{x,y}(t) * (1 - 0.8)$

    = $P_{x,y}(t) * 0.2$

    **Answer:** $P_{x,y}(t) * 0.2$

- If $(x,y)$ has never been visited?

    $P(\text{finding target in (x,y)})$

    = $P(\text{in (x,y) and finding in an unknown terrain})$ ← These two are independent events

    = $P(\text{in (x,y)}) * P(\text{finding in unknown terrain})$

    = $P(\text{in (x,y)}) * (P(\text{finding in terrain and terrain is blocked}) + P(\text{finding in terrain and terrain is flat}) + P(\text{finding in terrain and terrain is hilly}) + P(\text{finding in terrain and terrain is forest}))$

    = $P(\text{in (x,y)}) * (P(\text{terrain is blocked})*P(\text{finding in terrain | terrain is blocked}) + P(\text{terrain is flat})*P(\text{finding in terrain | terrain is flat}) + P(\text{terrain is hilly})*P(\text{finding in terrain | terrain is hilly}) + P(\text{terrain is forest})*P(\text{finding in terrain | terrain is forest}))$

    = $P(\text{in (x,y)}) * ((0.3) * (1-1) + (0.7) * ((1⁄3) * (1-0.2) + (1⁄3) * (1-0.5) + (1⁄3) * (1-0.8)))$

    = $P(\text{in (x,y)}) * (0.7) * ((1⁄3) * 1.5)$

    = $P(\text{in (x,y)}) * (0.7) * 0.5$

    = $P_{x,y}(t)*0.35$

    **Answer:** $P_{x,y}(t) * 0.35$


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

We first decided to start building Agent 8 from Agent 7 because we noticed that our Agent 7 was able to find the target in less actions than Agent 6 on average.

Once it reaches the first guess, it attempts to look for the target. Each square in the grid has a varying false negative rate depending on the type of terrain. If the target does not exist in the first guess or if the search returns a false negative, we make decisions that differs from Agent 7.

First, we calculate a *utility* value to determine which cell to examine next. This utility value is determined using the probability of finding the target and the manhattan distance from the target. As the probability of finding the target increases, our utility value will increase. However, as the manhattan distance from our current cell increases, our utility value for that cell will decrease. We chose to use this utility value as we don't want to disregard promising cells that are close by just because they don't happen to have the highest probability of finding the target. This way, we can examine closer cells that also have a reasonably high probability of finding the target. This should lower our number of movements as we may find the target in these closer cells which lessens the number of movements incase we go to farther cells and have to come back after examining those farther cells. We use the following formula to determine the utility value of a cell:
  - $value_{i,j} = p(finding in (i,j)) - dist(agent, (i,j)) * (\frac{1}{dim^2}) * 0.01$

We first normalize the distance value by dividing it by the total size of the grid. This way, we won't severely limit the distance we're willing to travel to a cell with the highest probability of finding the target. For example, in larger grid sizes, the manhattan distance to a promising cell will be large and could be bad for the utility value if we don't normalize the distance. And thus, we divide the manhattan distance by the size of the grid to prevent this issue. We then multiply the distance with an additional 0.01 to further avoid that issue of large distances being too punishing. Now that we determined the utility value of the cells, we pick the cell with the greatest utility value.

Next, in the event that there is a tie for the highest utility value, we look at the surroundings of all of the tied cells. We do this by summing the probability of finding the target in the neighbors of the tied cells. Whichever cell has the highest sum is then chosen as the next cell to examine. We do this in order to go to an area with high probabilties of finding the cell as this should increase our chances of finding the target without having to move much more incase the cell we examined failed.

Lastly, during execution of our path to the cell with the highest utilty value, we also examine cells along the path that also have a relatively high probability of finding the target. We determine this by seeing if that cell has a finding probability that is at least 0.8 * the finding probability of the cell with the highest utility value. This way, we can check reasonable cells along the way without having to perform A* and execute a path towards that cell later on. We chose the value 0.8 as we want to be open to more cells along the path; however, we don't want to examine too many cells along the path if their finding probability isn't reasonably high compared to the cell with the highest utility.

The belief state $(P_{i,j}(t))$ enters into our decision making when we are determining the utlity value of a cell, finding cells in areas with higher probabilities, and when deciding to examine cells along the path. This is because we rely on the probability of finding the cell to make these decisions as described above.

We don't need to calculate anything new that isn't already availaible to us as we use the same probabilities and manhattan distances that we used in Agent 6 and 7. All we do in Agent 8 is use these values in different ways to calculate the utility value of examining a cell to see if that cell is reasonable to examine.


**Implement Agent 8, run it sufficiently many times to give a valid comparison to Agents 6 and 7, and verify that Agent 8 is superior.**


**How could you improve Agent 8 even further? Be explicit as to what you could do, how, and what you would need.**

