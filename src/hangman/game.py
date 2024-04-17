"""Module for Game class """

import time

from hangman.dictionary import Dictionary
from hangman.cli.screen import Screen
from hangman.error import GuessError
from hangman.word import Word

class Game:
    """
    The primary object responsible for managing game details and flow.
    """
    def __init__(self):
        self._dictionary = Dictionary()

    def start(self):
        """Starts the game"""
        self.run_game()
        self.quit()

    def run_game(self):
        """Play a single game of hangman"""
        word = Word(self._dictionary.get())
        while True:
            # show the gallows and incorrect guesses
            Screen.clear()
            Screen.gallows(len(word.incorrects))
            # show the masked word, incorrect guesses
            Screen.put(f"\tWord: {word.masked}")
            Screen.put(f"\tIncorrects: {' '.join(word.incorrects)}")
            Screen.put(f"{'=' * 50}")
            if not word.alive or word.solved:
                break
            # ask the player for a guess
            guess = Screen.get("What is your guess?")
            try:
                word.guess(guess)
            except GuessError as err:
                Screen.put(str(err))
                time.sleep(2)
        if word.alive:
            Screen.put(f"\tCongrats, you won!!!")
        else:
            Screen.put(f"\tI'm sorry. The word was {word.unmasked}")

    @staticmethod
    def quit():
        """Quit Play of hangman game"""
        Screen.goodbye()
