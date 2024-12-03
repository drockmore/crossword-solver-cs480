from classes.Variable import Variables

class Puzzle:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.variables: Variables = Variables()

        
    #Setters
    def set_puzzle(self, new_puzzle):
        self.puzzle = new_puzzle
    
    def set_variables(self, new_variables):
        self.variables = new_variables
        
    def add_variable(self, new_variable):
        self.variables.append(new_variable)
        

  
    def load_variables(self, NUMBER_VARIABLES):
        """
        Load variables for the puzzle.
        """
        self.createVariables(NUMBER_VARIABLES)
        
        
        
    def createVariables(self, NUMBER_VARIABLES):
        """
        Create variables for the puzzle.
        """
        for i in range(1, NUMBER_VARIABLES + 1):
            location = self.find_variable_location(i)
        
            horizontalExists, horizontalEnd = self.find_variable_end(i, "horizontal", location) 
            verticalExists, verticalEnd = self.find_variable_end(i, "vertical", location) 
        
            if horizontalExists:
                self.variables.add_variable(i, "horizontal", location, horizontalEnd, [])

            if verticalExists:
                self.variables.add_variable(i, "vertical", location, verticalEnd, [])
    
    def find_variable_location(self, cell_value):
        """
        Finds the coordinates of a specific cell value in the puzzle grid.

        Parameters:
        - cell_value (int): The value of the cell to search for.

        Returns:
        - (row, col) tuple if found, None otherwise.
        """
        for row_idx, row in enumerate(self.puzzle):
            for col_idx, value in enumerate(row):
                if value == cell_value:
                    return (row_idx, col_idx)  # Return the coordinates as (row, col)
        return None  # Return None if the cell value is not found
    
    def find_variable_end(self, variable, direction, location):
        """
        Finds the coordinates of a specific cell value in the puzzle grid.

        Parameters:
        - cell_value (int): The value of the cell to search for.

        Returns:
        - (row, col) tuple if found, None otherwise.
        """
        # Get the length of the variable
        length = len(self.puzzle[0]) if direction == "horizontal" else len(self.puzzle)
        endValue = 0
        startValue = location[1] if direction == "horizontal" else location[0]
        exists = True
   
   
        for col in range(length):
            colValue = self.puzzle[location[0]][col] if direction == "horizontal" else self.puzzle[col][location[1]]

            if colValue == '':
                endValue = col
                continue
            
            elif colValue == '#' and col < startValue:
                exists = True
                continue
            
            elif colValue == '#' and col > startValue:
                break 
            
            elif colValue < variable and col < startValue:
                exists = False
                continue
   
            elif colValue < variable and col > startValue:
                exists = False
                break 
            
            else:
                endValue = col
        
        endArr = [location[0], endValue] if direction == "horizontal" else [endValue, location[1]]
        
 
        if location[0] == endArr[0] and location[1] == endArr[1]:
            exists = False
        
        return exists, endArr
         
                
    def is_word_valid_for_variable(self, variable, word: str) -> bool:
        """
        Check if a word is valid to assign to a given variable.
        
        Parameters:
        - variable (Variable): The variable to which the word is being assigned.
        - word (str): The word being checked for validity.

        Returns:
        - bool: True if the word is valid for the variable, False otherwise.
        """
        # Step 1: Check length
        if len(word) != variable.get_word_length():
            return False  # Length mismatch
        
        # Step 2: Check intersections for compatibility
        start_row, start_col = variable.start
        
        for i in range(variable.get_word_length()):
            # Get the cell position based on direction
            row, col = (start_row, start_col + i) if variable.direction == "horizontal" else (start_row + i, start_col)
            
            # Check for intersections with other variables
            for other_variable in self.variables:
                if other_variable == variable:
                    continue  # Skip itself
                
                # Get cells occupied by the other variable
                if (row, col) in self.get_occupied_cells(other_variable):
                    other_word = other_variable.word.text if other_variable.word else None
                    other_index = self.get_index_at_position(other_variable, row, col)
                    
                    # If the other variable has a word, check for a match at the intersection
                    if other_word and other_word[other_index] != word[i]:
                        return False  # Mismatch found at an intersection

        return True  # All checks passed, word is valid for this variable

    def get_occupied_cells(self, variable):
        """
        Get all cells occupied by a variable.

        Parameters:
        - variable (Variable): The variable to check.

        Returns:
        - list of tuples: List of (row, col) positions occupied by the variable.
        """
        occupied = []
        start_row, start_col = variable.start
        length = variable.get_word_length()
        
        for i in range(length):
            if variable.direction == "horizontal":
                occupied.append((start_row, start_col + i))
            else:
                occupied.append((start_row + i, start_col))
        
        return occupied

    def get_index_at_position(self, variable, row, col):
        """
        Get the index of the letter in the variable's word at the specified position.

        Parameters:
        - variable (Variable): The variable to check.
        - row, col (int): The position to check.

        Returns:
        - int: The index in the word corresponding to the position.
        """
        if variable.direction == "horizontal":
            return col - variable.start[1]
        else:
            return row - variable.start[0]
        
    #Generated with chatGPT 4.o
    def are_variables_intersecting(self, variable1, variable2):
        """
        Check if two variables intersect.
        
        Parameters:
        - variable1: The first variable.
        - variable2: The second variable.
        
        Returns:
        - bool: True if the variables intersect, False otherwise.
        """
        cells1 = self.get_occupied_cells(variable1)
        cells2 = self.get_occupied_cells(variable2)

        # Check if any cell is shared between the two variables
        return any(cell in cells2 for cell in cells1)
        
    def print_puzzle_with_words(self):
        # Create a copy of the self.puzzle grid to modify with the words
        filled_grid = [[cell for cell in row] for row in self.puzzle]

        # Place each variable's word in the grid
        for variable in self.variables:
            if variable.word is None:
                continue  # Skip self.variables that don't have an assigned word

            word = variable.word.text
            start_row, start_col = variable.start

            # Fill in the word in the grid based on the direction of the variable
            for i, letter in enumerate(word):
                row, col = (start_row, start_col + i) if variable.direction == "horizontal" else (start_row + i, start_col)
                filled_grid[row][col] = letter  # Place the letter in the correct cell

        # Print the filled grid
        printed_grid = []
        outside_border_str = "+---" * len(filled_grid[0]) + "+"
        printed_grid.append(outside_border_str)

        for row in filled_grid:
            row_str = ""
            for cell in row:
                #row_str += f"| {cell:<6} |"
                row_str += "| " + str(cell if cell != '' else ' ') + " "
            row_str += "|"
            printed_grid.append(row_str)
            printed_grid.append(outside_border_str)

        for line in printed_grid:
            print(line)

