# This function was created with the help of chatgpt 4.o
def order_values_with_lcv(variable, words, puzzle, intersecting_variables):
    """
    Order the domain values (words) for a variable using the LCV heuristic.
    """
    def count_constraints(word):
        count = 0

        # Temporarily assign the word to the variable
        variable.set_word(word)
        word.mark_in_use()

        # Cache domain sizes for intersecting variables
        for intersecting_var in intersecting_variables(variable):
            intersecting_domain = [
                w for w in words.get_words_by_length(intersecting_var.get_word_length())
                if not w.in_use and puzzle.is_word_valid_for_variable(intersecting_var, w.text)
            ]
            domain_size = len(intersecting_domain)
            if domain_size == 0:
                # Early exit: this word makes the puzzle unsolvable for an intersecting variable
                variable.unset_word()
                word.mark_not_in_use()
                return float('inf')
            count += domain_size

        # Undo the temporary assignment
        variable.unset_word()
        word.mark_not_in_use()

        return count

    # Get valid words for the variable
    matching_words = words.get_words_by_length(variable.get_word_length())
    valid_words = [
        word for word in matching_words
        if not word.in_use and puzzle.is_word_valid_for_variable(variable, word.text)
    ]

    # Sort words by the number of constraints they impose on other variables (ascending)
    return sorted(valid_words, key=count_constraints)