from typing import List
from app.models.models import Item

# Função: Gera os dados da tabela a partir de uma lista de itens
def generate_graph_from_items(items: List[Item]):
    # Convertendo os itens para um DataFrame-like
    data = [
        {
            "nome": item.nome,
            "matricula": item.matricula,
            "departamento": item.departamento,
            "item": item.item_nome
        }
        for item in items
    ]
    
    # Criando a estrutura de JSON
    result = {
        "data": data
    }
    
    return result  # Retorna as colunas e os dados como JSON
