POS = 0
SCORE = 1

TARGET = 21

memo = {}


def update(pos_and_score, die_result, update_score):
    pos = 1 + (pos_and_score[POS] + die_result - 1) % 10
    score = pos_and_score[SCORE] + (pos if update_score else 0)
    return pos, score


def solve(pos_and_score_1, pos_and_score_2, step):
    if step in [1, 4]:  # the only times we check for winners (i.e., before each player rolls their 1st die)
        if pos_and_score_1[SCORE] >= TARGET:
            return 1, 0
        if pos_and_score_2[SCORE] >= TARGET:
            return 0, 1

    result_from_memo = memo.get((pos_and_score_1, pos_and_score_2, step))
    if result_from_memo is not None:
        return result_from_memo

    wins1, wins2 = 0, 0

    for die_result in [1, 2, 3]:
        new_pos_and_score_1, new_pos_and_score_2 = pos_and_score_1, pos_and_score_2
        if step < 4:  # next die goes to Player 1
            new_pos_and_score_1 = update(pos_and_score_1, die_result, step == 3)
        else:         # next die goes to Player 2
            new_pos_and_score_2 = update(pos_and_score_2, die_result, step == 6)

        wins = solve(new_pos_and_score_1, new_pos_and_score_2, 1 + (step % 6))
        wins1 += wins[0]
        wins2 += wins[1]

    result = wins1, wins2

    memo[pos_and_score_1, pos_and_score_2, step] = result

    return result


print max(solve((1, 0), (5, 0), 1))
