def solution():
    top3 = [0, 0, 0]
    with open("./inputs/day1.txt", "r") as f:
        current_elf_cals = 0
        for line in f:
            if line.strip():
                current_elf_cals += int(line)
            else:
                if current_elf_cals > top3[0]:
                    top3[0] = current_elf_cals
                    top3 = sorted(top3)

                current_elf_cals = 0

    return sum(top3)


if __name__ == "__main__":
    answer = solution()
    print(f"The solution is: {answer}")
