def run(x):
    x = x.split("\n")
    print(tobbogan(x, 3, 1))
    print(tobbogan2(x))


def tobbogan(input, r, d):
    x, y, count = r, d, 0
    width = len(input[0])
    while y < len(input):
        count += input[y][x % width] == "#"
        x += r
        y += d
    return count


def tobbogan2(x):
    from functools import reduce

    pairs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return reduce(mul, map(lambda y: tobbogan(x, y[0], y[1]), pairs))


def mul(x, y):
    return x * y


if __name__ == "__main__":
    x = """.#.....#..#..#....##.........#.
...#...#.........#..#.#..#.....
#.#...#.#....#.....#..#..##..##
..#..#.#.#.....#..#..#..##.....
.#..........#....####..##.#..#.
....##.......#.#.....#.........
....#......#....####.#.##......
........##..........##......#..
.........#........##..#.#.....#
.#..##..........#..#...#..##.#.
........#........#.....#....#.#
..#.......#.###...#.......##...
.##..##.#...#........#.........
...#....#..#..#..##.......#..#.
.#.#.##.##..##..#.#.....#.....#
....#.........#........#....##.
........#........#....###.#..#.
........#....#......##.........
.###.##.#.............##.......
....#.........#...#.#.##..#....
#.............#.#.#.#..#..#..##
###...###.###..#........#......
##..#.....#....##..##..........
.......#...#....#...#...#.....#
...#......###...##.###...#...#.
#.......#...##..#.......#..#...
.....##....#....#..#..#.#.##..#
.........#....##.#.#..##.#.....
.....#......#.#.#.....#.....#..
..#..#...#.#...#.........##.#..
.....#..#.................#.#..
##.#....##........#......#.....
#..#...##...#.#.#..#...........
.#..####.....#......#.###......
.#.......##............#....#..
.#.........##..#.##...#.....###
....##.........#.#...####...##.
..#.......#......##.....#.#..#.
...##....#..#..##....##...#.#.#
.................#.............
...#.##..#.##..............#...
...#......#.........##........#
..#.#..##...#.......#.#........
.###.#.....#.##.##.#...#...#...
.....#.##.....#..#......#..#...
.....#.#...#........#..#..#..#.
#...#.##.#....#................
..#...#.#..#.....#.#.#.........
#.#.###...#.....##........##...
#..##.##....#..........##.#...#
...#..#.#.###...##......#.#....
.#..#........##...#......#.#.#.
##........###....#.#....#......
....#...........#.........#....
#.#....#..#.....#.#....#.....#.
........###.......#..#.#.#.#.#.
..#....#.....#...............##
.....#..##....#.#...####.......
.#..#.....#..#.....#....#....#.
..##....#...........#.#....#...
..#.#......#..#.#..#.....###.#.
...........................##..
##.....#....#......###.#...#..#
...#...#.........#..#..#....#..
....#####.#.#.#....#..#........
.##.#..#.#............###......
##.#...##...##....#...#...##...
..#.#.....#.......#..##..###.##
#..##...........#.##.....#.##..
#...#....#...#..##...#.#...#.#.
.#..#...........###...#.#...#..
.#.....#......#.#......#...#..#
.#...##.##...............#....#
..#.........#....#.............
.#..##..#.#................#...
..#.#.#.#.................#.#.#
...#..#.#..#.#......#........#.
##....#......###.#......#......
..#....##.....#..#........#....
.#.#....#...#.#.....###..#...#.
.#..#...##.....#.#...#.....#.#.
...#....#....##....##.....#....
.......#...#...##..#.#.......#.
.###..#..###.#.#.#.#.#.....##..
....#.#......###.#....#....#..#
##.....#.....##.#.....#....#...
......#...##...#..#.#.....#....
...#.........###.....#..##.....
....#...#..#....#..#.........##
.#........#..#.....#.##.#....#.
.......#......#.##...##.#..#...
#......#.......##..##..#.#.....
..#.##..........#.#..#......#..
#.....#.......#......#.........
...##......##...........#.#....
.#....#........#...#.#..#.....#
.#...#...##......##...##...##.#
.#.#.##.....##....#.#.#..#.....
...#..#........#.....#.#.#####.
#..#..#......#....##....##.....
.#.............#....###.##.#...
.#....#.......#.#.....#......##
#..#.#.#........#...#..#...#...
#.#.#.....#.......#.##..#.....#
..#....#.....#...##.#...##.....
......#..#.............###...#.
..#...#.#....###...#...........
.........#..#..#....#..#.......
#....#.....#..#....#.#..##.....
.#..#.#.....#...##.....##......
.....####..#..#......#....##..#
#.#....#....#.##.......#.#.....
....#.#.............##..#.#...#
....#.#.#.....##.....##..#...#.
.#..#...#....#...#.#....#...#..
.#..#.#.#.......#...#..........
...##..#..#...##.....#.......#.
..##...##.#..#.......#.........
.##.#.......##...#...#......#.#
##.#.#..#...#............#.....
..#.##...##..#....##..#......#.
...#..........#.....#.#........
...#..#..#.......#.#.....##....
##.............#.....#.##...#..
#.#......#........#...#.##..#.#
...#..#...##.#.#........#.#....
#.....##...........#....#......
...##....#..#.#...#........#...
..##..####..#..#...............
.#.#..#......#.##.........##.#.
.##....#...##.#...#..##..#.....
........#........#.###.#.#....#
......##...#......#..#..#......
..#.......#...#..##........#..#
.#....###..###....###...##.#.##
#.#....#..#.#...#.#...##...#...
..#..##......#..#......####....
.#....###.......#...##...#.....
...#....#..#.....#..#...####.#.
............#.####..##...#..##.
.#..#.......#....#...#......#.#
.......#.......#..#.#..........
...#.#............#..#......#..
..#...........#...##......#...#
...##......#.........#.#...#.##
.#..#..#..#......#...........#.
....#.....#.###........#.......
..##.#.#........#.#...##....#..
.#.#........##....#...#......#.
.......#.##..###...............
#..#...##.....##........##....#
...####........#...#.........##
...#..............##..#........
......#.....#....#.......#....#
..###......#..##.....##....##..
##...#.....#..#.#.#...#.....#..
...#....#............#.........
..#..##...#..#.........#.......
.#.#.#...##..........#..###....
.......##.#.#.#...#.#...#.....#
..#..#..#..#...###.....#.##....
.#.#.....#.....##.#..#...###..#
.........#..##......##...##.#.#
#.........##..#......#..#.#.#..
.#..##.#.##......##........#...
..#...#.....##..#......#.....##
.#..#...#......#..#...#.....##.
..#..##...#.....#.....#........
....##..#....#.#....#......#.#.
..#.......##..#..#.##.#..#...##
...#..........#...#..##........
..#............#.#......#......
.#...##.......#...#.#........#.
.#...#....#..#....#....#.#...#.
......#..#.#..#..............#.
.....#.##.#...............##.##
.#...............#.....#..#...#
.#..##.......#.#...#..#..#....#
..#..###.##........##..........
.#....#..##...#.#.........#....
.......#.....#....###...##.#.#.
##..#.#...##.##.##....##.#.###.
#.#...........#..#.#...........
....#..#..#..#...#....#.......#
........##....#..#......##.#...
.#.#..##...##...#....#..#.###..
#..##....#..#...#.......##.....
..###..#.###......#..####....#.
.....#..#........##.#..#.......
.#......##..............#.#.#..
..#.#.......##...#....#.#.###..
#..#..#...###..#...............
......#..#.....#..#..#...#.....
.#...#..........###..#..#.#....
.#......##..#......#.....###..#
.......#...#..#....###.....#...
#....#.......###.##.....##....#
..#.....#..##..#.........##....
.....##....#.#......#..........
....#...#...#......##.....##.#.
........#.#.#......#...........
.#....#...#...#....#.....#...#.
..............#..##.#.....###.#
.#......##.....##...#....#.....
.............#.##......#.....#.
.#....#.#............#.#..##...
.#...##.......#..#...##....#...
.#.....#..........#............
#.#.#........#.....#..#....##..
#....#.##......#...#...........
........#.##.....#...##.....#..
..#.##....#.##.#...#.#.#....#..
......#.......####......#.#...#
#...#.##.####......#.....##....
.#..#....#.......#...##.....#..
................#......#.##....
###...##..#.#..........#....#.#
#.#..#.....#..##.##.##...#...##
..#.......#.......#..##..#..##.
......#.##.......#..#.....#...#
.##..##..#.#.......#..#......#.
....##.#....#...##.#..#.....#.#
..#..#.........###.#...........
....#.......#....##......#....#
..........#...#......#....#...#
..#.#....###.....#..#.#.#..#...
.....#...##..#.##........####..
##.............#....##........#
..#..........#..##.#...........
##.#.......#.#....#......#.#...
........####.....##.#.........#
.....#...#.#.....#.##..##.#....
........#...#.#.#.#...#......#.
.#..#.#....#.#...##.....#..#...
.....#.#............#.#.#......
....##.#...#...#.##...##.......
.........#.##.....#.......#...#
...........###....#.#....#...#.
.#..#.###......#..#............
#...#..#......#.#...#......#...
..##.#.#........#........##..##
..#.#.##..##....#........#.#.#.
...#........###......#.#.....#.
#.#.#.##........#.#...#..#.....
#..#...............#...#.#...#.
.....##......#...#.....#..#....
............#...#...#.##.#....#
...#..#..#...##.#....#.#..#.#..
##.#..#..............##........
.#.#..#.#..#....##..#.#.##.##..
......######....##.....#.......
.#.......#..........#.#..#.#..#
..........#.#......#...##......
#..........#.#..#.............#
...#...#..#....................
....#...#.....#.....##.....#...
..#....##.....#..#......#......
.#.#.....#..##.##..........###.
.#.##....#....#....#....#...#..
..##.....................##.#..
.....#..##....#.#.....##..#....
.####...#...##..#.##...#..#....
.........#.#...#.......###.....
...#..#........#..#..##.....#..
..#....#....#....###.....#.....
......#....#..#.........#......
#.#...#..#..#.#...#..#.#......#
..........#..........#.#.##....
.#..###..##..#....#.#.....#..#.
.##......#..#.##...#.........#.
...##...#....#.........#..#....
....#..##........#.........#...
.........##....#...#.#.....#..#
.#..........##...#..#.#..##....
#.......#...#...#............#.
.....##.#.##.......#.......#...
...........#...#.....###.....#.
#..................#.##..##...#
.........##.............#...#.#
#.#.....##...#........###....##
...##..#.##.....###.....#......
..#...#.#..#......##.#.......#.
.........##.#...........###..#.
..#...#.....#...#.#.....#..#...
.....##..#...#.#.#....#.....###
..#.#....#..#..#..#....#.#...#.
........##....#......#....#..#.
.##..#.....#.#....#..#.###.....
..............##.........#.#.#.
.##....#.#..#..#...#..........#
.....##.......#....#..#......#.
...#.#....................#..##
#.##..#.#...#...#....#.#....##.
...#.#..#.###................#.
.....##..#.##.#.#.........#.#..
.................##..........#.
..#......#........#.#....#.....
#......##......#......###....#.
....##....#..#..####......#...#
.##.##.........#...#..#....#.#.
.#..#....##...##..#...........#
#...#......#...#...........#...
...#...####.............##..#..
.....#....##............##....#
......##.#...##...........#.#..
..#......##.....###.......#.###
...#...#......#...##.#........#
.#.........##.##......##.......
....................#....#....#
.#.#.#........##.#....#.....#..
#.#.....####..#.........#.#.#..
...####..#..............#.#....
....#.#....#..........#....#...
.#..#..#.#...#..#.#............
.#.#.......##........##.....#..
#.#.##..#.....##......##....#.#
......#...#...#...#......#.....
.........##..#.....#.####.#.#..
.....#....#.###...#.###.#..#..#
..#.#..#..#.......#.......##...
.....#.........#......##.#....#
..#.#.##....#.#...............#
.....#..#....##......##..###..."""
    run(x)
