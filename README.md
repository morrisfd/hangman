##############################################################################

#Export your python src code path so that we will pick up the hangman package.
# "~/git/hangman" is the directory where you code resides. Adjust this if yours differs.
export PYTHONPATH=$PYTHONPATH:~/git/hangman/src

#To run test.sh you will need to install pip3 and coverage.
#    1. pip3 
         sudo apt install python3-pip
#    2. coverage
         pip3 install coverage

#To run pylint install from pip3
#    1. pylint
        pip3 install pylint: