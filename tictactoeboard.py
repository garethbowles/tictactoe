#!/usr/bin/env python

import logging

__version__ = '0.0.1'

logging.basicConfig(level=logging.INFO)

class TicTacToe(object):
    """
    Calculate the results of a TicTacToe game given a
    player ID and a 2-dimensional array containing the
    cells that the player occupies.
    Currently supports a 3x3 board and needs error
    checking to be added.
    """

    def __init__(self, player, board):
        self.player = player
        self.board = board

    def result(self):
        won = False
        cells = 0
        board = self.board
        player = self.player
        # Brute force algorithm - check rows, then columns, then diagonals
        # Check rows
        for row in range(0, 3):
            logging.debug('Checking row %d' % row)
            for col in range(0, 3):
                if board[row][col] == player:
                    cells += 1
                    logging.debug('Player filled out %d,%d, cells=%d' % (row, col, cells))

            if cells == 3:
                won = True
                break
            cells = 0

        # Check columns
        for col in range(0, 3):
            logging.debug('Checking column %d' % col)
            for row in range(0, 3):
                if board[row][col] == player:
                    cells += 1
                    logging.debug('Player filled out %d,%d, cells=%d' % (row, col, cells))

            if cells == 3:
                won = True
                break
            cells = 0

        # Check diagonals
        if board[0][0] == player and board[1][1] == player and board[2][2] == player or board[0][2] == player and board[1][1] == player and board[2][0] == player:
            won = True
        for row in range(0, 3):
            for col in range(0, 3):
                print '%s ' % board[row][col],

            print ''

        if won == True:
            print 'Player %s won !!!' % player
        else:
            print 'Player %s lost :-(' % player
        return won
