from unittest import mock
from unittest import TestCase
import Penalty_Shooters

class TestPenaltyShooters(TestCase):
    @mock.patch('Penalty_Shooters.input', create=True)
    def testgame(self, mocked_input):
        # mock the input for purpose of unit test, 2 games to test, energies of 4 9 5 and 10 13 7 in each game.
        mocked_input.side_effect = ['2', '4 9 5', '10 13 7']
        result = Penalty_Shooters.game
        # expected result given energies are 3 and 2 goals each and then 0 and 3 goals each.
        self.assertEqual(result, {'3 2': '0 3'})