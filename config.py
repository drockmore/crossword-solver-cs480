from puzzles import CROSSWORD_PUZZLE_LARGE, CROSSWORD_PUZZLE_SMALL, CROSSWORD_PUZZLE_3, CROSSWORD_PUZZLE_HEART

#WORD_FILE =  "words_small.txt" 
WORD_FILE = "words_large.txt"

VARIABLE_HEURISTIC = "mrv"
#VARIABLE_HEURISTIC = "default"
#VARIABLE_HEURISTIC = "degree"

WORD_SELECTION_HEURISTIC = "default"  #"lcv", 

#CROSSWORD_PUZZLE = CROSSWORD_PUZZLE_LARGE
CROSSWORD_PUZZLE = CROSSWORD_PUZZLE_SMALL
#CROSSWORD_PUZZLE = CROSSWORD_PUZZLE_3

# This one is very slow
#CROSSWORD_PUZZLE = CROSSWORD_PUZZLE_HEART

# 8 variables for crossword_puzzle_small
# 11 variables for crossword_puzzle_large
# 33 variables for crossword_puzzle_heart
# 10 variables for crossword_puzzle_3
NUMBER_VARIABLES = 8


    