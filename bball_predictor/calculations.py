# Wrangle
import pandas as pd
import pickle as pk

def calc_fourfactors(df):
    '''Calculate four factors for each team'''
    X = {}
    h_dreb = df['h_trb'] - df['h_orb']
    a_dreb = df['a_trb'] - df['a_orb']
    
    # Shooting : (FG + 0.5 * 3FG) / FGA
    X['h_efg'] = (df['h_fgm'] + 0.5 * df['h_3pm']) / df['h_fga']
    X['a_efg'] = (df['a_fgm'] + 0.5 * df['a_3pm']) / df['a_fga']
    
    # Turnovers : TOV / (FGA + 0.44 * FTA + TOV)
    X['h_tov'] = df['h_tov'] / (df['h_fga'] + 0.44 * df['h_fta'] + df['h_tov'])
    X['a_tov'] = df['a_tov'] / (df['a_fga'] + 0.44 * df['a_fta'] + df['h_tov'])
    
    # Rebounding : DRB / (Opp ORB + DRB)
    X['h_drp'] = h_dreb / (df['a_orb'] + h_dreb)
    X['a_drp'] = a_dreb / (df['h_orb'] + a_dreb)
    
    # Freethrows : FT / FGA
    X['h_ftr'] = df['h_ftm'] / df['h_fga']
    X['a_ftr'] = df['a_ftm'] / df['a_fga']
        
    return X

def predict_winner(X):
    '''Return winner of game and probability of expected result'''
    # load model
    with open('bball_predictor/model.pickle', 'rb') as f:
        model = pk.load(f)
    # predict
    X = pd.DataFrame(X, index=[0]).astype(float)
    result =  model.predict(X)[0]
    proba = round(model.predict_proba(X).max(), 3)
    if result == 1:
        return 'Home team', proba
    else:
        return 'Away team', proba