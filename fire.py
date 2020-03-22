import pyxel

class Demo:
	def __init__(self):
		self.first = True

		pyxel.init(100, 100, fps=10)
		pyxel.run(self.update, self.draw)

	def update(self):
		for y in range(100):
			for x in range(100):
				cc = pyxel.pget(x,y+1) 
				+ pyxel.pget(x,y+2)
				+ pyxel.pget(x+1,y+2)
				# print(cc) 
				pyxel.pset(x, y, int(cc/1.1))
		pass

	def draw(self):
		print('frame')
		if self.first:
			pyxel.text(50,50, 'yaaaay', 12)
			pyxel.text(30,75, 'hali hali ', 13)
			self.first = False




		pass

Demo()
