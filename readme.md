# Crossword solver

## Overview
This project is a crossword solver for cs480.

## Requirements
- Python 3.8 or higher
- Virtual environment setup (optional but recommended)

## Installation
```
pip install -r requirements.txt
```

### Running the program
```
python main.py
```

## Configuration Options
The configuration options are located in `config.py` and has the following variables:

**`WORD_FILE`** This is the location for the .txt file containing the list of words.
**`VARIABLE_HEURISTIC`** This determines which heuristic is used when solving. The options are "default", "mrv", and "degree".
**`WORD_SELECTION_HEURISTIC`** This determines if a heuristic will also used when selecting a word. The options are "default", and "lcv". 

**`CROSSWORD_PUZZLE`** This determines which crossword puzzle will be used. Import a puzzle into the configuration file and add it to this variable to use a different puzzle.

**`NUMBER_VARIABLES`** This is the number of variables to solved in the puzzle. It must match the number of variables in the CROSSWORD_PUZZLE variable.