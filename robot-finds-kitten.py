from defs import *
from player import player
from objects import object_list

# Game initializations and
#	curses settings not done in wrapper
def start(window) -> None:
	c.curs_set(0)
	
	# Redefining curses color RGB values to
	#	(hopefully) be consistent across terminals
	if c.can_change_color():
		c.init_color(COLOR_BLACK, 0, 0, 0)
		c.init_color(COLOR_GRAY, 300, 300, 300)
		c.init_color(COLOR_WHITE, 800, 800, 800)
		c.init_color(COLOR_RED, 800, 0, 0)
		c.init_color(COLOR_GREEN, 0, 800, 0)
		c.init_color(COLOR_BLUE, 350, 350, 1000)
		c.init_color(COLOR_YELLOW, 800, 800, 0)
		c.init_color(COLOR_CYAN, 0, 800, 800)
		c.init_color(COLOR_MAGENTA, 800, 0, 800)
		c.init_color(COLOR_ORANGE, 800, 600, 0)
		c.init_color(COLOR_PURPLE, 500, 0, 800)
		c.init_color(COLOR_LAVENDER, 600, 600, 800)

	c.init_pair(PLAYER_COLOR_PAIR, COLOR_BLACK, COLOR_CYAN)
	c.init_pair(CAT_COLOR_PAIR, COLOR_GRAY, COLOR_ORANGE)
	for i in range(NUM_OBJ_COLOR_PAIRS):
		c.init_pair(OBJ_COLOR_PAIRS[i], i+1, COLOR_BLACK)
	
	seed()


def main(w):
	start(w)

	robot: player = player()
	objs: object_list = object_list(5)
	w.addstr(5, 10, "h-hello?", c.color_pair(0))
	w.refresh()

	ch: int = 0

	while ch != ord('q'):
		ch = w.getch()
		check_x, check_y = robot.get_collision_coordinates(ch)
		
		if objs.check_collisions(check_x, check_y):
			objs.interact(check_x, check_y, w)
		else:
			robot.move(ch)

		w.clear()
		w.addstr(f"{check_x, check_y}")
		robot.draw(w)
		objs.draw_all(w)
		w.refresh()
		


# Automatically turns off echo
# 	and turns on cbreak, keypad, colors (if supported)
c.wrapper(main)