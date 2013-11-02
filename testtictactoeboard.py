#!/usr/bin/python

import unittest
from tictactoeboard import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_winning_column(self):
        game = TicTacToe('x', [['x','x','o'],['o','x',' '],[' ','x','o']])
        print 'Player x should have a win in column 2'
        self.assertTrue(game.result()) 

    def test_winning_row(self):
        game = TicTacToe('x', [['x','x','x'],['o','o',' '],[' ','o','x']])
        print 'Player x should have a win in row 1'
        self.assertTrue(game.result()) 

    def test_winning_diagonal(self):
        game = TicTacToe('x', [['x','x','o'],['o','x',' '],[' ','o','x']])
        print 'Player x should have a win in the left to right diagonal'
        self.assertTrue(game.result()) 

    def test_losing_column(self):
        game = TicTacToe('o', [['x','x','o'],['o','x',' '],[' ','o','x']])
        print 'player o should lose'
        self.assertFalse(game.result()) 

    def test_losing_row(self):
        game = TicTacToe('o', [['x','x','x'],['o','o',' '],[' ','o','x']])
        print 'player o should lose'
        self.assertFalse(game.result()) 

    def test_losing_diagonal(self):
        game = TicTacToe('o', [['x','x','o'],['o','x',' '],[' ','x','o']])
        print 'player o should lose'
        self.assertFalse(game.result()) 

if __name__ == '__main__':
    unittest.main()
