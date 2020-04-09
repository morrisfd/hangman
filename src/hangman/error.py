"""Custome exceptions for hangman"""

class Error(Exception):
    """Base class for Hangman exceptions"""

class GuessError(Error):
    """Exceptions raised for an invalid guess"""
