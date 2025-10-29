from pydantic import BaseModel
from datetime import date
from typing import Optional

class TransacaoSchema(BaseModel):
    descricao: str
    valor: float
    tipo: str
    categoria: str
    data: Optional[date] = date.today()
