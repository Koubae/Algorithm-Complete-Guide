"""Find Desire Weight in a connected Graph"""


def move(m, n, weight_limit):

    # ==== < CONFIG VARIABLES > ==== #
    step_counter = m + n - 1
    max_val = m         # NOTE: It starts from the last Value (4) and Goes Backwards
    path = []           # NOTE: Stores the path (need to reverse it afterwards)
    while max_val:
        if step_counter <= 0:   # NOTE: starting Node so it break Not need to return
            break
        least = max_val * ((max_val - 1) / 2)
        path.append(max_val)
        weight_limit -= max_val
        step_counter -= 1
        if weight_limit < least: 
            break
        # ==== < ROW CHECK | CAN IT GO TO THE LEFT? > ==== #
        if step_counter:     
            check_row = least + (step_counter - (max_val - 1)) * (max_val - 1)
            while weight_limit > check_row:  # FAQ: 1 Footnotes
                path.append(max_val)
                weight_limit -= max_val
                step_counter -= 1

        max_val -= 1
    return path


def combine(m, n, sum):
    path = move(m, n, sum)
    path.reverse()  # NOTE: Reverse the result Path
    result = []
    for i in range(1, len(path)):
        if path[i] == path[i - 1]:   # NOTE: Check if next Value is the same then it moved it to the Right
            result.append((path[i], 'Right'))
        else:
            result.append((path[i], 'Left'))
    return result


def prettify_result(res):
    for value in res:
        print(f'V={value[0]}) {value[1]} |-> ', end='')


if __name__ == '__main__':
    path = combine(4, 4, 16)
    prettify_result(path)

# FAQ: This loops checks whether it can go left (not right because is upside down) and if can then it keep going
#  to the left as mush as possible. In the example of a Matric of 4x4 and Max Weigth of 16, it keeps going to the left
#  in row N2 (index 1)
