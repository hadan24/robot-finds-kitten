from defs import *
from player import player
from objects import object_list

# Game initializations and
#	curses settings not done in wrapper
def start(window) -> None:
	c.curs_set(0)

	c.init_pair(PLAYER_COLOR, c.COLOR_WHITE, c.COLOR_CYAN)
	for i in range(NUM_OBJ_COLORS):
		c.init_pair(OBJ_COLOR_PAIRS[i],	i, c.COLOR_BLACK)

	seed()


def main(w):
	start(w)

	robot: player = player()
	objs: object_list = object_list(5)
	w.addstr(5, 10, "h-hello?")
	w.refresh()

	ch: int = 0

	while ch != ord('q'):
		ch = w.getch()
		robot.move(ch)

		w.clear()
		robot.draw(w)
		objs.draw_all(w)
		w.refresh()
		


# Automatically turns off echo
# 	and turns on cbreak, keypad, colors (if supported)
c.wrapper(main)