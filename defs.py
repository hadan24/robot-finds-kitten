import curses as c
from random import randrange, seed

PLAYER_COLOR_PAIR: int = 1
PLAYER_CHAR: chr = '#'

CAT: tuple[chr, str] = ('M', " Congratulations! You found kitten! ")
CAT_COLOR_PAIR: int = 2

OBJS: list[tuple[chr, str]] = [
	('I', " A battery! Some much-needed juice. "),
	('d', " This portable charger can keep you going for a bit. "),
	('@', " Drats, a wall. Gonna have to go around it. "),
	(':', " A wall socket. Seems like a good time to plug in. "),
	('*', " Enhanced parts! These'll save a few steps. ")
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
GRAY_PAIR: int = COLOR_GRAY + OBJ_COLOR_PAIR_OFFSET
WHITE_PAIR: int = COLOR_WHITE + OBJ_COLOR_PAIR_OFFSET
RED_PAIR: int = COLOR_RED + OBJ_COLOR_PAIR_OFFSET
GREEN_PAIR: int = COLOR_GREEN + OBJ_COLOR_PAIR_OFFSET
BLUE_PAIR: int = COLOR_BLUE + OBJ_COLOR_PAIR_OFFSET
YELLOW_PAIR: int = COLOR_YELLOW + OBJ_COLOR_PAIR_OFFSET
CYAN_PAIR: int = COLOR_CYAN + OBJ_COLOR_PAIR_OFFSET
MAGENTA_PAIR: int = COLOR_MAGENTA + OBJ_COLOR_PAIR_OFFSET
ORANGE_PAIR: int = COLOR_ORANGE + OBJ_COLOR_PAIR_OFFSET
PURPLE_PAIR: int = COLOR_PURPLE + OBJ_COLOR_PAIR_OFFSET
LAVENDER_PAIR: int = COLOR_LAVENDER + OBJ_COLOR_PAIR_OFFSET

OBJ_COLOR_PAIRS: list[int] = [ GRAY_PAIR, WHITE_PAIR,
	RED_PAIR, GREEN_PAIR, BLUE_PAIR,
	YELLOW_PAIR, CYAN_PAIR, MAGENTA_PAIR,
	ORANGE_PAIR, PURPLE_PAIR, LAVENDER_PAIR
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
