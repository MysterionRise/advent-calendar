"""
--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded
from the ships. Supplies are stored in stacks of marked crates, but because
the needed supplies are buried under many other crates, the crates need to
be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To
ensure none of the crates get crushed or fall over, the crane operator will
rearrange them in a series of carefully-planned steps. After the crates are
rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate
procedure, but they forgot to ask her which crate will end up where,
and they want to be ready to unload them as soon as possible so they can
embark.

They do, however, have a drawing of the starting stacks of crates and the
rearrangement procedure (your puzzle input). For example:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1 move 3 from 1 to 3 move 2 from 2 to 1 move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two
crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains
three crates; from bottom to top, they are crates M, C, and D. Finally,
stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure,
a quantity of crates is moved from one stack to a different stack. In the
first step of the above rearrangement procedure, one crate is moved from
stack 2 to stack 1, resulting in this configuration:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

In the second step, three crates are moved from stack 1 to stack 3. Crates
are moved one at a time, so the first crate to be moved (D) ends up below
the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates
are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in
this example, the top crates are C in stack 1, M in stack 2, and Z in stack
3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of
each stack?

--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice
the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly
wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air
conditioning, leather seats, an extra cup holder, and the ability to pick up
and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

However, the action of moving three crates from stack 1 to stack 3 means
that those three moved crates stay in the same order, resulting in this new
configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their
order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's
crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally
different order: MCD.

Before the rearrangement process finishes, update your simulation so that
the Elves know where they should stand to be ready to unload the final
supplies. After the rearrangement procedure completes, what crate ends up on
top of each stack?

"""
import copy
from typing import List

SIZE = 20000


def print_field(field):
    for _, row in enumerate(field):
        if len(set(row)) > 1:
            print(row)


def complete_start(start_pos):
    field = [[""] * 10] * SIZE
    row_indx = SIZE - 1
    for positions in reversed(start_pos[:-1]):
        values = positions.split(" ")
        cnt = 0
        idx = 0
        current_row = [""] * 10
        for v in values:
            if cnt == 4:
                idx += 1
                if len(v) > 0:
                    current_row[idx] = v[1]
                    idx += 1
                else:
                    current_row[idx] = ""
                cnt = 0
            elif v.startswith("["):
                current_row[idx] = v[1]
                cnt = 0
                idx += 1
            if v == "":
                cnt += 1
        field[row_indx] = current_row
        row_indx -= 1
    print(field)
    return field


def find_top_crate(
    field,
    from_pos,
):
    for idx, row in enumerate(field):
        if row[from_pos] != "":
            return idx, row[from_pos]
    return None


def find_empty_top_crate(field, from_pos):
    result = 0
    for idx, row in enumerate(field):
        if row[from_pos] == "":
            result = idx
    return result


def make_move(field, num_of_crates, from_pos, to_pos):
    new_field = copy.deepcopy(field)
    values_to_move = []
    for _ in range(num_of_crates):
        from_idx, val = find_top_crate(new_field, from_pos)
        new_field[from_idx][from_pos] = ""
        values_to_move.append(val)
    for i, val in enumerate(reversed(values_to_move)):
        to_idx = find_empty_top_crate(new_field, to_pos)
        print(to_idx)
        row_to_update = copy.deepcopy(new_field[to_idx])
        row_to_update[to_pos] = val
        new_field[to_idx] = row_to_update
    print_field(new_field)
    return new_field


def find_top_crates(field) -> List[str]:
    result = [""] * 10
    for idx, row in enumerate(field):
        for jdx, crate in enumerate(row):
            if crate != "" and result[jdx] == "":
                result[jdx] = crate
    return result


def main():
    """
    main solver function
    """
    with open("supply_stacks.txt", encoding="utf-8") as file:
        lines = file.readlines()

        start_pos = []
        not_started = True
        field = None
        for line in lines:
            if line == "\n" and not_started:
                field = complete_start(start_pos)
                not_started = False
            elif not_started:
                start_pos.append(line.replace("\n", ""))
            else:
                # execute move
                move = line.strip().split(" ")
                num_of_crates = int(move[1])
                from_pos = int(move[3]) - 1
                to_pos = int(move[5]) - 1
                field = make_move(field, num_of_crates, from_pos, to_pos)
        print("".join(find_top_crates(field)))


if __name__ == "__main__":
    main()
