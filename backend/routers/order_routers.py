from fastapi import APIRouter
from schemas.transacao import TransacaoSchema
from database.db import Session
from models.model import Transacao



order_router = APIRouter(prefix="/order", tags= ["order"]) 




#-------------------Rotas---------------------

#------------Get
@order_router.get("/")
async def home():
    return {"Menssagem": "Bem-vindo à API de Controle Financeiro!"}


@order_router.get("/transações")
def listar_trasaçoes():
    with Session() as session:
        transacoes = session.query(Transacao).all()
        return transacoes
    


@order_router.get("/saldo")
def saldo():
    with Session() as session:
        transacoes = session.query(Transacao).all()

        entradas = sum(t.valor for t in transacoes if t.tipo == "entrada")
        saidas = sum(t.valor for t in transacoes if t.tipo == "saida")

        saldo_total = entradas - saidas

        return {
            "entradas": entradas,
            "saidas": saidas,
            "saldo_total": saldo_total
        }




#------------Post
@order_router.post("/transações")
def transaçoes(dados: TransacaoSchema):
    with Session() as session:
        nova_trasacao = Transacao(descricao= dados.descricao, valor= dados.valor, tipo=dados.tipo, categoria= dados.categoria, )
        session.add(nova_trasacao)
        session.commit()
    
        return nova_trasacao