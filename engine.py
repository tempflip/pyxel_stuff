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

	def draw(self, camera, color):
		(x, y) = camera.show_point(self)
		pyxel.pset(x, y, color)

class Shape:
	def __init__(self, points=[]):
		self.points = points

	def draw(self, camera, color):
		prev_point = self.points[-1]
		for p in self.points:

			(x1, y1) = camera.show_point(prev_point)
			(x2, y2) = camera.show_point(p)

			pyxel.line(x1, y1, x2, y2, color)
			prev_point = p

class Model:
	def __init__(self, faces = [], points = []):
		self.faces = faces
		self.points = points

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

		return (x, y)
