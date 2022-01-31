from json.tool import main
import random
from tkinter.tix import COLUMN


def dead_state(width, height):
    d_state = []
    x_list = []
    for i in range(height):
        for j in range(width):
            x_list.append(0)
        d_state.append(x_list)
        x_list = []
    
    return d_state

def random_state(width, height):
    # Build the board using your previous work
    state = dead_state(width, height)

    # TODO: randomize each element of `state`
    # to either 0 or 1

    for i in range(len(state)):
        for j in range(len(state[i])):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state = 1
            else:
                cell_state = 0
            state[i][j] = cell_state
    return state


def render(state):
    print("-"+(len(state[0])+1)*2*'-')  # not very cool way to get the symmetry
    for row in range(len(state)):
        print("|",end=" ")
        for colum in range(len(state[row])):

            if state[row][colum] == 1:
                state[row][colum] = "◼"
            else:
                state[row][colum] = "*"

            print(state[row][colum], end=" ")
        print("|")
    print("-"+(len(state[0])+1)*2*'-')

if __name__ == "__main__":
    render(random_state(12,3))