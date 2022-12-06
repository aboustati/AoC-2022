from collections import deque


def read_file(path):
    with open(path, "r") as f:
        contents = f.read()
    return contents


def find_marker(code, pattern_len=4):
    buffer = deque([], maxlen=pattern_len)
    for idx, char in enumerate(code):
        if len(set(buffer)) < pattern_len:
            buffer.append(char)
        else:
            break
    return idx


if __name__ == "__main__":
    code = read_file("./inputs/day6.txt")
    idx = find_marker(code)
    print(f"The solution is: {idx}")