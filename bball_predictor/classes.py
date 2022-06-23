from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class BoxScoreForm(FlaskForm):
    h_fgm = IntegerField("h_fgm", validators=[DataRequired()])
    h_fga = IntegerField("h_fga", validators=[DataRequired()])
    h_3pm = IntegerField("h_3pm", validators=[DataRequired()])
    h_ftm = IntegerField("h_ftm", validators=[DataRequired()])
    h_fta = IntegerField("h_fta", validators=[DataRequired()])
    h_trb = IntegerField("h_trb", validators=[DataRequired()])
    h_orb = IntegerField("h_orb", validators=[DataRequired()])
    h_tov = IntegerField("h_tov", validators=[DataRequired()])
    a_fgm = IntegerField("a_fgm", validators=[DataRequired()])
    a_fga = IntegerField("a_fga", validators=[DataRequired()])
    a_3pm = IntegerField("a_3pm", validators=[DataRequired()])
    a_ftm = IntegerField("a_ftm", validators=[DataRequired()])
    a_fta = IntegerField("a_fta", validators=[DataRequired()])
    a_trb = IntegerField("a_trb", validators=[DataRequired()])
    a_orb = IntegerField("a_orb", validators=[DataRequired()])
    a_tov = IntegerField("a_tov", validators=[DataRequired()])

class FourFactorsForm(FlaskForm):
    h_efg = IntegerField('h_efg', validators=[DataRequired()])
    h_tov = IntegerField('h_tovr', validators=[DataRequired()])
    h_drb = IntegerField('h_drbr', validators=[DataRequired()])
    h_ftr = IntegerField('h_ftr', validators=[DataRequired()])
    a_efg = IntegerField('a_efg', validators=[DataRequired()])
    a_tov = IntegerField('a_tovr', validators=[DataRequired()])
    a_drb = IntegerField('a_drbr', validators=[DataRequired()])
    a_ftr = IntegerField('a_ftr', validators=[DataRequired()])
