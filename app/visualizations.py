from typing import List
from app.models.models import Items

def generate_graph(items: List[Items]):
    data = [
        {
            "nome": item.nome,
            "matricula": item.matricula,
            "departamento": item.departamento,
            "item": item.item_nome
        }
        for item in items
    ]
    
    result = {
        "data": data
    }
    
    return result
