
# Monte Carlo Simulator

Author: Ran Gao

## Synopsis

This Monte Carlo Simulator consists of three classes (Die, Game, and Analyzer) that work together to generate various outcomes for dice games. The simulator allows you to create custom dice, play games with specified dice configurations, and analyze the results.

### Installation

No installation is required. Simply download the `montecarlo.py` and `montecarlo_tests.py` files and place them in your working directory.

### Usage

Below is a simple example of how to use the Monte Carlo Simulator to create dice, play games, and analyze the results:

```python
from montecarlo import Die, Game, Analyzer

# Creating dice
fair_die = Die()
unfair_die = Die(weights=[1, 1, 1, 1, 1, 5])

# Playing games
game = Game([fair_die, unfair_die])
game.play(1000)

# Analyzing games
analyzer = Analyzer(game)
analyzer.combo()
top_combos = analyzer.combo_results.head(10)

print(top_combos)


```



## API Description 

### Die Class
Die class represents a die with customizable faces and weights.

Methods

__init__(self, faces, weights=None)

Initializes a Die object with given faces and optional weights.

Parameters:
faces (list): The faces of the die.   
weights (list, optional): The weights of the faces. Defaults to None, which means all faces have equal probability.

set_weight(self, face, weight)
Sets the weight of a specific face.

Parameters:   
face: The face whose weight you want to set.  
weight (float): The new weight for the face.
    
roll(self)
Rolls the die and returns the result.

Returns:
The face value of the rolled die.


### Game Class
Game class represents a game played with a set of dice.

Methods
__init__(self, dice)

Initializes a Game object with the given dice.

Parameters:

dice (list): A list of Die objects.
play(self, n)

Plays the game n times and stores the outcomes.

Parameters:

n (int): The number of times the game should be played.
    
    
### Analyzer Class
Analyzer class analyzes the results of a Game object.

Methods
__init__(self, game)

Initializes an Analyzer object with the given game.

Parameters:
game (Game): A Game object.
combo(self)

Analyzes the game results and calculates the frequencies of different face combinations.

Returns:
A pandas DataFrame with the face combinations and their frequencies.




# Manifest

## montecarlo.py: The main module containing the Die, Game, and Analyzer classes.
## montecarlo_tests.py: Unit tests for the Die, Game, and Analyzer classes.
## montecarlo_demo.ipynb: A Jupyter Notebook demonstrating the usage of the Monte Carlo Simulator.
## README.md: This README file.