import flask
from config import *
from model import PessoaFisica, PessoaJuridica, User
import flask_excel, pyexcel_xlsx
from io import BytesIO
from forms import LoginForm
flask_excel.init_excel(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
        logout_user()
        form = LoginForm()
        if form.validate_on_submit():
                user = User.query.filter_by(login=form.login.data).first()
                if user:
                        user.senha = bcrypt.generate_password_hash(form.senha.data)
                        if bcrypt.check_password_hash(user.senha, form.senha.data):
                                login_user(user)
                                return redirect(url_for('index'))
                        
        return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
        

@app.route('/lead_handler', methods=['GET', 'POST'])
@login_required
def index():

        lead_f = PessoaFisica.query.all()
        lead_j = PessoaJuridica.query.all()

        return render_template('index.html', lead_f=lead_f, 
        lead_j=lead_j)
        
@app.route("/lead_handler/export_f", methods=['GET'])
def export_f():
        colunas = ['nome', 'telefone', 'cidade', 'operadora', 'custo', 'internet', 'fixo', 'movel', 'data_cadastro']
        return flask_excel.make_response_from_query_sets(PessoaFisica.query.all(), colunas, "xlsx", file_name="leads_pf")
        #return flask_excel.make_response_from_a_table(db.session, PessoaFisica, "xlsx", file_name="leads_fisico")

@app.route("/lead_handler/export_j", methods=['GET'])
def export_j():
        colunas = ['nome', 'nome_empresa', 'setor', 'email', 'telefone', 'cidade', 'operadora', 'custo', 'internet', 'fixo', 'movel', 'linhas_moveis', 'data_cadastro']
        return flask_excel.make_response_from_query_sets(PessoaJuridica.query.all(), colunas, "xlsx",file_name="leads_pj")
        #return flask_excel.make_response_from_a_table(db.session, PessoaJuridica, "xlsx", file_name="leads_juridico")

@app.route('/lead_handler/download_f/<int:id>')
def download_f(id):

        file_data = PessoaFisica.query.filter_by(id=id).first()
        print(file_data)

        enviar_arquivo = send_file(BytesIO(file_data.fatura), attachment_filename='fatura.pdf',as_attachment=True)
        return enviar_arquivo

@app.route('/lead_handler/download_j/<int:id>')
def download_j(id):

        file_data = PessoaJuridica.query.filter_by(id=id).first()
        print(file_data)

        enviar_arquivo = send_file(BytesIO(file_data.fatura), attachment_filename='fatura.pdf', as_attachment=True)
        return enviar_arquivo



