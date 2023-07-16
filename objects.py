from defs import c, randrange, CAT, CAT_COLOR, MAX_X, \
	MAX_Y, OBJ_COLORS, NUM_OBJ_COLORS, OBJS, NUM_OBJS

class object_list:
	class object:
		def __init__(self, is_cat = False) -> None:
			self.__symbol, self.__message = \
				CAT if is_cat else OBJS[randrange(NUM_OBJS)]
			self.__color_pair =	CAT_COLOR if is_cat \
				else OBJ_COLORS[randrange(NUM_OBJ_COLORS)]
			self.__x = randrange(MAX_X)
			self.__y = randrange(MAX_Y)

	def __init__(self, to_spawn = 0) -> None:
		self.__list = [object(True)]
		self.__size = to_spawn + 1
		for _ in range(1, self.__size):
			self.__list.append(object)

