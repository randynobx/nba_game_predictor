'''Unit tests'''

from . import calculations


class TestCalculation:
    '''Tests for calculations.py'''

    test_boxscore = {
        'h_fgm': 40, 'h_fga': 80, 'h_3pm': 13,'h_ftm': 9,
        'h_fta': 17, 'h_trb': 42, 'h_orb': 10, 'h_tov': 17,
        'a_fgm': 37, 'a_fga': 90, 'a_3pm': 8, 'a_ftm': 27,
        'a_fta': 33, 'a_trb': 48, 'a_orb': 16, 'a_tov': 9
    }
    test_fourfactors = {
        'h_efg':0.581250, 'o_efg':0.455556, 'h_tov':0.162711,
        'o_tov':0.079281, 'h_drb':0.666667, 'o_drb':0.761905,
        'h_ftr':0.112500, 'o_ftr':0.300000
    }

    def test_calc_fourfactors(self) -> None:
        '''Test calc_fourfactors()'''
        out_df = calculations.calc_fourfactors(self.test_boxscore)
        assert isinstance(out_df, dict), 'Output is not a dictionary'
        assert len(out_df) == 8, \
            f'Output not the correct size of 8 keys: got {len(out_df)} keys'

    def test_predict_winner(self) -> None:
        '''Test predict_winner'''
        winner, proba = calculations.predict_winner(self.test_fourfactors)
        assert winner in ['Home team', 'Away team'], \
            f'Unknown winner returned: {winner}'
        assert .5 < proba <= 1, \
            f'Win probability out of bounds (.5 < proba <= 1): {proba}'
