import random
import time


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

    for i in range(height):
        for j in range(width):
            random_number = random.random()
            if random_number > 0.75:
                cell_state = 1
            else:
                cell_state = 0
            state[i][j] = cell_state
    return state

def next_board_state(state):

    ''' 
        Gets one state and calculate the next board state.
        Input: One state
        Output: Next state
    '''

    height = len(state)
    width  = len(state[0])
    
    #Get a new state variable to store the calculated cell values
    next_state = random_state(width, height)

    #Iterate over all cells and calculating next state of that cell
    for i in range(height):
        for j in range(width):

            next_state[i][j] = next_cell_value((i,j),state)

    
    return next_state


def next_cell_value(cell, state):

    '''
        Returns the next state of a cell by calculating neighbors
        Input : call coords and state
        Output : 0 or 1 depending on the neighbor count
    '''

    #Get the x and y position
    x,y = cell

    live_neighbors = 0

    height = len(state)
    width  = len(state[0])

    #Loop from top row to bottom row adjuscent to the cell
    for x1 in range(x-1, x+2):
        
        '''
            If row to be traversed is -1 , then traverse last row
            If row to be traversed is greater than the height or row count, ie, in the case of bottom edge cells,
            traverse the top row.
        '''
        if x1>=height:
            #x1 = 0
            continue
        elif x1<0:
            #x1 = height-1
            continue

        #Loop from left column to right column adjuscent to the cell
        for y1 in range(y-1,y+2):

            '''
                If column to be traversed is -1, then choose the last column which is the width-1
                If column to be traversed is greater than the column count or width, choose the first column ie, 0
            '''

            if y1>=width:
                #y1 = 0
                continue
            elif y1<0:
                #y1 = width-1
                continue


            #Check if the cell traversing is the cell that we are finding neighbours to.

            if (x1,y1) == (x,y): 
                continue
            else:
                
                #increase the count if neighbor is 1

                if state[x1][y1] == 1:
                    live_neighbors +=1

    if state[x][y] == 1:

        if live_neighbors < 1 or live_neighbors > 3:
            return 0
        else:
            return 1
    else:

        if live_neighbors == 3:
            return 1    
        else:
            return 0    


def render(state):

    '''
        Printing the state in a visually aesthetic way
        Input: state
        Output: Printing the state graphically
    '''

    display_as = {
        0: ' ',
        # This is "unicode" for a filled-in square. You can also just use a thick
        # "ASCII" character like a '$' or '#'.
        1: u"\u2588"
    }
    lines = []
    for x in range(0, len(state)):
        line = ''
        for y in range(0, len(state[0])):
            line += display_as[state[x][y]] * 2
        lines.append(line)
    print ("\n".join(lines))


def load_board_state(file_path):

    '''
    Reads input from file and returns state
    '''

    state = []
    item_list = []
    with open(file_path, 'r') as f:
        item_list = f.readlines()
    
    #Convert to a 2D list
    for item in item_list:
        list_item = list(item)
        
        #Remove newline
        try:
            list_item.remove("\n")
        except ValueError:
            pass
        
        num_list = [ int(x) for x in list_item ]

        state.append(num_list)

    return state


if __name__ == "__main__":
    
    init_state = load_board_state("./glider.txt")
    #init_state = random_state(3,3)
    
    
    print(next_board_state(init_state))
    while True:
         render(init_state)
         init_state = next_board_state(init_state)
         time.sleep(.3)