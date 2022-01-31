from json.tool import main
import random


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

    


if __name__ == "__main__":
    print(random_state(3,4))