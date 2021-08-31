from config import *

def pegarDia():
    hoje = datetime.datetime.now()
    return hoje.day

class PessoaFisica(db.Model):
    __tablename__ = 'pessoa_fisica'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(100))

    cidade = db.Column(db.String(100))
    operadora = db.Column(db.String(100))
    custo = db.Column(db.String(100))
    internet = db.Column(db.String(100), nullable = True)
    fixo = db.Column(db.String(100), nullable = True)
    movel = db.Column(db.String(100), nullable = True)

    fatura = db.Column(db.LargeBinary, nullable = True)

    data_cadastro = db.Column(db.String(100))


class PessoaJuridica(db.Model):
    __tablename__ = 'pessoa_juridica'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100))
    nome_empresa = db.Column(db.String(100))
    setor = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(100))

    cidade = db.Column(db.String(100))
    operadora = db.Column(db.String(100))
    custo = db.Column(db.String(100))
    internet = db.Column(db.String(100), nullable = True)
    fixo = db.Column(db.String(100), nullable = True)
    movel = db.Column(db.String(100), nullable = True)
    linhas_moveis = db.Column(db.String(100), nullable = True)

    fatura = db.Column(db.LargeBinary, nullable = True)

    data_cadastro = db.Column(db.String(100))

if __name__ == '__main__':
    db.create_all()