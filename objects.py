from defs import c, randrange, CAT, CAT_COLOR_PAIR,	MIN_X, MIN_Y, \
	MAX_X, MAX_Y, OBJ_COLOR_PAIRS, NUM_OBJ_COLOR_PAIRS, OBJS, NUM_OBJS

class object_list:
	def __init__(self, to_spawn: int = 0) -> None:
		self.__list = [self.__obj(True)]	# 1st obj is always cat
		self.__size = to_spawn + 1

		for i in range(1, self.__size):
			self.__list.append(self.__obj())
			for j in range(0, i):
				self.__fix_list_overlaps(i, j)

	def draw_all(self, window) -> None:
		for obj in self.__list:
			window.addch(obj.y, obj.x, obj.symbol, \
				c.color_pair(obj.color_pair))
			
	# Takes the coordinates that the collider (not collidee)
	#	has/would run into, checks if collision has happened
	def check_collisions(self, x: int, y: int) -> bool:
		for obj in self.__list:
			if obj.x == x and obj.y == y:
				return True
		return False
	
	# Detects if an object has been interacted with and displays
	#	its flavor text, returns its symbol for special effects
	def interact(self, x: int, y: int, w) -> chr:
		for obj in self.__list:
			if obj.x == x and obj.y == y:
				w.addstr(0, 0, obj.msg, c.color_pair(obj.color_pair))
				return obj.symbol
		return '\0'

	# Ensures the player does not overlap with any objects, (may be
	#	turned into global function to work with any two objects)
	def fix_external_overlaps(self, ext_x: int, ext_y: int) -> None:
		i = 0
		while i < self.__size:
			obj = self.__list[i]
			if (obj.x == ext_x) and (obj.y == ext_y):
				obj.x += (i+1) if (obj.x-1) <= MIN_X else -(i+1)
			else:	i += 1

	def destroy(self, x: int, y: int) -> None:
		for i in range(len(self.__list)):
			obj = self.__list[i]
			if obj.x == x and obj.y == y:
				self.__list.pop(i)
				return


	class __obj:
		def __init__(self, is_cat: bool = False) -> None:
			self.symbol, self.msg = CAT if is_cat \
				else OBJS[randrange(NUM_OBJS)]
			self.color_pair: int = CAT_COLOR_PAIR if is_cat \
				else OBJ_COLOR_PAIRS[randrange(NUM_OBJ_COLOR_PAIRS)]
			self.x: int = randrange(MIN_X, MAX_X)
			self.y: int = randrange(MIN_Y, MAX_Y)

	def __fix_list_overlaps(self, i1, i2) -> None:
		curr: self.__obj = self.__list[i1]
		to_cmp: self.__obj = self.__list[i2]

		if (curr.x == to_cmp.x) and (curr.y == to_cmp.y):
			curr.x += (-i2) if (curr.x+1) >= MAX_X else i2