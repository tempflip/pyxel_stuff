import pyxel
import random

pyxel.init(100, 100, fps=100)

def update():
	pass

def draw():
	for i in range(100):
		# pyxel.pix(random.randint(0, 99), random.randint(0, 99), random.randint(0, 15))
		pyxel.rect(random.randint(0, 99), random.randint(0, 99), 10, 10, random.randint(0, 15))

pyxel.run(update, draw)


