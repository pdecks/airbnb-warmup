"""Lego Blocks

You have 4 types of Lego blocks, of sizes (1x1x1), 1x1x2, 1x1x3, 1x1x4.
Assume that you have an infinite number of blocks of each type. For brevity,
we can call these types (1), (2), (3), and (4)

Using these blocks, you want to make a wall of height N and width M. The wall
should be a solid continuous structure with no holes. The wall should be
structurally connected so no straight vertical should exist that would allow the
wall to be separated in two without cutting one or more bricks.

INPUT:
first line: # test cases, The
subsequent T lines: N and M (space separated)

OUTPUT:
T lines, one for each test case, containing the number of ways to build the wall.


4
2 2
3 2
2 3
4 4

3
7
9
3375
"""