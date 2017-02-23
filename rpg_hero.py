import time
from rpg import name

# give the class a name...  Hero
class Hero(object):
	# call the init method which is built into classes
	# pass it self so that we have a "this to work with"
	def __init__(self):
		# define some class properties (attached to self)
		self.name = name
		self.health = 10
		self.power = 5

	def alive(self):
		return self.health > 0

	def attack(self, enemy):
		print "%s attacks %s" % (self.name, enemy.name)
		enemy.take_damage(self.power)
		time.sleep(1.5)
		print "%s has done %d damage to %s" % (self.name, self.power, enemy.name)

	def take_damage(self, points_of_damage):
		self.health -= points_of_damage