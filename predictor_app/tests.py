'''Test module'''

from . import calculations, create_app

test_boxscore = {
    'h_fgm': 40, 'h_fga': 80, 'h_3pm': 13,'h_ftm': 9,
    'h_fta': 17, 'h_trb': 42, 'h_orb': 10, 'h_tov': 17,
    'a_fgm': 37, 'a_fga': 90, 'a_3pm': 8, 'a_ftm': 27,
    'a_fta': 33, 'a_trb': 48, 'a_orb': 16, 'a_tov': 9
}

test_fourfactors = {
    'h_efg':0.581250, 'a_efg':0.455556, 'h_tov':0.162711,
    'a_tov':0.079281, 'h_drb':0.666667, 'a_drb':0.761905,
    'h_ftr':0.112500, 'a_ftr':0.300000
}

class TestCalculation:
    '''Tests for calculations.py'''

    def test_calc_fourfactors(self) -> None:
        '''Test calc_fourfactors()'''
        out_df = calculations.calc_fourfactors(test_boxscore)
        assert isinstance(out_df, dict), 'Output is not a dictionary'
        assert len(out_df) == 8, \
            f'Output not the correct size of 8 keys: got {len(out_df)} keys'

    def test_predict_winner(self) -> None:
        '''Test predict_winner'''
        winner, proba = calculations.predict_winner(test_fourfactors)
        assert winner in ['Home team', 'Away team'], \
            f'Unknown winner returned: {winner}'
        assert .5 < proba <= 1, \
            f'Win probability out of bounds (.5 < proba <= 1): {proba}'

class TestViews:
    '''Tests for views.py'''

    flask_app = create_app()

    def test_index_route(self):
        '''Test index view'''
        response = self.flask_app.test_client().get('/')

        assert response.status_code == 302 # Redirected response =>/predict

    def test_predict_route(self):
        '''Test predict view'''
        response = self.flask_app.test_client().get('/predict')

        assert response.status_code == 200
        assert b" team" not in response.data # No prediction has been made

    def test_upload_and_predict_route(self):
        '''Test upload_and_predict'''
        response = self.flask_app.test_client().post('/predict', data=test_boxscore)

        assert response.status_code == 200
        assert b" team" in response.data # A prediction has been made

    def test_about_route(self):
        '''Test about page'''
        response = self.flask_app.test_client().get('/about')

        assert response.status_code == 200
