from defs import *
from player import player
from objects import object_list
from text import *
from sys import exit

def main(w):
	start()
	title_screen(w)

	robot = player()
	objs = object_list((MAX_X * MAX_Y) // 200)
		# number of objects should scale w/ window area
	objs.fix_external_overlaps(
		robot.location()[0], robot.location()[1])

	ch: int = 0
	player_quit: bool = False
	game_done: bool = False
	player_won: bool = False	# False -> lose, True -> win

	while not (player_quit or game_done):
		if ch == ord('h'):	help_screen(w)

		w.clear()
		check_x, check_y = robot.get_collision_coordinates(ch)

		if objs.check_collisions(check_x, check_y):
			interacted: chr = objs.interact(check_x, check_y, w)
			game_done = player_won = \
				True if interacted == CAT[0] else False
			consumable = robot.apply_obj_effect(interacted)
			if consumable: objs.destroy(check_x, check_y)
		else:
			robot.move(ch)
			if ch == ord('b'):	robot.toggle_fast_mode()
			game_done = True if robot.battery_dead() else False
			# No need to explicitly change player_won since loss is
			#	assume until kitten is found
		
		robot.draw(w)
		objs.draw_all(w)
		w.refresh()

		if not game_done:
			ch = w.getch()
			player_quit = (ch == ord('q'))

	if player_quit:	exit(0)

	cutscene_window = c.newwin(1, MAX_X+1, 0, 0)
	if player_won:	win_cutscene(cutscene_window)
	else:	lose_cutscene(cutscene_window)
	
	game_quit_message(w)

# Automatically turns off echo
# 	and turns on cbreak, keypad, colors (if supported)
c.wrapper(main)