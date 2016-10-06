##!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from colorama import init
from colorama import Fore, Back, Style

class Bingo:

	def __init__(self):
		self.board = self.create_board()
		self.color = None

	def set_color(self, color):
		if color == "blue":
			self.color = Fore.BLUE
		elif color == "green":
			self.color = Fore.GREEN
		elif color == "yellow":
			self.color = Fore.YELLOW

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
		# If color is not set, use default
		# else use set color
		if self.color == None:
			for i in self.board:
				for j in i:
					if j in drawn:
						print(Fore.RED + "{0:3d}".format(j), end="")
						print (Fore.WHITE, end="")
					else:
						print (Fore.WHITE + "{0:3d}".format(j), end="")
				print ()
		else:
			for i in self.board:
				for j in i:
					if j in drawn:
						print(Fore.RED + "{0:3d}".format(j), end="")
						print (self.color, end="")
					else:
						print (self.color + "{0:3d}".format(j), end="")
				print ()

		print ()


