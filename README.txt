hangman
=======
Python-based console version of Hangman
This project includes unittest and coverage report

Getting Started
===============
This project is running on Windows 10 using Ubuntu 18.04 app and Python 3.6

Prerequisites
=============
Make git repository directory from your home directory, setup hangman remote, pull hangman from master and Export your python src code path so that game will pick up the hangman package.

cd
mkdir -p git/hangman
cd git/hangman
git init
git remote add hangman https://github.com/morrisfd/hangman.git
git pull hangman master
export PYTHONPATH=$PYTHONPATH:~/git/hangman/src

To run test.sh you will need to install pip3 and coverage.
    1. pip3 
         sudo apt install python3-pip
    2. coverage
         pip3 install coverage

To run pylint install from pip3
    1. pylint
        pip3 install pylint

Running the tests and coverage report
=====================================
From the root directory ("~/git/hangman") run the test.sh script. This will run all unit test and give a coverage report.

cd ~/git/hangman
./test.sh

Running individual tests
========================
From the tests directory ("~/git/hangman/tests") run each test with pylint

cd ~/git/hangman/tests
./test_dictionary.py
./test_word.py
./test_screen.py
./test_game.py

Running pylint (source-code, bug and quality checker for Python)
========================
cd ~/git/hangman/src/hangman
pylint dictionary.py
pylint word.py
pylint cli/screen.py
pylint game.py
