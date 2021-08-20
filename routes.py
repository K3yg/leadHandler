from config import *
from model import PessoaFisica, PessoaJuridica

@app.route('/', methods=['GET', 'POST'])
def index():
    clientes_fisico = PessoaFisica.query.all()
    clientes_juridico = PessoaJuridica.query.all()

    print(type(clientes_fisico))

    return render_template('index.html', clientes_fisico=clientes_fisico, 
    clientes_juridico=clientes_juridico)


@app.route('/export')
def export():
    clientes_fisico = PessoaFisica.query.all()
    clientes_juridico = PessoaJuridica.query.all()

    clientes = clientes_fisico + clientes_juridico


    return render_template('index.html', clientes_fisico=clientes_fisico, 
    clientes_juridico=clientes_juridico)

