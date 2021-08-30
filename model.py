from config import *

class PessoaFisica(db.Model):
    __tablename__ = 'pessoa_fisica'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(100))

    cidade = db.Column(db.String(100))
    operadora = db.Column(db.String(100))
    custo = db.Column(db.Float)
    internet = db.Column(db.String(100), nullable = True)
    fixo = db.Column(db.String(100), nullable = True)
    movel = db.Column(db.String(100), nullable = True)

    #fatura = db.Column(db.LargeBinary, nullable = True)


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
    custo = db.Column(db.Float)
    internet = db.Column(db.String(100), nullable = True)
    fixo = db.Column(db.String(100), nullable = True)
    movel = db.Column(db.String(100), nullable = True)
    #fatura = db.Column(db.LargeBinary, nullable = True)


if __name__ == '__main__':
    db.create_all()
    
    x = PessoaJuridica(nome='Jonas', nome_empresa='Fey', setor='Comercial', email='jonas@gmail.com', telefone='11 99999-9999', cidade='São Paulo', operadora='Vivo', custo=10.00)
    y = PessoaFisica(nome='Cleitin', telefone='11 99999-9999', cidade='São Paulo', operadora='Vivo', custo=220.00)

    db.session.add(x)
    db.session.add(y)
    db.session.commit()



    
