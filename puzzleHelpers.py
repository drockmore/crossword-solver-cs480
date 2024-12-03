
def print_default_puzzle(puzzle):
    
    printed_grid = []
    
    outside_border_str = ""
    for i in range(0, len(puzzle[0])):
        outside_border_str += ("+----")
        if i == len(puzzle[0]) - 1:
            outside_border_str += ("+")
        
    printed_grid.append(outside_border_str)

    rowStr = ""
    for row in puzzle:
        for cell in row:
            rowStr += f"| {cell:<2} "
            #rowStr += ("| " + str(cell if cell != '' else ' ') + " ")
        rowStr += ("|")
        printed_grid.append(rowStr)
        printed_grid.append(outside_border_str)
        rowStr = ""
        
    for line in printed_grid:
        print(line)
    
    
    

def get_variable_length_words(words):
    variable_length_words = []
    for word in words:
        if len(word) not in variable_length_words:
            variable_length_words.append(len(word))
    return variable_length_words
