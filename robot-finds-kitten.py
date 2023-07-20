from defs import *
from player import player
from objects import object_list

# Game initializations and
#	curses settings not done in wrapper
def start() -> None:
	c.curs_set(0)
	
	# Redefining curses color RGB values to
	#	(hopefully) be consistent across terminals
	if c.can_change_color():
		c.init_color(COLOR_BLACK, 0, 0, 0)
		c.init_color(COLOR_GRAY, 500, 500, 500)
		c.init_color(COLOR_WHITE, 800, 800, 800)
		c.init_color(COLOR_RED, 800, 0, 0)
		c.init_color(COLOR_GREEN, 0, 800, 0)
		c.init_color(COLOR_BLUE, 350, 350, 1000)
		c.init_color(COLOR_YELLOW, 800, 800, 0)
		c.init_color(COLOR_CYAN, 0, 800, 800)
		c.init_color(COLOR_MAGENTA, 800, 0, 800)
		c.init_color(COLOR_ORANGE, 800, 600, 200)
		c.init_color(COLOR_PURPLE, 500, 300, 800)
		c.init_color(COLOR_LAVENDER, 600, 600, 800)

	c.init_pair(PLAYER_COLOR_PAIR, COLOR_BLACK, COLOR_CYAN)
	c.init_pair(CAT_COLOR_PAIR, COLOR_BLACK, COLOR_ORANGE)
	for i in range(NUM_OBJ_COLOR_PAIRS):
		c.init_pair(OBJ_COLOR_PAIRS[i], i+1, COLOR_BLACK)
	
	seed()

def title_screen(window) -> None:
	window.clear()
	title_attribute = c.color_pair(0) | c.A_BOLD
	title_line: int = 2
	left_margin: int = 5

	welcome: str = "Welcome to Robot Finds Kitten - Dan Edition!"

	player_char: str = "In this game, you play as robot: "
	goal: str = "And you must get to kitten: "

	battery: str = "But, you must do so before your battery runs out. "
	battery_UI: str = "(You can check it in the top right corner.)"

	controls: str = "Use WASD or the arrow keys to move. "
	wasd_offset: int = 4
	arrow_keys_offest: int = 16
	begin: str = "Press almost any key to start playing. "
	quit: str = "Press Q at any time to quit."
	q_offset: int = 6

	sendoff: str = "Good luck, friend."

	window.addstr(title_line, left_margin, welcome,
		title_attribute | c.A_UNDERLINE)

	window.addstr(title_line+2, left_margin, player_char, title_attribute)
	window.addch(title_line+2, left_margin+len(player_char),
	 	PLAYER_CHAR, c.color_pair(PLAYER_COLOR_PAIR))

	window.addstr(title_line+3, left_margin, goal, title_attribute)
	window.addch(title_line+3, left_margin+len(goal), CAT[0],
		c.color_pair(CAT_COLOR_PAIR))

	window.addstr(title_line+5, left_margin, battery, title_attribute)
	window.addstr(title_line+5, left_margin+len(battery), battery_UI,
		c.color_pair(BLUE_PAIR))

	window.addstr(title_line+6, left_margin, controls, title_attribute)
	window.addstr(title_line+6, left_margin+wasd_offset, "WASD",
	  	c.color_pair(CYAN_PAIR))
	window.addstr(title_line+6, left_margin+arrow_keys_offest,
		"arrow keys", c.color_pair(CYAN_PAIR))
	
	window.addstr(title_line+7, left_margin, begin, title_attribute)
	window.addstr(title_line+7, left_margin+len(begin), quit,
		title_attribute)
	window.addch(title_line+7, left_margin+len(begin)+q_offset,
		'Q', c.color_pair(ORANGE_PAIR))
	
	window.addstr(title_line+9, left_margin, sendoff,
		c.color_pair(YELLOW_PAIR))

	window.refresh()

def win_cutscene(window) -> None:
	# Animation goal
	# *#	  M
	# *  #  M
	# *   #M
	robot_start: int = len(CAT[1]) + 2
	kitty_start: int = robot_start + 7
	cutscene_start = time.time()
	wait_time: float = 1.25
	time.sleep(wait_time - ((time.time()-cutscene_start) % wait_time))

	window.clear()
	window.addstr(0, 0, CAT[1], c.color_pair(CAT_COLOR_PAIR))
	window.addch(0, robot_start, PLAYER_CHAR,
		c.color_pair(PLAYER_COLOR_PAIR))
	window.addch(0, kitty_start, CAT[0], c.color_pair(CAT_COLOR_PAIR))
	window.refresh()
	time.sleep(wait_time - ((time.time()-cutscene_start) % wait_time))

	window.clear()
	window.addstr(0, 0, CAT[1], c.color_pair(CAT_COLOR_PAIR))
	window.addch(0, robot_start + 2, PLAYER_CHAR,
		c.color_pair(PLAYER_COLOR_PAIR))
	window.addch(0, kitty_start - 2, CAT[0],
		c.color_pair(CAT_COLOR_PAIR))
	window.refresh()
	time.sleep(wait_time - ((time.time()-cutscene_start) % wait_time))

	window.clear()
	window.addstr(0, 0, CAT[1], c.color_pair(CAT_COLOR_PAIR))
	window.addch(0, robot_start + 3, PLAYER_CHAR,
		c.color_pair(PLAYER_COLOR_PAIR))
	window.addch(0, kitty_start - 3, CAT[0],
		c.color_pair(CAT_COLOR_PAIR))
	window.refresh()
	time.sleep(wait_time - ((time.time()-cutscene_start) % wait_time))


def main(w):
	start()
	title_screen(w)

	robot = player()
	objs = object_list((MAX_X * MAX_Y) // 200)

	ch: int = 0
	player_won: bool = False

	while (ch != ord('q')) and (not player_won):
		ch = w.getch()

		w.clear()
		check_x, check_y = robot.get_collision_coordinates(ch)

		if objs.check_collisions(check_x, check_y):
			interacted = objs.interact(check_x, check_y, w)
			player_won = True if interacted == CAT[0] else False
			robot.apply_obj_effect(interacted)
		else:
			robot.move(ch)

		robot.draw(w)
		objs.draw_all(w)
		w.refresh()
		
	if player_won:
		cutscene_window = c.newwin(1, MAX_X, 0, 0)
		win_cutscene(cutscene_window)
		w.addstr(1, 0, " Press any key to quit. ",
	   		c.color_pair(PLAYER_COLOR_PAIR))
		w.refresh()
		c.flushinp()
		w.getch()

# Automatically turns off echo
# 	and turns on cbreak, keypad, colors (if supported)
c.wrapper(main)