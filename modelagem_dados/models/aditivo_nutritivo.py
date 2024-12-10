from sqlalchemy import Column, DateTime, BigInteger, String
from datetime import datetime
from .model_base import ModelBase


class AditivoNutritivo(ModelBase):
    __tablename__: str = "aditivos_nutritivos"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    data_criacao = Column(DateTime, default=datetime.now, index=True)
    nome = Column(String(45), unique=True, nullable=False)
    formula_quimica = Column(String(45), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"<Aditivo Nutritivo: {self.nome}>"
