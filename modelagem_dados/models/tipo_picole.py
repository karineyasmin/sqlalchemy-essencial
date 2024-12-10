from .model_base import ModelBase
from datetime import datetime
from sqlalchemy import BigInteger, String, Column, DateTime


class TipoPicole(ModelBase):
    __tablename__: str = "tipos_picole"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    data_criacao = Column(DateTime, default=datetime.now, index=True)
    nome = Column(String(45), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"<Tipo Picolé: {self.nome}>"
