import random
import time  # Import the time module

# Define the maze as a 2D list where 0 represents a path and 1 represents a wall
maze = [
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 0]
]


maze2 = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0]]


# Define the player's initial position
player_position = [0, 0]

# Define the exit position
exit_position = [9, 9]

# Initialize a variable to count the player's steps
steps = 0

# Initialize a list to store the player's inputs
player_inputs = []

# Define the game title
game_title = "Mamba Maze"

# Initialize start time
start_time = time.time()

# Function to print the current state of the maze
def print_maze():
    # Print the game title
    print(game_title.center(30, '-'))

    for row_index, row in enumerate(maze):
        for col_index, cell in enumerate(row):
            if [row_index, col_index] == player_position:
                print('X', end=' ')
            elif [row_index, col_index] == exit_position:
                print('*', end=' ')
            else:
                print(cell, end=' ')
        print()
    print("Inputs: " + " ".join(player_inputs))

# Main game loop
while True:
    print_maze()

    # Ask the player for their move
    move = input("Enter 'n' for North, 's' for South, 'w' for West, 'e' for East, or 'exit' to quit: ")

    if move == 'exit':
        print("You exited the game.")
        break

    if move not in ['n', 's', 'w', 'e']:
        print("Invalid input. Please enter 'n', 's', 'w', 'e', or 'exit'.")
        continue

    # Add the move to the list of player inputs
    player_inputs.append(move)

    # Calculate the new position based on the player's move
    new_position = player_position.copy()
    if move == 'n':
        new_position[0] -= 1
    elif move == 's':
        new_position[0] += 1
    elif move == 'w':
        new_position[1] -= 1
    elif move == 'e':
        new_position[1] += 1

    # Check if the new position is within the bounds of the maze
    if 0 <= new_position[0] < len(maze) and 0 <= new_position[1] < len(maze[0]):
        # Check if the new position is a valid path (0)
        if maze[new_position[0]][new_position[1]] == 0:
            player_position = new_position
            steps += 1
            # Check if the player has reached the exit
            if player_position == exit_position:
                print_maze()
                end_time = time.time()
                elapsed_time = end_time - start_time
                minutes = int(elapsed_time // 60)
                seconds = int(elapsed_time % 60)
                print(f"Congratulations! You reached the exit in {steps} steps.")
                print(f"Time taken: {minutes} minutes {seconds} seconds.")
                break
        else:
            print("You hit a wall. You can't move there.")
    else:
        print("You can't move outside the maze.")

