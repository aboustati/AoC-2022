def solution():
    max_calories = 0
    with open("./inputs/day1.txt", "r") as f:
        current_elf_cals = 0
        for line in f:
            if line.strip():
                current_elf_cals += int(line)
            else:
                if current_elf_cals > max_calories:
                    max_calories = current_elf_cals

                current_elf_cals = 0

    return max_calories


if __name__ == "__main__":
    answer = solution()
    print(f"The solution is: {answer}")
