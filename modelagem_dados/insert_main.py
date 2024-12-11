from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor


# 1 Aditivo Nutritivo
def insert_aditivo_nutritivo() -> None:
    print("Cadastrando Aditivo Nutritivo")

    nome: str = input("Informe o nome do Aditivo Nutritivo: ")
    formula_quimica: str = input("Informe a fórmula química: ")

    aditivo_nutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(aditivo_nutritivo)
        session.commit()

    print("Aditivo Nutritivo cadastrado com sucesso")
    print(f"ID: {aditivo_nutritivo.id}")
    print(f"Nome: {aditivo_nutritivo.nome}")
    print(f"Data: {aditivo_nutritivo.data_criacao}")
    print(f"Fórmula Química: {aditivo_nutritivo.formula_quimica}")


# 2 Insert sabor
def insert_sabor() -> None:
    print("Cadastrando Sabor")

    nome: str = input("Informe o nome do sabor: ")

    sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)
        session.commit()

    print("Sabor com sucesso")
    print(f"ID: {sabor.id}")
    print(f"Nome: {sabor.nome}")
    print(f"Data: {sabor.data_criacao}")


# 3 Insert Tipo Embalagem
def insert_tipo_embalagem() -> None:
    print("Cadastrando Tipo de Embalagem")

    nome: str = input("Informe o Tipo de Embalagem: ")

    tipo_embalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(tipo_embalagem)
        session.commit()

    print("Tipo de Embalagem cadastrado com sucesso")
    print(f"ID: {tipo_embalagem.id}")
    print(f"Nome: {tipo_embalagem.nome}")
    print(f"Data: {tipo_embalagem.data_criacao}")


# 4 Insert Tipo Picolé
def insert_tipo_picole() -> None:
    print("Cadastrando Tipo de Picolé")

    nome: str = input("Informe o Tipo do Picolé: ")

    tipo_picole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tipo_picole)
        session.commit()

    print("Tipo do Picolé cadastrado com sucesso")
    print(f"ID: {tipo_picole.id}")
    print(f"Nome: {tipo_picole.nome}")
    print(f"Data: {tipo_picole.data_criacao}")


# 5 Insert Ingredientes
def insert_ingrediente() -> None:
    print("Cadastrando Ingrediente")

    nome: str = input("Informe o Ingrediente: ")

    ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)
        session.commit()

    print("Ingrediente cadastrado com sucesso")
    print(f"ID: {ingrediente.id}")
    print(f"Nome: {ingrediente.nome}")
    print(f"Data: {ingrediente.data_criacao}")


# 6 Insert Conservante
def insert_conservante() -> None:
    print("Cadastrando Conservante")

    nome: str = input("Informe o Conservante: ")
    descricao: str = input("Informe a descrição do Conservante: ")
    conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(conservante)
        session.commit()

    print("Conservante com sucesso")
    print(f"ID: {conservante.id}")
    print(f"Nome: {conservante.nome}")
    print(f"Data: {conservante.data_criacao}")


# 7 Insert Revendedor
def insert_revendedor() -> Revendedor:
    print("Cadastrando Revendedor")

    cnpj: str = input("Informe o CPNJ do Revendedor: ")
    razao_social: str = input("Informe a razão social do revendedor: ")
    contato: str = input("Informe o contato do revendedor: ")

    revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(revendedor)
        session.commit()

    return revendedor


if __name__ == "__main__":
    # insert_aditivo_nutritivo()
    # insert_sabor()
    # insert_tipo_embalagem()
    # insert_tipo_picole()
    # insert_ingrediente()
    # insert_conservante()
    rev = insert_revendedor()
    print(f"ID: {rev.id}")
    print(f"Data: {rev.data_criacao}")
    print(f"CNPJ: {rev.cnpj}")
    print(f"Razão Social: {rev.razao_social}")
    print(f"Contato: {rev.contato}")
