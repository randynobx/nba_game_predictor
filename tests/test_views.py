'''Test module'''

from nba_game_predictor import create_app

test_boxscore = {
    'h_fgm': 40, 'h_fga': 80, 'h_3pm': 13,'h_ftm': 9,
    'h_fta': 17, 'h_trb': 42, 'h_orb': 10, 'h_tov': 17,
    'a_fgm': 37, 'a_fga': 90, 'a_3pm': 8, 'a_ftm': 27,
    'a_fta': 33, 'a_trb': 48, 'a_orb': 16, 'a_tov': 9
}

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
        response = self.flask_app.test_client().post('/predict'
                                                     , data=test_boxscore)

        assert response.status_code == 200
        assert b" team" in response.data # A prediction has been made

    def test_about_route(self):
        '''Test about page'''
        response = self.flask_app.test_client().get('/about')

        assert response.status_code == 200
