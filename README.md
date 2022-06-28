# NBA Game Predictor

## Introduction
<p>NBA Game Predictor uses the [Four Factors](https://www.nbastuffer.com/analytics101/four-factors/) to predict the outcome of nba regular season games.</p>

<p>At the end of the day, basketball may be 'about getting buckets', but there is a lot more that goes on within the game that has significant impact on which team ends up getting those buckets. What Dean Oliver coined as the 'Four Factors' summerizes the most important parts of the game captured by the traditional box score. Each of these four composite statistics can be calculated for each team to directly compare how each team fared using percentages or rates.</p>

## The Four Factors
### Effective Field Goal Percentage (EFG%)
- *Formula:* EFG% = (FieldGoalsMade + 0.5 * 3ptFieldGoalsMade) / FieldGoalsAttempted
- *Purpose:* EFG% gives a measure of how efficently a team is scoring relative to their field goal attempts. Three point field goals are given extra weight because of the additional point they provide when made.
### Turnover Percentage (TOV%)
- *Formula:* TOV% = Turnovers / (FieldGoalsAttempted + 0.44 * FreeThrowsAttempted + Turnovers)
- *Purpose:* TOV% is the percentage of total possesions that ended in a turnover.
### Defensive Rebounding Percentage (DRB%)
- *Formula:* DRB% = DefensiveRebounds / (OpponentOffensiveRebounds + DefensiveRebounds)
- *Purpose:* DRB% is the percentage of available rebounds that a team claimed while on defense. This measure is sometimes measured as Offensive RB%, which is the same measure but from the opposite perspective.
### Free Throw Rate (FTR).
- *Formula:* FTR = FreeThrowsMade / FieldGoalAttempts
- *Purpose:* FTR is a measure of how often a team gets to the foul line. It is traditionally measured as `FreeThrowsMade / FieldGoalAttempts` or as `FreeThrowAttempts / FieldGoalAttempts`.

*For detailed information on these metrics, see Dean Oliver's "Basketball on Paper".*

## Conclusions

- While all essential to winning basketball games, not all four metrics are weighted evenly. When examining feature and permutation importances in the models, I came to the same approximate weights that Dean Oliver found, with the slight exception of Rebounding being weighted slightly less and Shooting slightly more.
    1. Shooting (40%)
    2. Turnovers (25%)
    3. Rebounding (20%)
    4. Free Throws (15%)
- Home court advantage does not seem to be an independently relevant factor in the regular season games used for modeling. It is possible that homecourt advantage shows in the improvement of other metics such as shooting or free throw rate. Further examination of this question is beyond the scope of this project, and would make an interesting topic for future study.