EXAMPLE_2 = [
"             Z L X W       C                 ",
"             Z P Q B       K                 ",
"  ###########.#.#.#.#######.###############  ",
"  #...#.......#.#.......#.#.......#.#.#...#  ",
"  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  ",
"  #.#...#.#.#...#.#.#...#...#...#.#.......#  ",
"  #.###.#######.###.###.#.###.###.#.#######  ",
"  #...#.......#.#...#...#.............#...#  ",
"  #.#########.#######.#.#######.#######.###  ",
"  #...#.#    F       R I       Z    #.#.#.#  ",
"  #.###.#    D       E C       H    #.#.#.#  ",
"  #.#...#                           #...#.#  ",
"  #.###.#                           #.###.#  ",
"  #.#....OA                       WB..#.#..ZH",
"  #.###.#                           #.#.#.#  ",
"CJ......#                           #.....#  ",
"  #######                           #######  ",
"  #.#....CK                         #......IC",
"  #.###.#                           #.###.#  ",
"  #.....#                           #...#.#  ",
"  ###.###                           #.#.#.#  ",
"XF....#.#                         RF..#.#.#  ",
"  #####.#                           #######  ",
"  #......CJ                       NM..#...#  ",
"  ###.#.#                           #.###.#  ",
"RE....#.#                           #......RF",
"  ###.###        X   X       L      #.#.#.#  ",
"  #.....#        F   Q       P      #.#.#.#  ",
"  ###.###########.###.#######.#########.###  ",
"  #.....#...#.....#.......#...#.....#.#...#  ",
"  #####.#.###.#######.#######.###.###.#.#.#  ",
"  #.......#.......#.#.#.#.#...#...#...#.#.#  ",
"  #####.###.#####.#.#.#.#.###.###.#.###.###  ",
"  #.......#.....#.#...#...............#...#  ",
"  #############.#.#.###.###################  ",
"               A O F   N                     ",
"               A A D   M                     "
]

# inner to outer
EXAMPLE_2_INCREASE_DEPTH = {
    (8, 13): (34, 19),      # FD
    (8, 21): (25, 2),       # RE
    (8, 23): (17, 42),      # IC
    (8, 31): (13, 42),      # ZH
    (13, 8): (34, 17),      # OA
    (17, 8): (2, 27),       # CK
    (23, 8): (15, 2),       # CJ
    (28, 17): (21, 2),      # XF
    (28, 21): (2, 17),      # XQ
    (28, 29): (2, 15),      # LP
    (23, 36): (34, 23),     # NM
    (21, 36): (25, 42),     # RF
    (13, 36): (2, 19),      # WB
}

# outer to inner
EXAMPLE_2_DECREASE_DEPTH = {
    (34, 19): (8, 13),      # FD
    (25, 2): (8, 21),       # DE
    (17, 42): (8, 23),      # IC
    (13, 42): (8, 31),      # ZH
    (34, 17): (13, 8),      # OA
    (2, 27): (17, 8),       # CK
    (15, 2): (23, 8),       # CJ
    (21, 2): (28, 17),      # XF
    (2, 17): (28, 21),      # XQ
    (2, 15): (28, 29),      # LP
    (34, 23): (23, 36),     # NM
    (25, 42): (21, 36),     # RF
    (2, 19): (13, 36),      # WB
}