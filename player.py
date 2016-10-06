##!/usr/bin/env python
# -*- coding: utf-8 -*-
from bingo import Bingo
from colorama import Style

class Player:

	def __init__(self, name, color=None):
		self.bingo = Bingo()
		self.name = name
		self.color = color

	def draw(self, drawn=[]):
		self.bingo.draw_board(drawn)

	def win_print(self):
		if self.bingo.color == None:
			print ("Player {0:s} wins".format(self.name))
		else:
			print (self.bingo.color + "Player {0:s} wins".format(self.name))
			#print (Style.RESET_ALL, end="")

	def win_chances(self, drawn):
		if len(drawn) < 10:
			return 0

		if self.rows(drawn) == 1 or self.columns(drawn) == 1:
			return 1

		return 0

	def rows(self, drawn=[]):
		board = self.bingo.board
		for i in board:
			row = []
			for j in i:
				row.append(j)

			# for clarity, if row is subset of drawn
			if set(row) <= set(drawn):
				return 1

		return 0

	def columns(self, drawn):
		board = self.bingo.board
		# number of items in inner list equals number of inner lists
		# so len(board) is always working
		for i in range(len(board)):
			column = []
			for j in range(len(board)):
				column.append(board[j][i])

			if set(column) <= set(drawn):
				return 1

		return 0
