from sqlalchemy import Column, DateTime, BigInteger, Integer, ForeignKey
from datetime import datetime
from .model_base import ModelBase
from .tipo_picole import TipoPicole
from sqlalchemy.orm import relationship


class Lote(ModelBase):
    __tablename__: str = "lotes"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    data_criacao = Column(DateTime, default=datetime.now, index=True)
    id_tipo_picole = Column(Integer, ForeignKey("tipos_picole.id"))  # tabela.campo
    tipo_picole = relationship("TipoPicole", lazy="joined")
    quantidade = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<Lote: {self.id}>"
