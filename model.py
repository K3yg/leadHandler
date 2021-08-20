from config import *

class PessoaFisica(db.Model):
    __tablename__ = 'pessoa_fisica'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(100))

    cidade = db.Column(db.String(100))
    analise_sobre = db.Column(db.String(100))
    desejo = db.Column(db.String(500))
    operadora = db.Column(db.String(100))

    fatura = db.Column(db.LargeBinary)

    aceitar_termos = db.Column(db.String(100))


class PessoaJuridica(db.Model):
    __tablename__ = 'pessoa_juridica'

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100))
    nome_empresa = db.Column(db.String(100))
    setor = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(100))

    cidade = db.Column(db.String(100))
    analise_sobre = db.Column(db.String(100))
    desejo = db.Column(db.String(500))
    operadora = db.Column(db.String(100))

    aceitar_termos = db.Column(db.String(100))




if __name__ == '__main__':
    if os.path.exists(arquivobd):
        print('Arquivo já existente!')
    else:
        db.create_all()



    
