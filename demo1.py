import pyxel
import math

def rot(x_, y_, angle, cx=0, cy=0):

	x = x_ - cx
	y = y_ - cy
	c = math.cos(math.radians(angle))
	s = math.sin(math.radians(angle))
	xn = x * c + y * s 
	yn = -x * s + y * c

	return (xn + cx, yn + cy)

class Point:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

class Shape:
	def __init__(self, points=[]):
		self.points = points

	def draw(self, camera, color):
		prev_point = self.points[-1]
		for p in self.points:

			(x1, y1) = camera.show_point(prev_point)
			(x2, y2) = camera.show_point(p)

			pyxel.line(x1, y1, x2, y2,
				color
				)
			prev_point = p

	def rot_z(self, cx, cy, angle):
		for p in self.points:
			(p.x, p.y) = rot(p.x, p.y, angle, cx = cx, cy = cy)

	def rot_y(self, cx, cz, angle):
		for p in self.points:
			(p.x, p.z) = rot(p.x, p.z, angle, cx = cx, cy = cz)


class Camera:
	# fl -- focal length
	def __init__(self, fl = 100, angle = 45, fx = 100, fy = 100): 
		self.fl = fl
		self.angle = angle
		self.fy = fy
		self.fx = fx

	def show_point(self, p):

		yc1 = math.radians(self.angle) * self.fl
		yc2 = math.radians(self.angle) * self.fl + p.z
		z_prop = yc1 / yc2


		x = self.fx - (self.fx-p.x) * z_prop
		y = self.fy - (self.fy-p.y) * z_prop


		# print('p.x,p.y', p.x, p.y)
		# print('z_prop', z_prop)
		# print('x,y', x, y)

		return (x, y)



class Demo:
	def __init__(self):

		self.screen_x = 200
		self.screen_y = 200

		self.shapes = []

		p1 = Point(30,30,0)
		p2 = Point(30,150,0)
		p3 = Point(150,150,0)
		p4 = Point(150,30,0)

		pp1 = Point(30,30,100)
		pp2 = Point(30,150,100)
		pp3 = Point(150,150,100)
		pp4 = Point(150,30,100)

		ppp1 = Point(30,30,200)
		ppp2 = Point(30,150,200)
		ppp3 = Point(150,150,200)
		ppp4 = Point(150,30,200)

		pa1 = Point(150, 30, 0)
		pa2 = Point(150, 30, 200)
		pa3 = Point(150, 150, 200)
		pa4 = Point(150, 150, 0)

		s1 = Shape([p1,p2, p3, p4])
		s2 = Shape([pp1,pp2, pp3, pp4])
		s3 = Shape([ppp1,ppp2, ppp3, ppp4])
		s4 = Shape([pa1,pa2, pa3, pa4])
		self.shapes.append(s1)
		self.shapes.append(s2)
		self.shapes.append(s3)
		self.shapes.append(s4)

		self.cam = Camera()

		pyxel.init(self.screen_x, self.screen_y, fps=100)
		pyxel.run(self.update, self.draw)

	def update(self):
		self.rot_all()

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
		# elif pyxel.btn(pyxel.KEY_R):
			# self.rot_all()

	def draw(self):
		pyxel.cls(0)

		for shape in self.shapes:
			shape.draw(self.cam, 2)

		pyxel.text(10, 10, 'fl: ' + str(self.cam.fl), 5)
		pyxel.text(10, 16, 'angle: ' + str(self.cam.angle), 6)
		pyxel.text(10, 22, 'fx, fy: ' + str(self.cam.fx) + ', ' + str(self.cam.fy), 7)

	def rot_all(self):
		for shape in self.shapes:
			shape.rot_z(100, 100, 2)
			shape.rot_y(100, 100, 1)
	
Demo()	

print(rot(5, 15, 0, 5, 5))
print(rot(5, 15, 45, 5, 5))
print(rot(5, 15, 90, 5, 5))
print(rot(5, 15, 135, 5, 5))
print(rot(5, 15, 180, 5, 5))

