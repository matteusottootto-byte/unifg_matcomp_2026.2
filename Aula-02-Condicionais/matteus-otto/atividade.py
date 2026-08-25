# --- TAREFA 1 ---
A = {"Notebook", "Projetor", "Impressora"}
B = {"Centro", "Boa Viagem", "Casa Amarela"}

produto_cartesiano = {(a, b) for a in A for b in B}
relacao_atendimento = {("Notebook", "Centro"), ("Projetor", "Boa Viagem"), ("Impressora", "Casa Amarela")}

print("A x B:", produto_cartesiano)
print("Relação:", relacao_atendimento)


# --- TAREFA 2 ---
f_ativo_sec = {
    "TOMB-101": "Educação",
    "TOMB-102": "Saúde",
    "TOMB-103": "Finanças"
}

def f(ativo):
    return f_ativo_sec.get(ativo)

im_f = set(f_ativo_sec.values())
e_injetora = len(f_ativo_sec) == len(im_f)

print("Imagem Im(f):", im_f)
print("É injetora?:", e_injetora)


# --- TAREFA 3 ---
f_tomb = {
    "Notebook": "TOMB-101",
    "Projetor": "TOMB-102",
    "Impressora": "TOMB-103"
}

f_inv = {v: k for k, v in f_tomb.items()}
e_bijetora = len(f_tomb) == len(set(f_tomb.values()))

print("Função Inversa (f⁻¹):", f_inv)
print("É bijetora?:", e_bijetora)


# --- TAREFA 4 ---
def g(secretaria):
    resp = {"Educação": "Prof. Carlos", "Saúde": "Dra. Ana", "Finanças": "Sr. Roberto"}
    return resp.get(secretaria, "Não encontrada")

def pipeline(tombamento):
    ativo = f_inv.get(tombamento)
    if not ativo:
        return f"Erro: Tombamento {tombamento} inexistente!"
    
    sec = f(tombamento)
    return f"Tombamento: {tombamento} | Ativo: {ativo} | Resp: {g(sec)}"

print(pipeline("TOMB-901"))
print(pipeline("TOMB-101"))