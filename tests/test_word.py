#!/usr/bin/env python3
"""Unit test for Word module"""
import unittest
import unittest.mock as mock

import context
import hangman.word

class TestWord(unittest.TestCase):
    """Tests for Word class"""

    def setUp(self):
        self._word = hangman.word.Word("hangman")

    def test_guess_single_letter_error(self):
        """test guess already guessed error"""
        with self.assertRaises(hangman.error.GuessError):
            self._word.guess("hangman")

    def test_guess_already_guessed_error(self):
        """test guess already guessed error"""
        self._word.guess("a")
        with self.assertRaises(hangman.error.GuessError):
            self._word.guess("a")
        self._word.guess("B")
        with self.assertRaises(hangman.error.GuessError):
            self._word.guess("B")

    def test_guess_funky_characters_guessed_error(self):
        """test guess already guessed error"""
        with self.assertRaises(hangman.error.GuessError):
            self._word.guess("!")

    def test_incorrects(self):
        """test masked"""
        for _x in list("aeiouybcdfhngm"):
            self._word.guess(_x)
        self.assertEqual(
            ''.join(self._word.incorrects),
            "EIOUYBCDF"
        )

    def test_masked(self):
        """test masked"""
        for _x in list("eiouybcdfhngm"):
            self._word.guess(_x)
        self.assertEqual(
            self._word.masked,
            "H _ N G M _ N"
        )

    def test_unmasked(self):
        """test that unmasked returns the word"""
        self.assertEqual(
            self._word.unmasked,
            "HANGMAN"
        )

    def test_alive_true(self):
        """test that alive returns True"""
        self.assertTrue(
            self._word.alive
        )

    def test_alive_false(self):
        """test that alive returns False"""
        for _x in list("bcdefijklopq"):
            self._word.guess(_x)
        self.assertFalse(
            self._word.alive
        )

    def test_solved(self):
        """test that solved returns False"""
        self.assertFalse(
            self._word.solved
        )

    def test_solved_true(self):
        """test that solved returns True"""
        for _x in list("hangm"):
            self._word.guess(_x)
        self.assertTrue(
            self._word.solved
        )

if __name__ == "__main__":
    unittest.main()
