from defs import *

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

	welcome: str = "Welcome to Robot Finds Kitten - Dan Edition! "

	player_char: str = "In this game, you play as robot: "
	goal: str = "And you must get to kitten: "

	battery: str = "But, you must do so before your battery runs out. "
	battery_UI: str = "(You can check it in the top right corner.) "

	controls: str = "Use WASD or the arrow keys to move. "
	wasd_offset: int = 4
	arrow_keys_offest: int = 16
	begin: str = "Press almost any key to start playing. "
	quit: str = "Press Q at any time to quit. "
	help: str = "Press H at any time for item information. "
	button_offset: int = 6

	sendoff: str = "Good luck, friend. "

	window.addstr(title_line, left_margin, welcome,
		title_attribute | c.A_UNDERLINE)

	window.addstr(title_line+2, left_margin, player_char, title_attribute)
	window.addch(title_line+2, left_margin+len(player_char),
	 	PLAYER_CHAR, c.color_pair(PLAYER_COLOR_PAIR))

	window.addstr(title_line+3, left_margin, goal, title_attribute)
	window.addch(title_line+3, left_margin+len(goal), CAT[0],
		c.color_pair(CAT_COLOR_PAIR))

	window.addstr(title_line+4, left_margin, battery, title_attribute)
	window.addstr(title_line+4, left_margin+len(battery), battery_UI,
		c.color_pair(BLUE_PAIR))

	window.addstr(title_line+6, left_margin, controls, title_attribute)
	window.addstr(title_line+6, left_margin+wasd_offset, "WASD",
	  	c.color_pair(CYAN_PAIR))
	window.addstr(title_line+6, left_margin+arrow_keys_offest,
		"arrow keys", c.color_pair(CYAN_PAIR))
	
	window.addstr(title_line+7, left_margin, begin, title_attribute)
	window.addstr(title_line+8, left_margin, quit, title_attribute)
	window.addch(title_line+8, left_margin+button_offset, 'Q',
		c.color_pair(RED_PAIR))
	window.addstr(title_line+8, left_margin+len(quit), help,
	    title_attribute)
	window.addch(title_line+8, left_margin+len(quit)+button_offset,
		'H', c.color_pair(GREEN_PAIR))
	
	window.addstr(title_line+10, left_margin, sendoff,
		c.color_pair(LAVENDER_PAIR))

	window.refresh()

def help_screen(window) -> None:
	window.clear()
	text_attribute = c.color_pair(0) | c.A_BOLD
	symbol_attribute = c.color_pair(YELLOW_PAIR)
	start_line: int = 2
	left_margin: int = 5

	battery: str = "(I) Battery: consume to recharge your battery " + \
		"a bit and increase its capacity by that same amount."
	charger: str = "(d) Portable Charger: consume to recharge " + \
		"your battery a sizeable amount."
	wall: str = "(@) Wall: just a wall, it just sits there. "
	socket: str = "(:) Socket: continually interact to recharge " + \
		"your batter a bit."
	parts1: str = "(*) Spare parts: consume to attach them to " + \
		"yourself for faster movement. "
	parts2: str = "(Faster movement can be toggled on or off " + \
		"by pressing B.) "
	b_offset: int = len(parts2) - 4
	close: str = "Press any key to return to the game (Q to quit). "
	
	window.addstr(start_line, left_margin, battery, text_attribute)
	window.addch(start_line, left_margin+1, 'I', symbol_attribute)

	window.addstr(start_line+1, left_margin, charger, text_attribute)
	window.addch(start_line+1, left_margin+1, 'd', symbol_attribute)

	window.addstr(start_line+2, left_margin, wall, text_attribute)
	window.addch(start_line+2, left_margin+1, '@', symbol_attribute)

	window.addstr(start_line+3, left_margin, socket, text_attribute)
	window.addch(start_line+3, left_margin+1, ':', symbol_attribute)

	window.addstr(start_line+4, left_margin, parts1, text_attribute)
	window.addch(start_line+4, left_margin+1, '*', symbol_attribute)
	window.addstr(start_line+5, left_margin, parts2, text_attribute)
	window.addch(start_line+5, left_margin+b_offset, 'B',
		c.color_pair(ORANGE_PAIR))
	
	window.addstr(start_line+7, left_margin, close, text_attribute)
	window.addch(start_line+7, left_margin+len(close)-12, 'Q',
		c.color_pair(RED_PAIR))

	window.refresh()
	c.flushinp()
	if window.getch() == ord('q'):	exit(0)

def win_cutscene(window) -> None:
	# Animation goal
	# *#	  M
	# *  #  M
	# *   #M
	robot_start: int = len(CAT[1]) + 2
	kitty_start: int = robot_start + 7
	cutscene_start = t.time()
	wait_time: float = 1.25
	t.sleep(wait_time - ((t.time()-cutscene_start) % wait_time))

	window.clear()
	window.addstr(0, 0, CAT[1], c.color_pair(CAT_COLOR_PAIR))
	window.addch(0, robot_start, PLAYER_CHAR,
		c.color_pair(PLAYER_COLOR_PAIR))
	window.addch(0, kitty_start, CAT[0], c.color_pair(CAT_COLOR_PAIR))
	window.refresh()
	t.sleep(wait_time - ((t.time()-cutscene_start) % wait_time))

	window.clear()
	window.addstr(0, 0, CAT[1], c.color_pair(CAT_COLOR_PAIR))
	window.addch(0, robot_start + 2, PLAYER_CHAR,
		c.color_pair(PLAYER_COLOR_PAIR))
	window.addch(0, kitty_start - 2, CAT[0],
		c.color_pair(CAT_COLOR_PAIR))
	window.refresh()
	t.sleep(wait_time - ((t.time()-cutscene_start) % wait_time))

	window.clear()
	window.addstr(0, 0, CAT[1], c.color_pair(CAT_COLOR_PAIR))
	window.addch(0, robot_start + 3, PLAYER_CHAR,
		c.color_pair(PLAYER_COLOR_PAIR))
	window.addch(0, kitty_start - 3, CAT[0],
		c.color_pair(CAT_COLOR_PAIR))
	window.refresh()
	t.sleep(wait_time - ((t.time()-cutscene_start) % wait_time))

def lose_cutscene(window) -> None:
	# Animation goal
	# *#      M
	# *  H    M
	# *   f   M
	# *    _  M
	lose_msg: str = " Oh no your battery has run out! You lose... "
	robot_start: int = len(lose_msg) + 2
	kitty_start: int = robot_start + 7
	cutscene_start = t.time()
	wait_time: float = 1.25

	window.clear()
	window.addstr(0, 0, lose_msg, c.color_pair(CAT_COLOR_PAIR))
	window.addch(0, robot_start, PLAYER_CHAR,
		c.color_pair(PLAYER_COLOR_PAIR))
	window.addch(0, kitty_start, CAT[0], c.color_pair(CAT_COLOR_PAIR))
	window.refresh()
	t.sleep(wait_time - ((t.time()-cutscene_start) % wait_time))

	window.clear()
	window.addstr(0, 0, lose_msg, c.color_pair(CAT_COLOR_PAIR))
	window.addch(0, robot_start + 2, 'H',
		c.color_pair(PLAYER_COLOR_PAIR))
	window.addch(0, kitty_start, CAT[0], c.color_pair(CAT_COLOR_PAIR))
	window.refresh()
	t.sleep(wait_time - ((t.time()-cutscene_start) % wait_time))

	window.clear()
	window.addstr(0, 0, lose_msg, c.color_pair(CAT_COLOR_PAIR))
	window.addch(0, robot_start + 3, 'f',
		c.color_pair(PLAYER_COLOR_PAIR))
	window.addch(0, kitty_start, CAT[0], c.color_pair(CAT_COLOR_PAIR))
	window.refresh()
	t.sleep(wait_time - ((t.time()-cutscene_start) % wait_time))

	window.clear()
	window.addstr(0, 0, lose_msg, c.color_pair(CAT_COLOR_PAIR))
	window.addch(0, robot_start + 4, '_',
		c.color_pair(PLAYER_COLOR_PAIR))
	window.addch(0, kitty_start, CAT[0], c.color_pair(CAT_COLOR_PAIR))
	window.refresh()
	t.sleep(wait_time - ((t.time()-cutscene_start) % wait_time))

def game_quit_message(window) -> None:
	window.addstr(1, 0, " Press any key to quit. ",
		c.color_pair(PLAYER_COLOR_PAIR))
	window.refresh()
	c.flushinp()
	window.getch()
