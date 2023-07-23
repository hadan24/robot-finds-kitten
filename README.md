# Modded Robot Finds Kitten
## Dan Ha
My first homework project for _CS 410 Computer Game Design_ at
Portland State University, taught by Dr. Bart Massey.

## What the project is
A remaking of the classic _Robot Finds Kitten_ (RFK) game
targeting an entirely different player experience.

## Build Instructions
If you have Python 3.11.3 or another compatible version:
* Create an environment
* Run	`pip install -r requirements.txt`
* Run	`py robot-finds-kitten.py`

## Design Questions
1. With my changes to RFK, I want to create a more challenging
	puzzle/strategy game-like experience where finding the kitten
	is hard enough that the	player may not be able to do it every
	round unless they play well. I want to encourage minimalist
	pathing between objects	and finding the kitten as fast as
	possible, turning this into more of a puzzle-/strategy-like
	game in terms of finding that minimal path.

2. My objects (symbols will be marked `thusly`):
	* Battery (`I`) - consume to immediately regain a random, small percentage of battery life

	* Portable Charger (`d`) - consume and the next few steps (random amount) will cost no battery life

	* Wall (`@`) - multi-space, blocks path

	* Wall socket (`:`) - interact for multiple turns to recharge as much as desired

	* Enhanced parts (`*`) - can interact with objects from further away (can stack)

3. Each step or every few steps costs some battery life, and the robot
	must find the kitten before running completely out. This is, in
	effect, a timer but is much easier to implement as the value only
	changes when the player makes a move. Using a battery metaphor
	instead of a normal clock timer also allows for a more fitting,
	"robot-flavored" take on the limited time idea.

4. Because I tested each feature in some common edge cases as I
	implemented them, I am fairly confident the game is bug-free.
	However, extremely extreme edge case bugs that I haven't yet
	thought of may still be possible.

5. Overall, my playtester had a very easy time with finding the kitten
	before their battery ran out. The times they did lose were early
	on in the session where they were unfamiliar with how items worked.
	It was not very tense at all, which could be attributed both to the
	high starting battery total and how abundant the items were. The
	fact that the kitten was highlighted and conspicuous also took away
	from the intensity; I intended for that feature to allow the player
	to focus on finding the best path and collecting the best items
	along the way, but their first instinct was to make a mad dash for
	the kitten, ignoring any items until the end was near.

6. The experience arises from the game and its elements, and I did not
	fully account for how the original RFK's elements added to its
	experience. While the hidden kitten allows and incentivizes one to
	focus more on the searching journey, checking each item along the
	way, it also added a little bit of tension as the player wonders 
	"where is it going to be this time?" and "is it this one? That
	one?" Revealing the kitten takes that away and forces my version
	to rely solely on the battery mechanic to create tension.

7. My "AAA" version would include more potential items to interact
	with and thus more ways to obstruct or help the player. Since I
	have been on a modern roguelike kick with Supergiant's _Hades_,
	It could include multiple randomly generated levels, in which
	objects spawn at different rates to vary the difficulty. Another
	possible route would be to have hand-crafted levels to take this
	more into a puzzle-like direction.

## How it went

The start of the project was very rough with trying to decide on a
language to use and find a corresponding terminal ASCII graphics
library. I could not find one for C# with clear build instructions and
I made good headway with C++ before realizing I had no clue how to
export it with the correct `.dll`s for others to play without using
my machine. I finally settled on Python as the remote playtesters I
had in mind all had Python interpreters.

After that gigantic mess of a hurdle, creating the game was not very
difficult since the logic is very simple. The more difficult part was
deciding how and where to draw the boundaries between my objects and
how to keep them separate and encapsulated while still allowing
interaction for my desired special effects. While I found a solution
that works, I am unsure of whether this would scale. Playtesting was
surprisingly easy and painless, likely also because the game is so
simple. Some failures with my design (in terms of the desired player
experience) were also obvious from the start.


## What must still be done

* From here, I would like to fix the existing issues I found while
	play-testing which include: making the directions more prominent, 
	including movement controls on the help screen, lowering the
	starting battery value, and adding a restart button for easy
	replayability. After that, I would do more play-testing until this
	core was strong, then build on it to eventually reach that "AAA"
	version mentioned in question 7.