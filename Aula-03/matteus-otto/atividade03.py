from collections import deque

class CruzamentoSemaforico:
    def __init__(self):
        self.fila_veiculos = deque()
        self.fila_pedestres = deque()
        self.fila_ambulancias = deque()
        self.cancela_ferrea_ativa = False

    def adicionar_veiculo(self, veiculo_id):
        self.fila_veiculos.append(veiculo_id)

    def adicionar_pedestre(self, pedestre_id):
        self.fila_pedestres.append(pedestre_id)

    def adicionar_ambulancia(self, ambulancia_id):
        self.fila_ambulancias.append(ambulancia_id)

    def definir_estado_cancela_ferrea(self, ativa):
        self.cancela_ferrea_ativa = ativa

    def processar_proximo_evento(self):
        if self.cancela_ferrea_ativa:
            return "BLOQUEIO TOTAL: Trem passando. Cancela ferrea fechada."

        if self.fila_ambulancias:
            ambulancia = self.fila_ambulancias.popleft()
            return f"PRIORIDADE EMERGENCIA: Ambulancia {ambulancia} liberada."

        if self.fila_pedestres:
            pedestre = self.fila_pedestres.popleft()
            return f"PREFERENCIA PEDESTRE: Pedestre {pedestre} liberado para atravessar."

        if self.fila_veiculos:
            veiculo = self.fila_veiculos.popleft()
            return f"FLUXO ORDINARIO: Veiculo {veiculo} liberado."

        return "ESTADO OCIOSO: Nenhum veiculo ou pedestre aguardando."


cruzamento = CruzamentoSemaforico()

cruzamento.adicionar_veiculo("Carro A")
cruzamento.adicionar_veiculo("Carro B")
cruzamento.adicionar_pedestre("Pedestre 1")
cruzamento.adicionar_ambulancia("Ambulancia 01")

print(cruzamento.processar_proximo_evento())

cruzamento.definir_estado_cancela_ferrea(True)
print(cruzamento.processar_proximo_evento())

cruzamento.definir_estado_cancela_ferrea(False)
print(cruzamento.processar_proximo_evento())
print(cruzamento.processar_proximo_evento())
print(cruzamento.processar_proximo_evento())