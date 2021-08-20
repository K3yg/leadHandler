from config import *
from model import PessoaFisica, PessoaJuridica

@app.route('/', methods=['GET', 'POST'])
def index():
    clientes_fisico = PessoaFisica.query.all()
    clientes_juridico = PessoaJuridica.query.all()

    return render_template('index.html', clientes_fisico=clientes_fisico, 
    clientes_juridico=clientes_juridico)

