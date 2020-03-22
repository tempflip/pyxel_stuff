from engine import *
import pyxel

def read_obj(fname, px=0, py=0, pz=0, mlt=1):
	points = []
	faces = []
	with open(fname) as lines:
		for line in lines:
			line = line.replace('  ', ' ')
			els = line.split(' ')
			if (els[0] == 'v'):
				x = float(els[1]) * mlt + px
				y = float(els[2]) * mlt + py
				z = float(els[3]) * mlt + pz
				print(x,y,z)
				points.append(Point(x, y, z))

			if els[0] == 'f':
				vertex_a = int(els[1].split('/')[0]) # the index of the vertex in the points list
				vertex_b = int(els[2].split('/')[0])
				vertex_c = int(els[3].split('/')[0])
				print(els)
				print(vertex_a, vertex_b, vertex_c)
				faces.append(
					Shape([points[vertex_a-1],
							points[vertex_b-1],
							points[vertex_c-1]
					]))


	mod = Model(faces = faces, points = points)
	return mod

class App:
	def __init__(self):

		self.screen_x = 250
		self.screen_y = 250

		self.models = []
		# self.shapes = []
		# self.points = []
		self.models.append(read_obj('cube.obj', px=50, py=50, pz=250, mlt=150))
		print(self.models)
		# p1 = Point(30,30,0)
		# p2 = Point(30,150,0)
		# p3 = Point(150,150,0)
		# p4 = Point(150,30,0)

		# pp1 = Point(30,30,100)
		# pp2 = Point(30,150,100)
		# pp3 = Point(150,150,100)
		# pp4 = Point(150,30,100)

		# ppp1 = Point(30,30,200)
		# ppp2 = Point(30,150,200)
		# ppp3 = Point(150,150,200)
		# ppp4 = Point(150,30,200)

		# pa1 = Point(150, 30, 0)
		# pa2 = Point(150, 30, 200)
		# pa3 = Point(150, 150, 200)
		# pa4 = Point(150, 150, 0)

		# self.points.extend([p1,p2,p3,p4])
		# self.points.extend([pp1,pp2,pp3,pp4])
		# self.points.extend([ppp1,ppp2,ppp3,ppp4])

		# s1 = Shape([p1,p2, p3, p4])
		# s2 = Shape([pp1,pp2, pp3, pp4])
		# s3 = Shape([ppp1,ppp2, ppp3, ppp4])
		# s4 = Shape([pa1,pa2, pa3, pa4])
		# self.shapes.append(s1)
		# self.shapes.append(s2)
		# self.shapes.append(s3)
		# self.shapes.append(s4)

		self.cam = Camera()

		pyxel.init(self.screen_x, self.screen_y, fps=100)
		pyxel.run(self.update, self.draw)

	def update(self):

		if pyxel.btn(pyxel.KEY_UP):
			self.cam.fy+=1
		elif pyxel.btn(pyxel.KEY_DOWN):
			self.cam.fy-=1
		elif pyxel.btn(pyxel.KEY_LEFT):
			self.cam.fx+=1
		elif pyxel.btn(pyxel.KEY_RIGHT):
			self.cam.fx-=1
		elif pyxel.btn(pyxel.KEY_Q):
			self.cam.fl-=1
		elif pyxel.btn(pyxel.KEY_A):
			self.cam.fl+=1
		elif pyxel.btn(pyxel.KEY_S):
			self.cam.angle-=1
		elif pyxel.btn(pyxel.KEY_D):
			self.cam.angle+=1
		elif pyxel.btn(pyxel.KEY_R):
			self.rot_y()
		elif pyxel.btn(pyxel.KEY_T):
			self.rot_z()


	def draw(self):
		pyxel.cls(0)

		# for shape in self.shapes:
			# shape.draw(self.cam, 2)

		for model in self.models:
			for face in model.faces:
				face.draw(self.cam, 2)

		pyxel.text(10, 10, 'fl: ' + str(self.cam.fl), 5)
		pyxel.text(10, 16, 'angle: ' + str(self.cam.angle), 6)
		pyxel.text(10, 22, 'fx, fy: ' + str(self.cam.fx) + ', ' + str(self.cam.fy), 7)
	
	def rot_y(self):
		for model in self.models:		
			for face in model.faces:
				face.rot_y(30, 30, 1)

	def rot_z(self):
		for model in self.models:		
			for face in model.faces:
				face.rot_z(30, 30, 1)

	
App()	
