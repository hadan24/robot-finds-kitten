import curses as c
from random import randrange, seed

w = c.initscr()
MAX_Y, MAX_X = w.getmaxyx()		# AKA lines, cols
c.endwin()

# Redefining arrow key codes because they're
#	different for me for some reason
c.KEY_UP = 450
c.KEY_LEFT = 452
c.KEY_DOWN = 456
c.KEY_RIGHT = 454

PLAYER_COLOR = 1

CAT = ('M', "")
CAT_COLOR = 2

OBJS = [
    ('B', ""),
	('d', ""),
	('@', ""),
	(':', ""),
	('8', "")
]
NUM_OBJS = len(OBJS)

OBJ_COLORS = [i for i in range(3, 9)]
NUM_OBJ_COLORS = len(OBJ_COLORS)