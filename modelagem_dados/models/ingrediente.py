from .model_base import ModelBase
from sqlalchemy import Column, DateTime, BigInteger, String
from datetime import datetime


class Ingrediente(ModelBase):
    __tablename__: str = "ingredientes"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    data_criacao = Column(DateTime, index=True, default=datetime.now)
    nome = Column(String(45), nullable=False, unique=True)

    def __repr__(self):
        return f"<Ingrediente: {self.nome}>"
