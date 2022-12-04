def parse_line(line):
    left, right = line.split(",")
    left = tuple(int(i) for i in left.split('-'))
    right = tuple(int(i) for i in right.split('-'))
    return left, right

def is_contained(left, right):
    # Smaller interval first
    if left[1] - left[0] > right[1] - right[0]:
        left, right = right, left

    return left[0] >= right[0] and left[1] <= right[1]
        

def solution():
    with open('./inputs/day4.txt', 'r') as f:
        assignments = f.readlines()
    assignments = [parse_line(assignment) for assignment in assignments]
    overlapping_regions = [is_contained(*assignment) for assignment in assignments]
    return sum(overlapping_regions)


if __name__ == "__main__":
    answer = solution()
    print(f"The solution is: {answer}")
        