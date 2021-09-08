from config import *
from model import User

class LoginForm(FlaskForm):                   
    login = StringField("login", validators=[DataRequired() ,InputRequired(),Length(min=1, max=40)], render_kw={"placeholder": "Email"})                   
    senha = PasswordField("Senha", validators=[DataRequired(), InputRequired(),Length(min=1, max=25)], render_kw={"placeholder": "Senha"})                   
    submit = SubmitField("Entrar")