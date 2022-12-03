ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
PRIORITTY_DICT = {letter: value + 1 for value, letter in enumerate(ALPHABET)}

def split_rucksack(rucksack):
    n = len(rucksack)
    assert n % 2 == 0
    return rucksack[:n//2], rucksack[n//2:]


def compare_compartments(left, right):
    shared_item = list(set(left).intersection(set(right)))
    assert len(shared_item) == 1
    return shared_item[0]


def compute_priority(shared_item):
    return PRIORITTY_DICT[shared_item]


def solution():
    with open("./inputs/day3.txt", "r") as f:
        rucksacks = [line.strip() for line in f]
    priority_sum = 0
    for rucksack in rucksacks:
        left, right = split_rucksack(rucksack)
        shared_item = compare_compartments(left, right)
        priority = compute_priority(shared_item)
        priority_sum += priority

    return priority_sum

if __name__ == "__main__":
    answer = solution()
    print(f"The solution is: {answer}")
        