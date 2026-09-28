equipamentos = [
    {"id": "Respirador 1", "setor": "UTI", "dias": 45, "revisado": True},
    {"id": "Respirador 2", "setor": "UTI", "dias": 210, "revisado": True},
    {"id": "Bomba 1", "setor": "Triagem", "dias": 30, "revisado": False},
    {"id": "Monitor 1", "setor": "UTI", "dias": 100, "revisado": True},
]
print(all(equipamento["revisado"] for equipamento in equipamentos))
print(any(equipamento["revisado"] for equipamento in equipamentos))
equipamentos_com_problema = [eq["id"] for eq in equipamentos if not eq["revisado"]]
print(equipamentos_com_problema)