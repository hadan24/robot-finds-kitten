import curses as c
from random import randrange, seed

w = c.initscr()
MAX_Y, MAX_X = w.getmaxyx()		# AKA lines, cols
c.endwin()

# Redefining arrow key codes because they're
#	different for me for some reason
c.KEY_UP: int = 450
c.KEY_LEFT: int = 452
c.KEY_DOWN: int = 456
c.KEY_RIGHT: int = 454

PLAYER_COLOR: int = 1

CAT: tuple = ('M', "")
CAT_COLOR: int = 2

OBJS: list = [
	('B', ""),
	('d', ""),
	('@', ""),
	(':', ""),
	('8', "")
]
NUM_OBJS: int = len(OBJS)

# Curses color constants for reference
#	BLACK = 0
#	BLUE = 1
#	GREEN = 2
#	CYAN = 3
#	RED = 4
#	MAGENTA = 5
#	YELLOW = 6
#	WHITE = 7

OBJ_COLOR_OFFSET: int = 3
OBJ_GRAY: int = 0 + OBJ_COLOR_OFFSET
OBJ_BLUE: int = 1 + OBJ_COLOR_OFFSET
OBJ_GREEN: int = 2 + OBJ_COLOR_OFFSET
OBJ_CYAN: int = 3 + OBJ_COLOR_OFFSET
OBJ_RED: int = 4 + OBJ_COLOR_OFFSET
OBJ_MAGENTA: int = 5 + OBJ_COLOR_OFFSET
OBJ_YELLOW: int = 6 + OBJ_COLOR_OFFSET
OBJ_WHITE: int = 7 + OBJ_COLOR_OFFSET

OBJ_COLOR_PAIRS: list = [OBJ_GRAY, OBJ_BLUE, OBJ_GREEN,
	OBJ_CYAN, OBJ_RED, OBJ_MAGENTA, OBJ_YELLOW, OBJ_WHITE
]
NUM_OBJ_COLORS: int = len(OBJ_COLOR_PAIRS)