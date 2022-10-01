"""Test calculations.py module"""

from nba_game_predictor import calculations
from test_assets import test_boxscore, test_fourfactors


class TestCalculation:
    """Tests for calculations.py"""

    def test_calc_fourfactors(self) -> None:
        """Test calc_fourfactors()"""
        out_df = calculations.calc_fourfactors(test_boxscore)
        assert isinstance(out_df, dict), 'Output is not a dictionary'
        assert len(out_df) == 8, \
            f'Output not the correct size of 8 keys: got {len(out_df)} keys'

    def test_predict_winner(self) -> None:
        """Test predict_winner"""
        winner, proba = calculations.predict_winner(test_fourfactors)
        assert winner in ['Home team', 'Away team'], \
            f'Unknown winner returned: {winner}'
        assert .5 < proba <= 1, \
            f'Win probability out of bounds (.5 < proba <= 1): {proba}'
