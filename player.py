from defs import c, randrange, PLAYER_COLOR_PAIR, \
	MIN_X, MIN_Y, MAX_X, MAX_Y

class player:
	def __init__(self) -> None:
		self.__symbol: chr = '#'
		self.__x: int = randrange(MIN_X, MAX_X)
		self.__y: int = randrange(MIN_Y, MAX_Y)
		self.__color_pair: int = PLAYER_COLOR_PAIR
		
		self.__step_size: int = 1

		self.__battery_capacity: int = 50
		self.__battery_lvl: int = self.__battery_capacity
		self.__fast_mode: bool = False

	# Returns coordinates for what's in front of player
	#	for interaction/collision purposes
	#	*** ideally should be called BEFORE moving player ***
	def get_collision_coordinates(self, key_pressed: int) -> \
		tuple[int, int]:

		dir: str = self.__direction_from_key(key_pressed)
		if dir == "up":
			return (self.__x, self.__y-self.__step_size)
		if dir == "left":
			return (self.__x-self.__step_size, self.__y)
		if dir == "down":
			return (self.__x, self.__y+self.__step_size)
		if dir == "right":
			return (self.__x+self.__step_size, self.__y)
		else:
			return 0, 0

	def move(self, key_pressed: int) -> None:
		dir: str = self.__direction_from_key(key_pressed)

		if dir == "up":			self.__y -= self.__step_size
		elif dir == "left":		self.__x -= self.__step_size
		elif dir == "down":		self.__y += self.__step_size
		elif dir == "right":	self.__x += self.__step_size

		if dir != "invalid":	self.__battery_lvl -= randrange(2)
		self.__screen_wrap()

	def draw(self, window) -> None:
		window.addch(self.__y, self.__x, \
	       self.__symbol, c.color_pair(self.__color_pair))
		
		battery_UI = f" current battery % = " + \
			f"{self.__battery_lvl}/{self.__battery_capacity} "
		window.addstr(0, MAX_X-len(battery_UI)+1, battery_UI, \
			c.color_pair(self.__color_pair))
		
	def apply_obj_effect(self, obj: chr) -> bool:
		if obj == 'I':
			self.__battery_lvl += 3
			self.__battery_capacity += 3
			return True
		if obj == 'd':
			self.__battery_lvl = \
				min(self.__battery_lvl+5, self.__battery_capacity)
			return True
		if obj == '@':
			return False
		if obj == ':':
			self.__battery_lvl = \
				min(self.__battery_lvl+2, self.__battery_capacity)
			return False
		if obj == '*':
			self.__step_size += 1
			self.__fast_mode = True
			return True

	def battery_dead(self) -> bool:
		return self.__battery_lvl <= 0
	
	def location(self) -> tuple[int, int]:
		return self.__x, self.__y
	

	# *** Little helper section :) ***
	def __screen_wrap(self) -> None:
		if self.__y >= MAX_Y:		self.__y = MIN_Y
		elif self.__y < MIN_Y:		self.__y = MAX_Y - 1

		if self.__x >= MAX_X:		self.__x = MIN_X
		elif self.__x < MIN_X:		self.__x = MAX_X - 1

	def __direction_from_key(self, key_pressed: int) -> str:
		if (key_pressed == c.KEY_UP) or (key_pressed == ord('w')):
			return "up"
		if (key_pressed == c.KEY_LEFT) or (key_pressed == ord('a')):
			return "left"
		if (key_pressed == c.KEY_DOWN) or (key_pressed == ord('s')):
			return "down"
		if (key_pressed == c.KEY_RIGHT) or (key_pressed == ord('d')):
			return "right"
		
		return "invalid"