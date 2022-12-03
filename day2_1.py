SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def resolve_round(left, right):
    if left == 'A':
        if right == 'X':
            return 3
        elif right == 'Y':
            return 6
        else:
            return 0
    elif left == 'B':
        if right == 'X':
            return 0
        elif right == 'Y':
            return 3
        else:
            return 6
    else:
        if right == 'X':
            return 6
        elif right == 'Y':
            return 0
        else:
            return 3

def solution():
    with open('./inputs/day2.txt', 'r') as f:
        strategy = [tuple(line.strip().split(" ")) for line in f]

    total_score = 0
    for hand in strategy:
        round_score = resolve_round(*hand)
        hand_score = SCORES[hand[1]]
        total_score += round_score + hand_score

    return total_score


if __name__ == "__main__":
    answer = solution()
    print(f"The solution is: {answer}")

        
        