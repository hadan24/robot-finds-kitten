from defs import c, randrange, PLAYER_COLOR, MAX_X, MAX_Y

class player:
	def __init__(self) -> None:
		self.__symbol = '#'
		self.__x = randrange(MAX_X)
		self.__y = randrange(MAX_Y)
		self.__color_pair = PLAYER_COLOR
		self.__step_size = 1

