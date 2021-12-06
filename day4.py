GROUP_SIZE = 5

def bingo():
    
    with open("/Users/viniciusgusmao/Documents/AoC2021/4.1.txt") as file:
        content = file.read().split()
    
        numbers_drawn = content[0].split(',')
    
        boards_count = (len(content) - 1) / (GROUP_SIZE * GROUP_SIZE)
    
        boards = []
        positions_by_number = {}
    
        number_idx = 1
    
        # create all boards
        for board_idx in range(boards_count):
            board = []
            for row_idx in range(GROUP_SIZE):
                row = []
                for col_idx in range(GROUP_SIZE):
                    number = content[number_idx]
                    number_idx += 1
                    row.append(number)
    
                    # adds to map with positions of each number across all boards
                    positions = positions_by_number.get(number)
                    if positions is None:
                        positions = []
                        positions_by_number[number] = positions
                    positions.append((board_idx, row_idx, col_idx))
    
                board.append(row)
            boards.append(board)
    
        marks_by_group = {}
        marked_numbers = set()
        boards_that_won = set()
        last_board_to_win = None
    
        for number_drawn in numbers_drawn:
            marked_numbers.add(number_drawn)
            positions_to_mark = positions_by_number.get(number_drawn)
    
            if positions_to_mark is not None:
                # for each board that contains the number that was drawn...
                for position_to_mark in positions_to_mark:
                    board_idx = position_to_mark[0]

                    if board_idx in boards_that_won:
                        continue  # we no longer care about this board
    
                    # checks row completion
                    board_row = (board_idx, position_to_mark[1], -1)
                    count_marks = marks_by_group.get(board_row, 0) + 1
                    marks_by_group[board_row] = count_marks
                    if count_marks == GROUP_SIZE:
                        boards_that_won.add(board_idx)
                        if len(boards_that_won) == boards_count:
                            last_board_to_win = board_idx
                            break
    
                    # checks column completion
                    board_col = (board_idx, -1, position_to_mark[2])
                    count_marks = marks_by_group.get(board_col, 0) + 1
                    marks_by_group[board_col] = count_marks
                    if count_marks == GROUP_SIZE:
                        boards_that_won.add(board_idx)
                        if len(boards_that_won) == boards_count:
                            last_board_to_win = board_idx
                            break
    
            if last_board_to_win is not None:
                sum_unmarked = 0
                for row_idx in range(GROUP_SIZE):
                    for col_idx in range(GROUP_SIZE):
                        number = boards[last_board_to_win][row_idx][col_idx]
                        if number not in marked_numbers:
                            sum_unmarked += int(number)

                return sum_unmarked * int(number_drawn)

        return None
            

print bingo()        



