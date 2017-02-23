from rpg_hero import Hero
from rpg_monsters import Goblin
from images import homer
from images import llama
from images import look_up

hero = Hero()
enemies = [Goblin()]

for enemy in enemies:
	# loop thru all the bad guys in the enemies list
	# print vars(enemy)
	while hero.alive() and enemy.alive():
		# print off content
		print look_up
		print "Enter your name to get started"
		name = raw_input()
		print "Welcome %s, you have %d health and %d power." % (name, hero.health, hero.power)
		print "The enemy has %d health and %d power." % (enemy.health, enemy.power)
		print "What will you do fool?"
		print "1. Fight %s" % enemy.name
		print "2. Run Away"
		print "> ",
		# get input from user
		input = int(raw_input())
		if input == 1:
			# user has chosen to fight
			hero.attack(enemy)
		elif input == 2:
			# user has run away, break out of while loop
			break
		else:
			# user has malfunctioned, complain
			print "Invalid choice %r" % input
		if enemy.alive():
			# user has made their choice and now its the enemys turn
			# IF the enemy has health. subtract his power from his health
			enemy.attack(hero)
	if hero.alive() and enemy.alive() == False:
		# we know they won, because someone's health is less than 0
		print "You won! the %s has been defeated!!" % enemy.name
	else:
		# we knowe the hero lost
		print "You were defeated by %s!!" % enemy.name