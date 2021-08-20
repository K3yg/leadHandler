from sqlalchemy.sql.elements import Null
from config import *

class PessoaFisica(db.Model):
    __tablename__ = 'pessoa_fisica'

    def __init__(self, nome, telefone, cidade, analise_sobre, desejo, operadora, aceitar_termos):
        self.nome = nome
        self.telefone = telefone
        self.cidade = cidade
        self.analise_sobre = analise_sobre
        self.desejo = desejo
        self.operadora = operadora
        self.aceitar_termos = aceitar_termos

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(100))

    cidade = db.Column(db.String(100))
    analise_sobre = db.Column(db.String(100))
    desejo = db.Column(db.String(500))
    operadora = db.Column(db.String(100))

    #fatura = db.Column(db.LargeBinary, nullable = True)

    aceitar_termos = db.Column(db.String(100), default = 'Sim')


class PessoaJuridica(db.Model):
    __tablename__ = 'pessoa_juridica'

    def __init__(self, nome, nome_empresa, setor, email,telefone, cidade, analise_sobre, desejo, operadora, aceitar_termos):
        self.nome = nome
        self.nome_empresa = nome_empresa
        self.setor = setor
        self.email = email
        self.telefone = telefone
        self.cidade = cidade
        self.analise_sobre = analise_sobre
        self.desejo = desejo
        self.operadora = operadora
        self.aceitar_termos = aceitar_termos


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

    #fatura = db.Column(db.LargeBinary, nullable = True)

    aceitar_termos = db.Column(db.String(100), default = 'Sim')




if __name__ == '__main__':
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    else:
        db.create_all()
        x = PessoaJuridica('Jonas', 'Fey', 'Comercial', 'jonas@gmail.com', '11 99999-9999', 'São Paulo', 'Internet', 'Aumentar', 'Vivo', 'Sim')
        y = PessoaFisica('Claudio', '11 99999-9999', 'Rio de Janeiro', 'Móvel', 'Aumentar dados', 'Claro', 'Sim')

        db.session.add(x)
        db.session.add(y)
        db.session.commit()



    
