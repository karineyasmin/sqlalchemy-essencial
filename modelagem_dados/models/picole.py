from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    DECIMAL,
    ForeignKey,
    Integer,
    Table,
    TIMESTAMP,
)

from models import tipo_embalagem
from .model_base import ModelBase
from sqlalchemy.orm import relationship
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo

# Picolé pode ter vários ingredientes
ingredientes_picole = Table(
    "ingredientes_picole",
    ModelBase.metadata,
    Column("id_picole", Integer, ForeignKey("picoles.id")),
    Column("id_ingrediente", Integer, ForeignKey("ingredientes.id")),
)

# Picolé pode ter vários conservantes
conservantes_picole = Table(
    "conservantes_picole",
    ModelBase.metadata,
    Column("id_picole", Integer, ForeignKey("picoles.id")),
    Column("id_conservante", Integer, ForeignKey("conservantes.id")),
)


# Picolé pode ter vários aditivos nutritivos
aditivos_nutritivos_picole = Table(
    "aditivos_nutritivos_picole",
    ModelBase.metadata,
    Column("id_picole", Integer, ForeignKey("picoles.id")),
    Column("id_aditivo_nutritivo", Integer, ForeignKey("aditivos_nutritivos.id")),
)


class Picole(ModelBase):
    __tablename__: str = "picoles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_criacao = Column(TIMESTAMP)
    preco = Column(DECIMAL(10, 2), nullable=False)
    id_sabor = Column(Integer, ForeignKey("sabores.id"))
    sabor = relationship("Sabor", lazy="joined")
    id_tipo_embalagem = Column(Integer, ForeignKey("tipos_embalagem.id"))
    tipo_embalagem = relationship("TipoEmbalagem", lazy="joined")
    id_tipo_picole = Column(Integer, ForeignKey("tipos_picole.id"))
    tipo_picole = relationship("TipoPicole", lazy="joined")

    #  Um picole pode ter varios ingredientes
    ingredientes = relationship(
        "Ingrediente",
        secondary=ingredientes_picole,
        backref="ingrediente",
        lazy="joined",
    )

    # Um picole pode ter varios ou nenhum consevantes
    conservantes = relationship(
        "Conservante",
        secondary=conservantes_picole,
        backref="conservante",
        lazy="joined",
    )

    # Um picolé pode ter varios ou nenhum aditivos nutritivos
    aditivos_nutritivos = relationship(
        "AditivoNutritivo",
        secondary=aditivos_nutritivos_picole,
        backref="aditivo_nutritivo",
        lazy="joined",
    )

    def __repr__(self) -> str:
        return f"<Picolé: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>"
