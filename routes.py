from json import encoder
from flask.json import dumps, jsonify
from config import *
from model import PessoaFisica, PessoaJuridica
import flask_excel
import pyexcel_xlsx

flask_excel.init_excel(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    lead_f = PessoaFisica.query.all()
    lead_j = PessoaJuridica.query.all()

    return render_template('index.html', lead_f=lead_f, 
    lead_j=lead_j)
    
@app.route("/export_f", methods=['GET'])
def export_f():
        return flask_excel.make_response_from_tables(db.session, [PessoaFisica], "xlsx", file_name="leads_fisico")

@app.route("/export_j", methods=['GET'])
def export_j():
        return flask_excel.make_response_from_tables(db.session, [PessoaJuridica], "xlsx", file_name="leads_juridico")