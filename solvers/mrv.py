# mrv.py
# generated with the help of chatGPT 4.o
def select_variable_with_mrv(vertex, variables, get_valid_domain):
    """
    Select the next variable to assign using the MRV heuristic.
    """
    mrv_variable = None
    min_domain_size = float('inf')

    for variable in variables:
        
        if variable.has_word():  # Skip already assigned variables
            continue
        


        # Get the domain size for the current variable
        domain_size = len(get_valid_domain(variable))
        
   
        # Update the MRV variable if this domain size is smaller
        if domain_size < min_domain_size:
            mrv_variable = variable
            min_domain_size = domain_size

    return mrv_variable

# This function was generated with the help of chat gpt 4.o
def get_valid_domain(variable, words, is_word_valid_for_variable):
    """
    Get the list of valid words for a given variable based on constraints.
    """
    matching_words = words.get_words_by_length(variable.get_word_length())

    return [
        word for word in matching_words
        if not word.in_use and is_word_valid_for_variable(variable, word.text)
    ]
