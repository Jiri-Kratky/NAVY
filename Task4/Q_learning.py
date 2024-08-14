import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from maze import R

environment_rows = R.shape[0]
environment_columns = R.shape[1]

#playground
plt.imshow(R)
plt.show()

actions = ['up', 'down', 'left', 'right']

# Define the possible actions
Q_values = np.zeros((R.shape[0], R.shape[1], len(actions)))      # 15x15x4


#Check if the state is a terminal state (i.e., goal or trap)
def is_terminal_state(current_row_index, current_column_index):
  if R[current_row_index,current_column_index] == -1.0:   #when we are on -1, we are on the path... continue
    return False
  else:
    return True

#Get starting location
def get_starting_location():
  current_row_index = np.random.randint(environment_rows)
  current_column_index = np.random.randint(environment_columns)

  while is_terminal_state(current_row_index, current_column_index): #if i spawn on the goal or trap, spawn again
    current_row_index = np.random.randint(environment_rows)
    current_column_index = np.random.randint(environment_columns)

  return current_row_index, current_column_index

#Get next action (random or based on Q_values)
def get_next_action(current_row_index, current_column_index, epsilon):
  if np.random.random() < epsilon:  #choose the best action
    return np.argmax(Q_values[current_row_index, current_column_index])
  else:                             #choose a random action
    return np.random.randint(4)

#Get next location based on action
def get_next_location(current_row_index, current_column_index, action_index):
  new_row_index = current_row_index
  new_column_index = current_column_index
  if actions[action_index] == 'up' and current_row_index > 0:
    new_row_index -= 1
  elif actions[action_index] == 'right' and current_column_index < environment_columns - 1:
    new_column_index += 1
  elif actions[action_index] == 'down' and current_row_index < environment_rows - 1:
    new_row_index += 1
  elif actions[action_index] == 'left' and current_column_index > 0:
    new_column_index -= 1
  return new_row_index, new_column_index

#Get shortest path based on Q_values
def get_shortest_path(current_row_index, current_column_index):

    shortest_path = []
    shortest_path.append([current_row_index, current_column_index])

    while not is_terminal_state(current_row_index, current_column_index):   #until i reach goal (or fall into the trap if badly trained)

      action_index = get_next_action(current_row_index, current_column_index, 1.0) #epsilon changed to 1.0 to make sure the best action is chosen

      current_row_index, current_column_index = get_next_location(current_row_index, current_column_index, action_index)
      shortest_path.append([current_row_index, current_column_index])
    return shortest_path
  

#define training parameters
epsilon = 0.5           #the percentage of time when we should take the best action (instead of a random action)
discount_factor = 0.9   #discount factor for future rewards
learning_rate = 0.2     #the rate at which the AI agent should learn


episodes = 3000
for episode in range(episodes):
  row_index, column_index = get_starting_location()
  path = []
  path.append([row_index, column_index])
  while not is_terminal_state(row_index, column_index): #until we step on the goal or trap
    
    action_index = get_next_action(row_index, column_index, epsilon)    #choose an action (up,down,left,right)

    #perform the chosen action, and transition to the next state (i.e., move to the next location)
    old_row_index, old_column_index = row_index, column_index #store the old row and column indexes
    row_index, column_index = get_next_location(row_index, column_index, action_index)
    path.append([row_index, column_index])
    
    #Using Bellman equation
    #receive the reward for moving to the new state, and calculate the temporal difference
    reward = R[row_index,column_index]
    old_q_value = Q_values[old_row_index, old_column_index, action_index]
    temporal_difference = reward + (discount_factor * np.max(Q_values[row_index, column_index])) - old_q_value

    #update the Q-value for the previous state and action pair
    new_q_value = old_q_value + (learning_rate * temporal_difference)
    Q_values[old_row_index, old_column_index, action_index] = new_q_value
  
  if (episode % 1500 == 0):    
    fig, ax = plt.subplots()
    def animate(i):
        ax.clear()
        ax.imshow(R)
        for j in range(i+1):
            ax.scatter(path[j][1], path[j][0], color='red', marker='x')
        ax.scatter(path[i][1], path[i][0], color='blue', marker='o')
        ax.set_title(f'Step {i+1}')

    ani = animation.FuncAnimation(fig, animate, frames=len(path), interval=400, repeat=False)
    plt.show()

print('Training Done')



#Getting shortest paths
start = get_starting_location()
print("\nStarting location: ",start)
path = get_shortest_path(start[0],start[1])
fig, ax = plt.subplots()
def animate(i):
    ax.clear()
    ax.imshow(R)
    for j in range(i+1):
        ax.scatter(path[j][1], path[j][0], color='red', marker='x')
    ax.scatter(path[i][1], path[i][0], color='blue', marker='o')
    ax.set_title(f'Step {i+1}')

ani = animation.FuncAnimation(fig, animate, frames=len(path), interval=400, repeat=False)
plt.show()



#another one
start = get_starting_location()
print("\nStarting location: ",start)
path = get_shortest_path(start[0],start[1])
fig, ax = plt.subplots()
def animate(i):
    ax.clear()
    ax.imshow(R)
    for j in range(i+1):
        ax.scatter(path[j][1], path[j][0], color='red', marker='x')
    ax.scatter(path[i][1], path[i][0], color='blue', marker='o')
    ax.set_title(f'Step {i+1}')

ani = animation.FuncAnimation(fig, animate, frames=len(path), interval=400, repeat=False)
plt.show()