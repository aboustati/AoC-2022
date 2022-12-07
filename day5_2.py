from collections import deque
from copy import deepcopy
from itertools import takewhile
from typing import List, Tuple, NamedTuple, Deque, Dict


def _read_file(path) -> List[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
    return lines


class Move(NamedTuple):
    num: int
    from_: int
    to: int

    @classmethod
    def from_string(cls, string: str) -> 'Move':
        words = string.split(" ")
        return cls(int(words[1]), int(words[3]), int(words[5]))


class Instructions:
    def __init__(self, instructions: List[Move]):
        self._instruction_set = instructions

    @property
    def instruction_set(self) -> List[Move]:
        return self._instruction_set

    @classmethod
    def from_file(cls, path) -> 'Instructions':
        lines = _read_file(path)

        instructions = [
            Move.from_string(line) for line in lines if line.startswith("move")
        ]
        return cls(instructions)

    def execute(self, stack) -> 'Stack':
        new_stack = deepcopy(stack)
        for instruction in self.instruction_set:
            moved_cargo = new_stack[instruction.from_].popleft(instruction.num)
            new_stack[instruction.to].extendleft(moved_cargo)
        return new_stack


class FlexColumn(Deque):
    def popleft(self, n=1) -> Deque:
        popped = deque()
        if n > len(self):
            n = len(self)
        for _ in range(n):
            popped.appendleft(super().popleft())
        return popped

    @classmethod
    def from_strings(cls, list_of_strings: List[str],
                     stack_id: int) -> 'FlexColumn':
        column = []
        string_idx = 1 + 4 * (stack_id - 1)
        for string in list_of_strings:
            crate = string[string_idx]
            if crate != " ":
                column.append(crate)

        return cls(column)


class Stack(Dict):
    @classmethod
    def from_file(cls, path: str) -> 'Stack':
        lines = _read_file(path)
        lines = list(takewhile(lambda x: x.strip(), lines))
        crate_idxs = [int(idx) for idx in lines[-1].split()]

        return cls(
            {idx: FlexColumn.from_strings(lines[:-1], idx)
             for idx in crate_idxs})


if __name__ == "__main__":
    instructions = Instructions.from_file("./inputs/day5.txt")
    stack = Stack.from_file("./inputs/day5.txt")
    new_stack = instructions.execute(stack)
    print(f"The solution is: {''.join([top[0] for top in new_stack.values()])}")
