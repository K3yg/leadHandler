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

    nomes = ['claudio', 'jonas', 'valter']
    nome_count = 0

    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

        writer.writeheader()

        for nome in nomes:
            nome_count += 1
            writer.writerow({'first_name': nome, 'last_name': 'santos'})


    path =  os.path.dirname(os.path.abspath(__file__))    
    print(path)

    return render_template('index.html', clientes_fisico=clientes_fisico, 
    clientes_juridico=clientes_juridico)

