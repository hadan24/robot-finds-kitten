from defs import *
from player import player
from objects import object_list

# Game initializations and
#	curses settings not done in wrapper
def start(window):
	c.curs_set(0)
	c.init_pair(PLAYER_COLOR, c.COLOR_WHITE, c.COLOR_CYAN)

	seed()


def main(w):
	start(w)

	robot = player()
	w.addstr(5, 10, "h-hello?")
	w.refresh()

	ch = 0

	while ch != ord('q'):
		ch = w.getch()
		robot.move(ch)

		w.clear()
		robot.draw(w)
		w.refresh()
		


# Automatically turns off echo
# 	and turns on cbreak, keypad, colors (if supported)
c.wrapper(main)