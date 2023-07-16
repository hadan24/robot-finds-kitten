from defs import *

def main(w):
	w.addstr(5, 10, "h-hello?")
	w.refresh()
	w.getch()

c.wrapper(main)