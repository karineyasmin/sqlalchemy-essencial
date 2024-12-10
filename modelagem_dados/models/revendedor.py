from .model_base import ModelBase
from sqlalchemy import Column, DateTime, BigInteger, String
from datetime import datetime


class Revendedor(ModelBase):
    __tablename__: str = "revendedores"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    data_criacao = Column(DateTime, index=True, default=datetime.now)
    cnpj = Column(String(45), nullable=False, unique=True)
    contato = Column(String(100), nullable=False, unique=True)
    razao_social = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Revendedor: {self.cnpj}>"
