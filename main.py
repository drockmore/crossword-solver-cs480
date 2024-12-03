from config import CROSSWORD_PUZZLE, NUMBER_VARIABLES
from classes.Puzzle import Puzzle
from classes.Words import Words
from classes.Backtrack import Backtrack
from puzzleHelpers import print_default_puzzle
import time

def crossword_solver():
    
    # Print the initial puzzle
    print("Solver started, Initial crossword puzzle: \n")
    print_default_puzzle(CROSSWORD_PUZZLE)
    
    #init words
    words = Words()
    
    #init puzzle
    puzzle = Puzzle(CROSSWORD_PUZZLE)
    
    #load variables into puzzle
    puzzle.load_variables(NUMBER_VARIABLES)
    
    #init solver
    backtrack = Backtrack(puzzle)
    
    #start time tracking
    start_time = time.time()
    backtrack.solve(words)
    end_time = time.time()
    

    
    print("\n\n-----------------| Solver Results |-----------------")
    
    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print(f"\nFunction execution time: {elapsed_time:.4f} seconds. \n")
    
    print(f"Variables: \n")
    
    direction = "Direction"
    length = "Length"
    starting_cell = "Starting Cell"
    ending_cell = "Ending Cell"
    word = "Word"
  
    print(f"{direction:<14} | {length:<4} | {starting_cell:<10} | {ending_cell:<10} | {word:<20}")
    print("-" * 66)
    print(puzzle.variables)
    
    print(f"\nSolved Puzzle: \n")
    print(puzzle.print_puzzle_with_words())
    
    return


if __name__ == "__main__":
    crossword_solver()


def variable_table_heading():
    
    direction = "Direction"
    length = "Length"
    starting_cell = "Starting Cell"
    ending_cell = "Ending Cell"
    word = "Word"
  
    print(f"{direction:<14} | {length:<10} | {starting_cell:<20} | {ending_cell:<20} | {word:<20}")
    print("-" * 66)