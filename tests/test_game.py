#!/usr/bin/env python3

"""Unit tests for game module"""

import unittest
import unittest.mock as mock

import context
import hangman.game

_SIMULATED_GAMES = {
    "perfect": {
        "guesses": ["h", "a", "n", "g", "m"],
        "gallows": [0, 0, 0, 0, 0, 0]
    },
    "some misses": {
        "guesses": ["a", "e", "i", "o", "h", "n", "g", "m"],
        "gallows": [0, 1, 2, 3, 3, 3, 3, 3]
    },
    "invalid input": {
        "guesses": ["4", "!", "fishy", "b", "b", "c", "d", "e", "f", "i", "j", "k", "l", "o", "p", "q"],
        "gallows": [0, 0, 0, 0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    }
}

class MockDictionary:
    """Mocked Dictionary class that returns a word"""
    def __init__(self, exclude_words=None):
        pass

    @staticmethod
    def get():
        """Mocked get method that returns the word 'hangman' """
        return "hangman"

@mock.patch.object(hangman.game.Screen, "clear")
@mock.patch.object(hangman.game.Screen, "gallows")
@mock.patch.object(hangman.game.Screen, "put")
@mock.patch.object(hangman.game.Screen, "get")
class TestGame(unittest.TestCase):
    """Tests for Game class"""

    def setUp(self):
        with mock.patch.object(hangman.game, "Dictionary", return_value=MockDictionary()):
            self._game = hangman.game.Game()

    @mock.patch.object(hangman.game.Game, "game")
    @mock.patch.object(hangman.game.Game, "quit")
    def test_start(self, mock_quit, mock_game, *args):
        """Test the start method"""
        self._game.start()
        self.assertTrue(mock_game.called)
        self.assertTrue(mock_quit.called)
        
    def test_game_perfect(self, mock_get, mock_put, mock_gallows, mock_clear):
        """Test the game method with perfect guesses"""
        simulation = _SIMULATED_GAMES["perfect"]
        mock_get.side_effect = simulation["guesses"]
        self._game.game()
        self.assertEqual(mock_clear.call_count, len(simulation["guesses"]) + 1)
        mock_gallows.assert_has_calls([mock.call(x) for x in simulation["gallows"]])

    def test_game_some_misses(self, mock_get, mock_put, mock_gallows, mock_clear):
        """Test the game method with some missed guesses"""
        simulation = _SIMULATED_GAMES["some misses"]
        mock_get.side_effect = simulation["guesses"]
        self._game.game()
        self.assertEqual(mock_clear.call_count, len(simulation["guesses"]) + 1)
        mock_gallows.assert_has_calls([mock.call(x) for x in simulation["gallows"]])

    def test_game_invalid(self, mock_get, mock_put, mock_gallows, mock_clear):
        """Test the game method with invalid guesses"""
        simulation = _SIMULATED_GAMES["invalid input"]
        mock_get.side_effect = simulation["guesses"]
        with mock.patch("hangman.game.time.sleep"):
            self._game.game()
        self.assertEqual(mock_clear.call_count, len(simulation["guesses"]) + 1)
        mock_gallows.assert_has_calls([mock.call(x) for x in simulation["gallows"]])

    def test_quit(self, *args):
        """Test the quit method"""
        with mock.patch.object(hangman.game.Screen, "goodbye") as mock_goodbye:
            self._game.quit()
            mock_goodbye.assert_called_once()

if __name__ == "__main__":
    unittest.main()
