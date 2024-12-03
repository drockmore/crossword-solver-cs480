# This function was created with the help of chatgpt 4.o
def select_variable_with_degree(variables, get_intersecting_variables):
    """
    Select the next variable to assign using the Degree Heuristic.

    Parameters:
    - variables: List of variables to choose from.
    - get_intersecting_variables: A function that returns intersecting variables for a given variable.

    Returns:
    - Variable: The variable with the highest degree (most constraints).
    """
    max_degree = -1
    selected_variable = None

    for variable in variables:
        if variable.has_word():  # Skip assigned variables
            continue

        # Use the provided get_intersecting_variables function
        degree = len(get_intersecting_variables(variable))

        # Select the variable with the highest degree
        if degree > max_degree:
            max_degree = degree
            selected_variable = variable

    return selected_variable
