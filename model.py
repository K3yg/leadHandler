from flask_sqlalchemy import Pagination
from config import *


class Pessoa_Anexo(db.Model):
    __tablename__ = "pessoa_anexo"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    telefone = 
    email =
    termos de uso
    fatura


class Pessoa_Preencher(db.Model):
    '''
    PF/PJ
    LOCALIDADE
    INTERNET/MOVEL/Fixo 
    operadora
    VALOR QUE Paga  
    pERGUNTAS QUE ELE TEM QUE SELECIONAR(AUMENTAR PLANO ETC...) QUE VAI SER DIFERENTE PARA CADA UM QUE ELE ESCOLHER DE (INTERNET/MOVEL/Fixo)
    DISPONIBILIDADE
    nome = db.Column(db.String(100))
    telefone = 
    email =
    termos de uso
    '''

