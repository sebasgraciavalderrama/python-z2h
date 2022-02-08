import unittest
import TicTacToe

class TestTicTacToe(unittest.TestCase):
    TICTACTOEBOARD = [['1','2','3'],
                     ['4','5','6'],
                     ['7','8','9']]

    TICTACTOEBOARD_X = [['1','2','X'],
                      ['4','X','6'],
                      ['7','8','X']]

    TICTACTOEBOARD_X_WIN = [['X','2','3'],
                            ['4','X','6'],
                            ['7','8','X']]

    TICTACTOEBOARD_O = [['O','2','3'],
                        ['4','5','O'],
                        ['O','8','9']]

    TICTACTOEBOARD_O_WIN = [['1','O','3'],
                            ['4','O','6'],
                            ['7','O','9']]

    def test_get_index_of_player_choice(self):
        player_choice = '2'
        result = TicTacToe.get_index_of_player_choice(self.TICTACTOEBOARD, player_choice)
        self.assertEqual(result, (0,1))

        player_choice = '8'
        result = TicTacToe.get_index_of_player_choice(self.TICTACTOEBOARD, player_choice)
        self.assertEqual(result, (2,1))

        player_choice = '6'
        result = TicTacToe.get_index_of_player_choice(self.TICTACTOEBOARD, player_choice)
        self.assertEqual(result, (1,2))

    def test_get_index_player_of_choice_with_X(self):
        player_choice = '3'
        result = TicTacToe.get_index_of_player_choice(self.TICTACTOEBOARD_X, player_choice)
        self.assertEqual(result, (-1,-1))

        player_choice = '5'
        result = TicTacToe.get_index_of_player_choice(self.TICTACTOEBOARD_X, player_choice)
        self.assertEqual(result, (-1,-1))

        player_choice = '9'
        result = TicTacToe.get_index_of_player_choice(self.TICTACTOEBOARD_X, player_choice)
        self.assertEqual(result, (-1,-1))

    def test_get_index_player_of_choice_with_O(self):
        player_choice = '1'
        result = TicTacToe.get_index_of_player_choice(self.TICTACTOEBOARD_O, player_choice)
        self.assertEqual(result, (-1,-1))

        player_choice = '6'
        result = TicTacToe.get_index_of_player_choice(self.TICTACTOEBOARD_O, player_choice)
        self.assertEqual(result, (-1,-1))

        player_choice = '7'
        result = TicTacToe.get_index_of_player_choice(self.TICTACTOEBOARD_O, player_choice)
        self.assertEqual(result, (-1,-1))

    def test_insert_player_choice_X_successful(self):
        player = 'X'

        player_choice = '1'
        result = TicTacToe.insert_player_choice(self.TICTACTOEBOARD, player_choice, player)
        self.assertEqual(result, True)

        player_choice = '3'
        result = TicTacToe.insert_player_choice(self.TICTACTOEBOARD, player_choice, player)
        self.assertEqual(result, True)

        player_choice = '7'
        result = TicTacToe.insert_player_choice(self.TICTACTOEBOARD, player_choice, player)
        self.assertEqual(result, True)

    def test_insert_player_choice_O_successful(self):
        player = 'O'

        player_choice = '4'
        result = TicTacToe.insert_player_choice(self.TICTACTOEBOARD, player_choice, player)
        self.assertEqual(result, True)

        player_choice = '5'
        result = TicTacToe.insert_player_choice(self.TICTACTOEBOARD, player_choice, player)
        self.assertEqual(result, True)

        player_choice = '9'
        result = TicTacToe.insert_player_choice(self.TICTACTOEBOARD, player_choice, player)
        self.assertEqual(result, True)

    def test_insert_player_choice_X_unsuccessful(self):
        player = 'X'
        player_choice = '3'

        result = TicTacToe.insert_player_choice(self.TICTACTOEBOARD_X, player_choice, player)
        self.assertEqual(result, False)

        player_choice = '5'
        result = TicTacToe.insert_player_choice(self.TICTACTOEBOARD_X, player_choice, player)
        self.assertEqual(result, False)

        player_choice = '9'
        result = TicTacToe.insert_player_choice(self.TICTACTOEBOARD_X, player_choice, player)
        self.assertEqual(result, False)

    def test_insert_player_choice_O_unsuccessful(self):
        player = 'O'
        player_choice = '1'

        result = TicTacToe.insert_player_choice(self.TICTACTOEBOARD_O, player_choice, player)
        self.assertEqual(result, False)

        player_choice = '6'
        result = TicTacToe.insert_player_choice(self.TICTACTOEBOARD_O, player_choice, player)
        self.assertEqual(result, False)

        player_choice = '7'
        result = TicTacToe.insert_player_choice(self.TICTACTOEBOARD_O, player_choice, player)
        self.assertEqual(result, False)

    def test_win_X(self):
        player = 'X'

        result = TicTacToe.win(self.TICTACTOEBOARD_X_WIN, player)
        self.assertEqual(result, True)

        result = TicTacToe.win(self.TICTACTOEBOARD_X, player)
        self.assertEqual(result, False)

    def test_win_O(self):
        player = 'O'

        result = TicTacToe.win(self.TICTACTOEBOARD_O_WIN, player)
        self.assertEqual(result, True)

        result = TicTacToe.win(self.TICTACTOEBOARD_O, player)
        self.assertEqual(result, False)

    def test_tie(self):
        number_of_plays = 9
        result = TicTacToe.tie(number_of_plays)
        self.assertEqual(result, True)

        number_of_plays = 7
        result = TicTacToe.tie(number_of_plays)
        self.assertEqual(result, False)

        number_of_plays = 3
        result = TicTacToe.tie(number_of_plays)
        self.assertEqual(result, False)

        number_of_plays = -1
        result = TicTacToe.tie(number_of_plays)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
