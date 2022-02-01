from main import next_board_state

if __name__ == "__main__":

    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    actual_next_state1 = next_board_state(init_state1)

    if expected_next_state1 == actual_next_state1:
        print ("PASSED 1")
    else:
        print("FAILED 1")
        print ("Expected:")
        print (expected_next_state1)
        print ("Actual:")
        print (actual_next_state1)

    init_state2 = [
        [0,0,1,1],
        [0,1,1,0],
        [0,0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1,1],
        [0,1,1,1],
        [0,1,0,1]
    ]


    actual_next_state2 = next_board_state(init_state2)


    if expected_next_state2 == actual_next_state2:
        print ("PASSED 2")
    else:
        print("FAILED 2")
        print ("Expected:")
        print (expected_next_state2)
        print ("Actual:")
        print (actual_next_state2)