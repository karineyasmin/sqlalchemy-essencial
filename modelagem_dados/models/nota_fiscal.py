from sqlalchemy import (
    Column,
    DateTime,
    BigInteger,
    Integer,
    DECIMAL,
    String,
    ForeignKey,
    Table,
    TIMESTAMP,
)

from models.model_base import ModelBase
from sqlalchemy.orm import relationship


# Nota fiscal pode ter vários lotes
lotes_nota_fiscal = Table(
    "lotes_nota_fiscal",
    ModelBase.metadata,
    Column("id_nota_fiscal", Integer, ForeignKey("notas_fiscais.id")),
    Column("id_lote", Integer, ForeignKey("lotes.id")),
)


class NotaFiscal(ModelBase):
    __tablename__: str = "notas_fiscais"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    data_criacao = Column(TIMESTAMP)
    valor = Column(DECIMAL(10, 2), nullable=False)
    numero_serie = Column(String(45), unique=False, nullable=False)
    descricao = Column(String(200), nullable=False)
    id_revendedor = Column(Integer, ForeignKey("revendedores.id"))
    revendedor = relationship("Revendedor", lazy="joined")

    # Uma nota fiscal pode ter vários lotes e um lote está ligado a uma nota fiscal
    lotes = relationship(
        "Lote", secondary=lotes_nota_fiscal, backref="lote", lazy="dynamic"
    )

    def __repr__(self):
        return f"<Nota Fiscal: {self.numero_serie}>"
