import flask
from config import *
from model import PessoaFisica, PessoaJuridica
import flask_excel, pyexcel_xlsx
from io import BytesIO

flask_excel.init_excel(app)

@app.route('/', methods=['GET', 'POST'])
def index():

        lead_f = PessoaFisica.query.all()
        lead_j = PessoaJuridica.query.all()

        return render_template('index.html', lead_f=lead_f, 
        lead_j=lead_j)
        
@app.route("/export_f", methods=['GET'])
def export_f():
        colunas = ['id', 'nome']
        return flask_excel.make_response_from_query_sets(PessoaFisica.query.all(), colunas, "xlsx")
        #return flask_excel.make_response_from_a_table(db.session, PessoaFisica, "xlsx", file_name="leads_fisico")

@app.route("/export_j", methods=['GET'])
def export_j():
        colunas = ['id', 'nome']
        return flask_excel.make_response_from_query_sets(PessoaFisica.query.all(), colunas, "xlsx")
        #return flask_excel.make_response_from_a_table(db.session, PessoaJuridica, "xlsx", file_name="leads_juridico")

@app.route('/download_f/<int:id>')
def download_f(id):

        file_data = PessoaFisica.query.filter_by(id=id).first()
        print(file_data)

        enviar_arquivo = send_file(BytesIO(file_data.fatura), attachment_filename='fatura.pdf',as_attachment=True)
        return enviar_arquivo

@app.route('/download_j/<int:id>')
def download_j(id):

        file_data = PessoaJuridica.query.filter_by(id=id).first()
        print(file_data)

        enviar_arquivo = send_file(BytesIO(file_data.fatura), attachment_filename='fatura.pdf', as_attachment=True)
        return enviar_arquivo
