##!/usr/bin/env python
# -*- coding: utf-8 -*-
from player import Player
import random
from time import sleep

class Game:

	def __init__(self):
		self.game_nums = self.randomizer() # return randomized list 0-99
		self.players = []
		colors = ["blue", "green", "yellow"]
		for i in range(2):
			if (i < 1):
				pl = Player("Player 1")
			else:
				pl = Player("Player " + str(i + 1), colors[i-1])
				pl.bingo.set_color(colors[i-1])
			self.players.append(pl)

		#self.p1 = Player("Player 1")

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
		for pl in self.players:
			pl.draw(drawn)
			if pl.win_chances(drawn) == 1:
				pl.win_print()
				return 0
		#self.p1.draw(drawn)
		#if self.p1.win_chances(drawn) == 1:
		#	self.p1.win_print()
		#	return 0

		return 1

	def run_loop(self):
		drawn = []
		#self.p1.draw()
		for pl in self.players:
			pl.draw()
		for i in range(len(self.game_nums)):
			sleep(0.1)
			if self.timer_zone(drawn, i) == 0:
				break

	def run(self):
		self.run_loop()



