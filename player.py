##!/usr/bin/env python
# -*- coding: utf-8 -*-
from bingo import Bingo

class Player:

	def __init__(self, name):
		self.bingo = Bingo()
		self.name = name

	def draw(self, drawn=[]):
		self.bingo.draw_board(drawn)

	def win_print(self):
		print ("Player {0:s} wins".format(self.name))

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
