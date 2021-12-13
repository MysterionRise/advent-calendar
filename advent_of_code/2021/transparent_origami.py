"""
--- Day 13: Transparent Origami ---

You reach another volcanically active part of the cave. It would be nice if
you could do some kind of thermal imaging so you could tell ahead of time
which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When
you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise,
you manage to find the manual; as you go to open it, page 1 falls out. It's
a large sheet of transparent paper! The transparent paper is marked with
random dots and includes instructions on how to fold it up (your puzzle
input). For example:

6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5

The first section is a list of dots on the transparent paper. 0,0 represents
the top-left coordinate. The first value, x, increases to the right. The
second value, y, increases downward. So, the coordinate 3,0 is to the right
of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example
form the following pattern, where # is a dot on the paper and . is an empty,
unmarked position:

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........

Then, there is a list of fold instructions. Each instruction indicates a
line on the transparent paper and wants you to fold the paper up (for
horizontal y=... lines) or left (for vertical x=... lines). In this example,
the first fold instruction is fold along y=7, which designates the line
formed by all of the positions where y is 7 (marked here with -):

...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........

Because this is a horizontal line, fold the bottom half up. Some of the dots
might end up overlapping after the fold is complete, but dots will never
appear exactly on a fold line. The result of doing this fold looks like this:

#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........
Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the
transparent paper is folded; after the fold is complete, those dots appear
in the top left corner (at 0,0 and 0,1). Because the paper is transparent,
the dot just below them in the result (at 0,3) remains visible, as it can be
seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots
merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....
Because this is a vertical line, fold left:

#####
#...#
#...#
#...#
#####
.....
.....
The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing
the first fold. After the first fold in the example above, 17 dots are
visible - dots that end up overlapping after the fold is completed count as
a single dot.

How many dots are visible after completing just the first fold instruction
on your transparent paper?

--- Part Two ---

Finish folding the transparent paper according to the instructions. The
manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?
"""


def main():
    """
    main solver function
    """
    with open("transparent_origami.txt", encoding="utf-8") as file:
        lines = file.readlines()
        x_max = 0
        y_max = 0
        for line in lines:
            if "fold" not in line:
                x_coord, y_coord = [int(x) for x in line.split(",")]
                x_max = max(x_max, x_coord)
                y_max = max(y_max, y_coord)

        field = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]
        for line in lines:
            if "fold" not in line:
                x_coord, y_coord = [int(x) for x in line.split(",")]
                field[y_coord][x_coord] = 1
            elif line != "\n":
                folding_instruction = line.split(" ")[2]
                if "y=" in folding_instruction:
                    y_coord = int(line.split("=")[1])
                    for x_c in range(y_coord + 1, len(field)):
                        for y_c in range(x_max + 1):
                            if field[x_c][y_c] == 1:
                                field[x_c][y_c] = 0
                                field[y_coord - (x_c - y_coord)][y_c] = 1
                else:
                    x_coord = int(line.split("=")[1])
                    for x_c in range(y_max + 1):
                        for y_c in range(x_coord + 1, len(field[0])):
                            if field[x_c][y_c] == 1:
                                field[x_c][y_c] = 0
                                field[x_c][x_coord - (y_c - x_coord)] = 1
                count = 0
                for _, row in enumerate(field):
                    for _, val in enumerate(row):
                        if val == 1:
                            count += 1
                print(count)
        for i in range(10):
            for j in range(100):
                if field[i][j] == 1:
                    print("1", end="")
                else:
                    print(" ", end="")
            print()


if __name__ == "__main__":
    main()
