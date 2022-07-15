# NBA Game Predictor Makefile

# Install app requirements only
init:
	pipenv install

# Install all requirements (required for running tests and notebook.ipynb)
init-dev:
	pipenv install --dev

test:
	pytest tests/test_*.py

# Run the flask application locally
flask:
	export FLASK_APP=nba_game_predictor && flask run

# Build Docker image
docker_build:
	docker build -t nba_game_predictor .

# Run Docker image
docker_run:
	docker run -p 5000:5000 nba_game_predictor