# NBA Game Predictor

## Introduction

NBA Game Predictor uses the [Four Factors](https://www.nbastuffer.com/analytics101/four-factors/) to predict the outcome of nba regular season games.

At the end of the day, basketball may be 'about getting buckets', but there is a lot more that goes on within the game that has significant impact on which team ends up getting those buckets. What Dean Oliver coined as the 'Four Factors' summerizes the most important parts of the game captured by the traditional box score. Each of these four composite statistics can be calculated for each team to directly compare how each team fared using percentages or rates.

Using these four factors, I've created a simple prediction app using the SK-Learn library and Flask to predict the winner of a given NBA basketball game given its final boxscore (without points).

For instructions on how to run this project on your machine, please see the [Usage](#usage) section below.

---

### Contents
- [How it works](#how-it-works)
- [Research Conclusions](#research-conclusions)
- [Usage](#usage)
    - [Makefile](#makefile)
    - [Docker](#docker)
    - [Pipenv](#pipenv)

---

## How it works

### The Four Factors

#### Effective Field Goal Percentage (EFG%)

- *Formula:* EFG% = (FieldGoalsMade + 0.5 * 3ptFieldGoalsMade) / FieldGoalsAttempted
- *Purpose:* EFG% gives a measure of how efficently a team is scoring relative to their field goal attempts. Three point field goals are given extra weight because of the additional point they provide when made.

#### Turnover Percentage (TOV%)

- *Formula:* TOV% = Turnovers / (FieldGoalsAttempted + 0.44 * FreeThrowsAttempted + Turnovers)
- *Purpose:* TOV% is the percentage of total possesions that ended in a turnover.

#### Defensive Rebounding Percentage (DRB%)

- *Formula:* DRB% = DefensiveRebounds / (OpponentOffensiveRebounds + DefensiveRebounds)
- *Purpose:* DRB% is the percentage of available rebounds that a team claimed while on defense. This measure is sometimes measured as Offensive RB%, which is the same measure but from the opposite perspective.

#### Free Throw Rate (FTR)

- *Formula:* FTR = FreeThrowsMade / FieldGoalAttempts
- *Purpose:* FTR is a measure of how often a team gets to the foul line. It is traditionally measured as `FreeThrowsMade / FieldGoalAttempts` or as `FreeThrowAttempts / FieldGoalAttempts`.

*For detailed information on these metrics, see [Dean Oliver's "Basketball on Paper"](http://www.basketballonpaper.com/).*

### Research Conclusions

- While all essential to winning basketball games, not all four metrics are weighted evenly. When examining feature and permutation importances in the models, I came to the same approximate weights that Dean Oliver found, with the slight exception of Rebounding being weighted slightly less and Shooting slightly more.
    1. Shooting (40%)
    2. Turnovers (25%)
    3. Rebounding (20%)
    4. Free Throws (15%)
- Home court advantage does not seem to be an independently relevant factor in the regular season games used for modeling. It is possible that homecourt advantage shows in the improvement of other metics such as shooting or free throw rate. Further examination of this question is beyond the scope of this project, and would make an interesting topic for future study.

---

## Usage

There are two ways to run the code in this project: using Docker or with pipenv. Docker is the recommended way to run the app with minimal work and maximum compatibility. If you are interested in exploring `notebook.ipynb`, you should following the instructions for pipenv.


### Makefile

*For ease of use, a Makefile has been included to make the following operations (and more) as simple as possible.*

```bash
% make init # install only packages to run flask app, uses pipenv

% make init-dev # install packages for flask app, testing, and notebook.ipynb

% make test # run test suite

% make flask # run flask application locally

% make docker_build # build Docker image

% make docker_run # run Docker image
```

### Docker

While in the main project directory (`nba_game_predictor`), run the following command in your shell to build an image:

```bash
% docker build -t nba_game_predictor .
```

Once built, use the `docker run` command to create and run a container:

```bash
% docker run -p 5000:5000 nba_game_predictor
```

Setup is now complete!

You may now access the app in your web browser of choice at `localhost:5000`

### pipenv

If you want to work with the notebook, or don't want to use Docker, you can use pipenv to create a virtualized local environment.

First setup your environment with `pipenv`. Use the `--dev` flag if you are planning on using the notebook or test suite.

```bash
% pipenv install --dev
```

If you are only using the notebook, you are done!

To run the flask app, you will need to add the FLASK_APP environment variable:

```bash
% export FLASK_APP=nba_game_predictor
```

and run flask:

```bash
% flask run
```
