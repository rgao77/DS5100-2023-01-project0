 # The Die class

    
import unittest
from montecarlo import Die

class TestDie(unittest.TestCase):
    """
    Test suite for the Die class.
    """

    def test_initialization(self):
        """
        Test if the Die object is initialized correctly.
        """
        die = Die([1, 2, 3, 4, 5, 6])
        self.assertIsNotNone(die)

    def test_set_weight(self):
        """
        Test if the set_weight method correctly updates the weight of a face.
        """
        die = Die([1, 2, 3, 4, 5, 6])
        die.set_weight(1, 2.0)
        result = die.show()
        self.assertEqual(result.loc[result['face'] == 1, 'weight'].values[0], 2.0)

    def test_roll(self):
        """
        Test if the roll method generates the correct number of outcomes.
        """
        die = Die([1, 2, 3, 4, 5, 6])
        outcomes = die.roll(10)
        self.assertEqual(len(outcomes), 10)
        
    def test_show(self):
        """
        Test if the show method returns a DataFrame with correct values and structure.
        """
        die = Die([1, 2, 3, 4, 5, 6])
        die.set_weight(1, 2.0)
        result = die.show()
        self.assertIsNotNone(result)
        self.assertEqual(result.loc[result['face'] == 1, 'weight'].values[0], 2.0)
        self.assertEqual(len(result), 6)
        
    
    
    

 # The Game class

import unittest
from montecarlo import Game

class TestGame(unittest.TestCase):
    """
    Test class for the Game class.
    """

    def test_initialization(self):
        """
        Test if the Game object is initialized properly.
        """
        dice = [Die([1, 2, 3, 4, 5, 6]) for _ in range(5)]
        game = Game(dice)
        self.assertIsNotNone(game)

    def test_play(self):
        """
        Test if the play method works correctly.
        """
        dice = [Die([1, 2, 3, 4, 5, 6]) for _ in range(5)]
        game = Game(dice)
        game.play(10)
        results = game.show(form='wide')
        self.assertEqual(results.shape, (10, 5))
        
    def test_show_wide(self):
        """
        Test if the show method returns the correct output in wide form.
        """
        dice = [Die([1, 2, 3, 4, 5, 6]) for _ in range(5)]
        game = Game(dice)
        game.play(10)
        results = game.show(form='wide')
        self.assertEqual(results.shape, (10, 5))

    def test_show_narrow(self):
        """
        Test if the show method returns the correct output in narrow form.
        """
        dice = [Die([1, 2, 3, 4, 5, 6]) for _ in range(5)]
        game = Game(dice)
        game.play(10)
        results = game.show(form='narrow')
        self.assertEqual(results.shape, (50, 1))
        self.assertEqual(results.index.names, ['roll', 'die'])

    def test_show_invalid_option(self):
        """
        Test if the show method raises a ValueError for an invalid form option.
        """
        dice = [Die([1, 2, 3, 4, 5, 6]) for _ in range(5)]
        game = Game(dice)
        game.play(10)
        with self.assertRaises(ValueError):
            game.show(form='invalid')
            
            
            
            

        
# The Analyzer class

import unittest
from montecarlo import Analyzer

class TestAnalyzer(unittest.TestCase):
    """
    Test suite for the Analyzer class.
    """

    def test_initialization(self):
        """
        Test if the Analyzer object is initialized correctly with a Game object.
        """
        dice = [Die([1, 2, 3, 4, 5, 6]) for _ in range(5)]
        game = Game(dice)
        game.play(10)
        analyzer = Analyzer(game)
        self.assertIsNotNone(analyzer)

    def test_jackpot(self):
        """
        Test if the jackpot method computes the correct number of identical face outcomes.
        """
        dice = [Die([1, 1, 1]) for _ in range(3)]
        game = Game(dice)
        game.play(10)
        analyzer = Analyzer(game)
        jackpot_count = analyzer.jackpot()
        self.assertEqual(jackpot_count, 10)

    def test_combo(self):
        """
        Test if the combo method computes the distinct combinations of faces rolled and their counts.
        """
        dice = [Die([1, 2, 3]) for _ in range(3)]
        game = Game(dice)
        game.play(10)
        analyzer = Analyzer(game)
        analyzer.combo()
        self.assertIsNotNone(analyzer.combo_results)

    def test_face_counts(self):
        """
        Test if the face_counts method computes the number of times a given face is rolled in each event.
        """
        dice = [Die([1, 2, 3]) for _ in range(3)]
        game = Game(dice)
        game.play(10)
        analyzer = Analyzer(game)
        analyzer.face_counts()
        self.assertIsNotNone(analyzer.face_counts_per_roll)

        
if __name__ == '__main__':
    unittest.main(verbosity=2)