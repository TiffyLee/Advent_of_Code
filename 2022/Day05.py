"""
author: Tiffany Lee
file: /Users/tiffanylee/Downloads/Personal Projects/Advent_of_Code/2022/InputFiles_2022/Day05_Input.txt

--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded
from the ships. Supplies are stored in stacks of marked crates, but because
the needed supplies are buried under many other crates, the crates need to be
rearranged. The ship has a giant cargo crane capable of moving crates between
stacks. To ensure none of the crates get crushed or fall over, the crane operator
will rearrange them in a series of carefully-planned steps. After the crates are
rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate
procedure, but they forgot to ask her which crate will end up where,
and they want to be ready to unload them as soon as possible so they can embark.
They do, however, have a drawing of the starting stacks of crates and the
rearrangement procedure (your puzzle input).
For example:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates.
Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top.
Stack 2 contains three crates; from bottom to top, they are crates M, C, and D.
Finally, stack 3 contains a single crate, P.
Then, the rearrangement procedure is given. In each step of the procedure,
a quantity of crates is moved from one stack to a different stack.
In the first step of the above rearrangement procedure, one crate is moved from
stack 2 to stack 1, resulting in this configuration:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

In the second step, three crates are moved from stack 1 to stack 3.
Crates are moved one at a time, so the first crate to be moved (D) ends up
below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are
moved one at a time, crate C ends up below crate M:

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

The Elves just need to know which crate will end up on top of each stack;
in this example, the top crates are C in stack 1, M in stack 2,
and Z in stack 3, so you should combine these together and give the Elves
the message CMZ.

After the rearrangement procedure completes,
what crate ends up on top of each stack?


--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice
the process isn't following your prediction. Some mud was covering the writing
on the side of the crane, and you quickly wipe it away. The crane isn't a
CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features:
air conditioning, leather seats, an extra cup holder, and the ability to pick up
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
that those three moved crates stay in the same order, resulting in this
new configuration:

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

In this example, the CrateMover 9001 has put the crates in a totally different
order: MCD.
Before the rearrangement process finishes, update your simulation so that the
Elves know where they should stand to be ready to unload the final supplies.

After the rearrangement procedure completes,
what crate ends up on top of each stack?

"""
from copy import deepcopy

def part1(mover9000, num, toC, fromC):
    mover9000[toC] = mover9000[fromC][:num][::-1] + mover9000[toC]
    mover9000[fromC] = mover9000[fromC][num:]

def part2(mover9001, num, toC, fromC):
    mover9001[toC] = mover9001[fromC][:num] + mover9001[toC]
    mover9001[fromC] = mover9001[fromC][num:]

def main():
    filepath = "/Users/tiffanylee/Downloads/Personal Projects/Advent_of_Code/2022/InputFiles_2022/Day05_Input.txt"
    info = [line for line in open(filepath).read().split("\n")]
    allCrates = []
    for line in info:
        if line == "": break
        lineSize = (len(line) + 1) // 4
        while len(allCrates) < lineSize:
            allCrates.append([])
        for i in range(len(allCrates)):
            crate = line[i * 4 + 1]
            if "A" <= crate <= "Z":
                allCrates[i].append(crate)

    mover9000 = deepcopy(allCrates)
    mover9001 = deepcopy(allCrates)

    for cmd in info:
        if not cmd.startswith("move"):
            continue
        words = cmd.split()
        num = int(words[1])
        fromC = int(words[3]) - 1
        toC = int(words[5]) - 1
        part1(mover9000, num, toC, fromC)
        part2(mover9001, num, toC, fromC)
    print("Part One: After the rearrangement procedure completes, "
          + "what crate ends up on top of each stack? (CrateMover9000)"
          + "\nANSWER: " + "".join(top[0] for top in mover9000 if len(top) > 0))
    print("\nPart Two: After the rearrangement procedure completes, "
          + "what crate ends up on top of each stack? (CrateMover9001)"
          + "\nANSWER: " + "".join(top[0] for top in mover9001 if len(top) > 0))
main()