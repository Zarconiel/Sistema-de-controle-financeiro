from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from datetime import date
from uuid import uuid4
from database import Base




# 3️⃣ Cria a tabela Transacao
class Transacao(Base):
    __tablename__ = "transacoes"  # nome da tabela no banco

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    descricao = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)         # Ex: 'entrada' ou 'saída'
    categoria = Column(String, nullable=False)    # Ex: 'alimentação', 'lazer'
    data = Column(Date, default=date.today)

    def __init__(self, descricao, valor, tipo, categoria):
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo
        self.categoria = categoria

