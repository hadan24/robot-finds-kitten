from defs import c, randrange, PLAYER_COLOR, MAX_X, MAX_Y

class player:
	def __init__(self) -> None:
		self.__symbol: chr = '#'
		self.__x: int = randrange(MAX_X)
		self.__y: int = randrange(MAX_Y)
		self.__color_pair: int = PLAYER_COLOR
		self.__step_size: int = 1

	def move(self, key_pressed: int):
		if (key_pressed == c.KEY_UP) or (key_pressed == ord('w')):
			self.__y -= self.__step_size
		elif (key_pressed == c.KEY_LEFT) or (key_pressed == ord('a')):
			self.__x -= self.__step_size
		elif (key_pressed == c.KEY_DOWN) or (key_pressed == ord('s')):
			self.__y += self.__step_size
		elif (key_pressed == c.KEY_RIGHT) or (key_pressed == ord('d')):
			self.__x += self.__step_size

	def draw(self, window):
		window.addch(self.__y, self.__x, \
	       self.__symbol, c.color_pair(self.__color_pair))
		
	