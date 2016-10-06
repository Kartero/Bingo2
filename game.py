##!/usr/bin/env python
# -*- coding: utf-8 -*-
from player import Player
import random
from threading import Timer

class Game:

	def __init__(self):
		self.game_nums = self.randomizer() # return randomized list 0-99
		self.p1 = Player("Tero")

	def randomizer(self):
		game_nums = list(range(100))
		random.shuffle(game_nums)
		return game_nums

	def number_print(self, i):
		print("\nNext number is...")
		print(self.game_nums[i])
		print("\n")

	def timer_zone(self, drawn, i):
		self.number_print(i)
		drawn.append(self.game_nums[i])
		self.p1.draw(drawn)
		if self.p1.win_chances(drawn) == 1:
			self.p1.win_print()
			return 0

		return 1

	def run_loop(self):
		drawn = []
		self.p1.draw()
		for i in range(len(self.game_nums)):
			if self.timer_zone(drawn, i) == 0:
				break

	def run(self):
		self.run_loop()



