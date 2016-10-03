##!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from colorama import init
from colorama import Fore, Back, Style

class Bingo:

	def __init__(self):
		self.board = self.create_board()

	def create_board(self):
		board = []
		random_list = list(range(100))
		random.shuffle(random_list)
		count = 0
		for i in range(10):
			row = []
			for j in range(10):
				row.append(random_list[count])
				count += 1
			board.append(row)

		return board

	def draw_board(self, drawn=[]):
		if (not self.board):
			print ("No board created")
			return
		#init() #Don't know why this ain't working?

		for i in self.board:
			for j in i:
				if j in drawn:
					# first print outputs red number amongst default white and second print just reset color to default
					# it works though I don't know why
					print(Fore.RED + "{0:3d}".format(j), end="")
					print (Style.RESET_ALL, end="")
				else:
					print ("{0:3d}".format(j), end="")
			print ()


