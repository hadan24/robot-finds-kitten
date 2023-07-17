import curses as c
from random import randrange, seed

PLAYER_COLOR_PAIR: int = 1

CAT: tuple = ('M', "Congratulations! You found kitten!")
CAT_COLOR_PAIR: int = 2

OBJS: list = [
	('I', "battery test"),
	('d', "charger test"),
	('@', "wall test"),
	(':', "socket test"),
	('8', "camera test")
]
NUM_OBJS: int = len(OBJS)

# Reassigning curses colors to a (personally) more memorable order
#	and to redefine their RGB values (if possible) for consistency
# 	across many different terminals
COLOR_BLACK: int = 0
COLOR_GRAY: int = 1
COLOR_WHITE: int = 2
COLOR_RED: int = 3
COLOR_GREEN: int = 4 
COLOR_BLUE: int = 5
COLOR_YELLOW: int = 6
COLOR_CYAN: int = 7
COLOR_MAGENTA: int = 8
COLOR_ORANGE: int = 9
COLOR_PURPLE: int = 10
COLOR_LAVENDER: int = 11

OBJ_COLOR_PAIR_OFFSET: int = 2
OBJ_GRAY_PAIR: int = COLOR_GRAY + OBJ_COLOR_PAIR_OFFSET
OBJ_WHITE_PAIR: int = COLOR_WHITE + OBJ_COLOR_PAIR_OFFSET
OBJ_RED_PAIR: int = COLOR_RED + OBJ_COLOR_PAIR_OFFSET
OBJ_GREEN_PAIR: int = COLOR_GREEN + OBJ_COLOR_PAIR_OFFSET
OBJ_BLUE_PAIR: int = COLOR_BLUE + OBJ_COLOR_PAIR_OFFSET
OBJ_YELLOW_PAIR: int = COLOR_YELLOW + OBJ_COLOR_PAIR_OFFSET
OBJ_CYAN_PAIR: int = COLOR_CYAN + OBJ_COLOR_PAIR_OFFSET
OBJ_MAGENTA_PAIR: int = COLOR_MAGENTA + OBJ_COLOR_PAIR_OFFSET
OBJ_ORANGE_PAIR: int = COLOR_ORANGE + OBJ_COLOR_PAIR_OFFSET
OBJ_PURPLE_PAIR: int = COLOR_PURPLE + OBJ_COLOR_PAIR_OFFSET
OBJ_LAVENDER_PAIR: int = COLOR_LAVENDER + OBJ_COLOR_PAIR_OFFSET

OBJ_COLOR_PAIRS: list = [ OBJ_GRAY_PAIR, OBJ_WHITE_PAIR,
	OBJ_RED_PAIR, OBJ_GREEN_PAIR, OBJ_BLUE_PAIR,
	OBJ_YELLOW_PAIR, OBJ_CYAN_PAIR, OBJ_MAGENTA_PAIR,
	OBJ_ORANGE_PAIR, OBJ_PURPLE_PAIR, OBJ_LAVENDER_PAIR
]
NUM_OBJ_COLOR_PAIRS: int = len(OBJ_COLOR_PAIRS)

w = c.initscr()

MAX_Y, MAX_X = w.getmaxyx()		# AKA lines, cols
# Setting play area bounds to be 1 less than actual window bounds
#	to prevent errors from writing to lower right corner
#	(that's apparently a part of Python curses:
# https://docs.python.org/3/library/curses.html#window-objects)
MIN_Y = 1
MIN_X = 1
MAX_Y -= 1
MAX_X -= 1

c.endwin()
