from defs import c, randrange, CAT, CAT_COLOR, MAX_X, \
	MAX_Y, OBJ_COLOR_PAIRS, NUM_OBJ_COLORS, OBJS, NUM_OBJS

class object_list:
	class __obj:
		def __init__(self, is_cat: bool = False) -> None:
			self.symbol, self.message = CAT if is_cat \
				else OBJS[randrange(NUM_OBJS)]
			self.color_pair: int = CAT_COLOR if is_cat \
				else OBJ_COLOR_PAIRS[randrange(NUM_OBJ_COLORS)]
			self.x: int = randrange(MAX_X)
			self.y: int = randrange(MAX_Y)

	def __init__(self, to_spawn: int = 0) -> None:
		self.__list: list = [self.__obj(True)]
		self.__size: int = to_spawn + 1
		for i in range(1, self.__size):
			self.__list.append(self.__obj())

			for j in range(0, i):
				self.__fix_overlaps(i, j)

	def draw_all(self, window) -> None:
		for obj in self.__list:
			window.addch(obj.y, obj.x, obj.symbol, \
				c.color_pair(obj.color_pair))

	def __fix_overlaps(self, i1, i2) -> None:
		curr: self.__obj = self.__list[i1]
		to_cmp: self.__obj = self.__list[i2]

		if (curr.x == to_cmp.x) and (curr.y == to_cmp.y):
			if (curr.x + 1) >= MAX_X:
				curr.x -= i2
			else:
				curr.x += i2