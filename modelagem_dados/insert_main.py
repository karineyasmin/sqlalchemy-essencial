from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo


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


if __name__ == "__main__":
    insert_aditivo_nutritivo()
