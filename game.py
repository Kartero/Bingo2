##!/usr/bin/env python
# -*- coding: utf-8 -*-
from player import Player
import random

class Game:

	def __init__(self):
		self.game_nums = self.randomizer() # return randomized list 0-99
		self.p1 = Player("Tero")

	def randomizer(self):
		game_nums = list(range(100))
		random.shuffle(game_nums)
		return game_nums

	def run(self):
		drawn = []
		self.p1.draw()

		for i in range(len(self.game_nums)):
			print ("\nNext number is...")
			print (self.game_nums[i])
			print ("\n")
			drawn.append(self.game_nums[i])
			self.p1.draw(drawn)
			if self.p1.win_chances(drawn) == 1:
				self.p1.win_print()
				break



