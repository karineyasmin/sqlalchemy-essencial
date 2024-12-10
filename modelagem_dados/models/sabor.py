from sqlalchemy import Column, DateTime, BigInteger, String
from datetime import datetime
from .model_base import ModelBase


class Sabor(ModelBase):
    __tablename__: str = "sabores"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    data_criacao = Column(DateTime, default=datetime.now, index=True)
    nome = Column(String(45), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"<Sabor: {self.nome}>"
