

# The Die class

import pandas as pd
import numpy as np

class Die:
    """
    This class represents a single die, which can be rolled to generate a random outcome based on weights.
    """

    def __init__(self, faces):
        """
        Initializes a Die object with the specified faces and default weights.
        :param faces: A list of unique elements (either strings or numbers) representing the faces of the die.
        """
        self._faces_weights = pd.DataFrame({'face': faces, 'weight': 1.0})
        
    def set_weight(self, face, new_weight):
        """
        Updates the weight of the specified face.
        :param face: The face whose weight needs to be updated.
        :param new_weight: The new weight (a float or convertible to float) for the specified face.
        """
        if face in self._faces_weights['face'].values and (isinstance(new_weight, (float, int)) or str(new_weight).replace('.', '', 1).isdigit()):
            self._faces_weights.loc[self._faces_weights['face'] == face, 'weight'] = float(new_weight)
        else:
            raise ValueError("Invalid face or weight.")
    
    def roll(self, num_rolls=1):
        """
        Rolls the die the specified number of times and returns the results as a list.
        :param num_rolls: The number of times the die is to be rolled, default is 1.
        :return: A list of outcomes.
        """
        outcomes = np.random.choice(self._faces_weights['face'], size=num_rolls, p=self._faces_weights['weight'] / self._faces_weights['weight'].sum())
        return list(outcomes)
    
    def show(self):
        """
        Returns the current set of faces and weights.
        :return: A DataFrame containing the faces and weights.
        """
        return self._faces_weights.copy()
    
    
    
    
    
    
#The Game class

class Game:
    """
    This class represents a game that uses one or more Die objects to generate outcomes.
    """

    def __init__(self, dice):
        """
        Initializes a Game object with a list of similarly defined Die objects.
        :param dice: A list of Die objects.
        """
        self._dice = dice
        self._results = None

    def play(self, num_turns):
        """
        Plays the game by rolling all dice the specified number of times.
        :param num_turns: The number of times the dice should be rolled.
        """
        results = []
        for turn in range(num_turns):
            for die_num, die in enumerate(self._dice):
                outcome = die.roll()[0]
                results.append({'roll': turn, 'die': die_num, 'outcome': outcome})

        self._results = pd.DataFrame(results)

    def show(self, form='wide'):
        """
        Returns the results of the most recent play in the specified form (narrow or wide).
        :param form: The form of the output DataFrame, either 'narrow' or 'wide'. Default is 'wide'.
        :return: A DataFrame containing the results of the most recent play.
        """
        if self._results is None:
            raise ValueError("No results available. Please play the game first.")

        if form == 'narrow':
            return self._results.set_index(['roll', 'die'])
        elif form == 'wide':
            return self._results.pivot(index='roll', columns='die', values='outcome')
        else:
            raise ValueError("Invalid form. Choose either 'narrow' or 'wide'.")
    
    
    
# The Analyzer class

    
class Analyzer:
    """
    This class analyzes the results of a single Game object and provides various statistical properties.
    """

    def __init__(self, game):
        """
        Initializes an Analyzer object with the results of a single Game object.
        :param game: A Game object.
        """
        self._results = game.show(form='narrow').reset_index()
        self._dtype = self._results['outcome'].dtype
        self.face_counts_per_roll = None
        self.jackpot_results = None
        self.combo_results = None

    def jackpot(self):
        """
        Computes the number of times the game resulted in all faces being identical.
        :return: An integer representing the number of times all faces were identical.
        """
        self.jackpot_results = self._results.groupby('roll')['outcome'].nunique()
        self.jackpot_results = self.jackpot_results[self.jackpot_results == 1]
        return len(self.jackpot_results)

    def combo(self):
        """
        Computes the distinct combinations of faces rolled and their counts.
        """
        self._results['outcome'] = self._results['outcome'].astype(str)
        self.combo_results = self._results.groupby('roll')['outcome'].apply(lambda x: tuple(sorted(x)))
        self.combo_results = self.combo_results.reset_index().groupby('outcome').size().reset_index(name='count')
        self.combo_results = self.combo_results.set_index(['outcome'])

    def face_counts(self):
        """
        Computes the number of times a given face is rolled in each event.
        """
        face_counts = self._results.pivot_table(index='roll', columns='outcome', values='die', aggfunc='count', fill_value=0)
        self.face_counts_per_roll = face_counts.astype(self._dtype)