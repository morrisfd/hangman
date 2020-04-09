#!/usr/bin/env python3

"""Unit tests for screen module"""

import unittest
import unittest.mock as mock

import context
import hangman.cli.screen

class TestScreen(unittest.TestCase):
    """Tests for Screen class"""

    def setUp(self):
        self._screen = hangman.cli.screen.Screen()
        self._gallows = hangman.cli.screen._GALLOWS

    @mock.patch("hangman.cli.screen.os.name", "nt")
    def test_clear_windows(self):
        """Test the clear method works with the NT-based systems"""
        with mock.patch("hangman.cli.screen.os.system") as mock_system:
            self._screen.clear()
            #hangman.cli.screen.Screen.clear()
            mock_system.assert_called_with("cls")

    @mock.patch("hangman.cli.screen.os.name", "posix")
    def test_clear_posix(self):
        """Test the clear method works with the posix-based systems"""
        with mock.patch("hangman.cli.screen.os.system") as mock_system:
            self._screen.clear()
            #hangman.cli.screen.Screen.clear()
            mock_system.assert_called_with("clear")

    def test_gallows_within_bounds(self):
        """Test to see if the gallows method returns the correct image"""
        with mock.patch("hangman.cli.screen.print") as mock_print:
            for index in range(len(self._gallows)):
                self._screen.gallows(index)
                mock_print.assert_called_with(self._gallows[index])

    def test_gallows_outside_bounds(self):
        """Test that gallows method handles out of bounds indices"""
        with mock.patch("hangman.cli.screen.print") as mock_print:
            for index in [-1, len(self._gallows)]:
                self._screen.gallows(index)
                mock_print.assert_called_with(self._gallows[-1])

    def test_get_return(self):
        """Test that get returns response"""
        #with mock.patch("hangman.cli.screen.print") as mock_print:
        with mock.patch("builtins.input", return_value="Yes"):
            self.assertEqual(
                self._screen.get("Is this working? "),
                "Yes"
            )

    def test_put_print(self):
        """Test that get prints"""
        with mock.patch("builtins.print") as mock_print:
            self._screen.put("Hello")
            mock_print.assert_called_with("\nHello")

    def test_goodbye_print(self):
        """Test that get prints"""
        with mock.patch("builtins.print") as mock_print:
            self._screen.goodbye()
            output = ",".join([str(x) for x in mock_print.call_args_list])
        self.assertTrue("Goodbye" in output)

if __name__ == "__main__":
    unittest.main()
