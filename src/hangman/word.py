"""Word Class"""

import re
from  hangman.error import GuessError

class Word:
    """Word module"""
    def __init__(self, raw_word):
        """__init__"""
        self._word = raw_word.upper()
        # Guesses
        self._guesses = []
        #Valid input pattern
        self._valid_input_pattern = re.compile("^[A-Z]$")

    @property
    def alive(self):
        """Check if player alive"""
        return len(self.incorrects) < 12

    @property
    def solved(self):
        """Check if player solved"""
        return "_" not in self.masked

    @property
    def unmasked(self):
        """Show word unmasked"""
        return self._word

    @property
    def masked(self):
        """Show word masked"""
        return " ".join([x if x in self._guesses else "_" for x in self._word])

    @property
    def incorrects(self):
        """Shows incorrect guesses"""
        return [x for x in self._guesses if x not in self._word]

    #@property
    def guess(self, letter):
        """Handles the guess"""
        letter = letter.upper()
        if self._valid_input_pattern.match(letter):
            if letter not in self._guesses:
                self._guesses.append(letter)
            else:
                raise GuessError(f"ERROR: Already guessed letter {letter}")
        else:
            raise GuessError("ERROR: Please enter a single letter.")
