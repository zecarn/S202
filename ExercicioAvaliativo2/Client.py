from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

class FamilyGraphClient:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # Função para responder: Quem da família é estudante?
    def who_is_student(self):
        query = """
        MATCH (p:Estudante) RETURN p.nome AS name
        """
        with self.driver.session() as session:
            result = session.run(query)
            return [record["name"] for record in result]

    # Função para responder: Fulano de tal é pai de quem?
    def who_is_parent(self, person_name):
        query = """
        MATCH (p:Pessoa {name: $person_name})-[:PAI_DE]->(child)
        RETURN child.name AS child_name
        """
        with self.driver.session() as session:
            result = session.run(query, person_name=person_name)
            return [record["child_name"] for record in result]

    # Função para responder: Quem tem pet?
    def who_have_pet(self):
        query = """
        MATCH (p:Pessoa)<-[:PET_DE]-(d:Pet) RETURN p.nome AS person_name, d.nome AS pet_name
        """
        with self.driver.session() as session:
            result = session.run(query)
            return [{"person_name": record["person_name"], "pet_name": record["pet_name"]} for record in result]


# Exemplo de uso
uri = "neo4j+s://1993cc46.databases.neo4j.io"
user = "neo4j"
password = "zecazeca"

client = FamilyGraphClient(uri, user, password)

def pergunta(valor):
    if valor == 1:
        # Quem da família é estudante?
        students = client.who_is_student()
        return print("Estudantes na família:", students)
    
    elif valor == 2:
        # Fulano de tal é pai de quem?
        parent_name = input("Qual é o nome do filho?")
        children = client.who_is_parent(parent_name)
        return print(f"{parent_name} é pai/mãe de:", children)

    elif valor == 3:
       # Quem tem pet?
        pet_info = client.who_have_pet()
        return 
        for info in pet_info:
            print(f"{info['person_name']} tem um pet chamado {info['pet_name']}") 
    
    elif valor == 0:
        return print("Muito obrigado, até a proxima!")

valor = 1
while valor != 0:
    print("Escolha uma das perguntas disponíveis:")
    print("=====================================================")
    print("[1]- Quem da família é estudante?")
    print("[2]- Fulano de tal é pai de quem?")
    print("[3]- Quem tem pet?")
    print("[0]- Sair")
    print("=====================================================")
    valor = input(int())
    pergunta(valor)
       
client.close()
