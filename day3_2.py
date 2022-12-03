ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
PRIORITTY_DICT = {letter: value + 1 for value, letter in enumerate(ALPHABET)}

def compare_compartments(left, center, right):
    shared_item = set(left).intersection(set(right))
    shared_item = list(shared_item.intersection(set(center)))
    assert len(shared_item) == 1
    return shared_item[0]


def compute_priority(shared_item):
    return PRIORITTY_DICT[shared_item]


def solution():
    with open("./inputs/day3.txt", "r") as f:
        rucksacks = [line.strip() for line in f]
    n_elves = len(rucksacks)
    assert n_elves % 3 == 0
    priority_sum = 0
    for i in range(n_elves // 3):
        left, center, right = rucksacks[3 * i: 3 * i + 3]
        shared_item = compare_compartments(left, center, right)
        priority = compute_priority(shared_item)
        priority_sum += priority

    return priority_sum

if __name__ == "__main__":
    answer = solution()
    print(f"The solution is: {answer}")
        