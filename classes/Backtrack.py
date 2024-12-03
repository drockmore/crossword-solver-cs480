from classes.Words import Words
from classes.Puzzle import Puzzle
from config import VARIABLE_HEURISTIC, WORD_SELECTION_HEURISTIC
from solvers.mrv import select_variable_with_mrv, get_valid_domain
from solvers.lcv import order_values_with_lcv
from solvers.degree import select_variable_with_degree
class Backtrack:
    # Chat gpt 4.o helped with the -> None part. This helps with type hinting.
    def __init__(self, puzzle: Puzzle) -> None:
        self.puzzle: Puzzle = puzzle


    def solve(self, words: Words) -> bool:
        """
        Solve the puzzle using backtracking with optional heuristics.
        """
        cost = 0
        vertex = []  # List of tuples to keep track of assigned words
        variableIndex = 0  # Index to track which variable we're working on
        word_history = {variable.id: set() for variable in self.puzzle.variables}  # Track words tried per variable

        while True:
            cost += 1
     

            # Check if the puzzle is solved
            if all(variable.has_word() for variable in self.puzzle.variables):
                return False  # Puzzle solved
            
            # If a heuristic is being used for variable selection
            # mrv heuristic
            if VARIABLE_HEURISTIC == "mrv":
                current_variable = select_variable_with_mrv(vertex, self.puzzle.variables, lambda var: get_valid_domain(var, words, self.puzzle.is_word_valid_for_variable))
                current_variable_id = current_variable.id
               
            # degree heuristic
            if VARIABLE_HEURISTIC == "degree":
                current_variable = select_variable_with_degree(self.puzzle.variables, self.get_intersecting_variables)
                current_variable_id = current_variable.id

            # No heuristic 
            if VARIABLE_HEURISTIC == "default":
                current_variable = self.puzzle.variables[variableIndex]
                current_variable_id = current_variable.id

            if current_variable is None:
                print("ERROR: No variable selected!")
                return False

           

            # Get words of matching length and filter out previously tried words
            if(WORD_SELECTION_HEURISTIC == "lcv"):
                matchingWords = self.lcv_filter_words(self.puzzle.variables.find_variable_by_id(current_variable_id), words)
            else:
                matchingWords = words.get_words_by_length(self.puzzle.variables.find_variable_by_id(current_variable_id).get_word_length())
            
            
            # Filter the words
            availableWord = self.filter_words(
                self.puzzle.variables.find_variable_by_id(current_variable_id),
                word_history[current_variable_id],
                matchingWords
            )
            
            # Log current variable being solved.
            print(f"Current variable: {current_variable_id} .....  {vertex} ")
            
            if availableWord:
                # Assign the word and track it in history
                vertex.append((current_variable_id, availableWord))
                self.puzzle.variables.find_variable_by_id(current_variable_id).set_word(availableWord)
                word_history[current_variable_id].add(availableWord.text)  # Add to history only if assigned
                variableIndex += 1  # Move forward to the next variable
                
            else:
                
                # Backtrack: No valid word, so we undo the last assignment
                if len(vertex) > 0:
                    self.puzzle.variables.find_variable_by_id(current_variable_id).unset_word()
                    word_history[current_variable_id].clear()  # Clear history for the current variable
                    
                    last_variable_id = vertex.pop()
                    self.puzzle.variables.find_variable_by_id(last_variable_id[0]).unset_word()
                    variableIndex -= 1
                    
                    current_variable = None
                    current_variable_id = None
                    
                

    def lcv_filter_words(self, variable, words):
        return order_values_with_lcv(
            variable,
            words,
            self.puzzle,
            lambda var: self.get_intersecting_variables(var)
    )


    def filter_words(self, variable, history, words):
        """
        Filter words based on the constraints of the variable.
        
        Parameters:
        - variable (Variable): The variable to check.
        - words (list of str): List of words to filter.
        
        Returns:
        - list of str: Words that satisfy the constraints of the variable.
        """

        for word in words:
            if word.text not in history and not word.in_use and self.puzzle.is_word_valid_for_variable(variable, word.text):
                return word
        return None
        
        
        
        
    def get_intersecting_variables(self, variable):
        """
        Get all variables that intersect with the given variable.
        """
        intersecting_variables = []
        for other_variable in self.puzzle.variables:
            if other_variable == variable:
                continue
            if self.puzzle.are_variables_intersecting(variable, other_variable):
                intersecting_variables.append(other_variable)
        return intersecting_variables
        