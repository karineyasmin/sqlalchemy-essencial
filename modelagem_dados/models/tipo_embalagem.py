from sqlalchemy import Column, DateTime, String, Integer
from datetime import datetime
from .model_base import ModelBase


class TipoEmbalagem(ModelBase):
    __tablename__: str = "tipos_embalagem"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_criacao = Column(DateTime, default=datetime.now, index=True)
    nome = Column(String(45), nullable=False)

    def __repr__(self) -> str:
        return f"<Tipo Embalagem: {self.nome}>"
