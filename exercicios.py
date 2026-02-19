# --- EXERCÍCIO DE REDES: UNIDADE 1.2 ---

# 1. Defina os dispositivos da rede (IPs)
dispositivos = ["192.168.0.10", "192.168.0.11", "192.168.0.12", "192.168.0.13"]

# 2. Defina o pacote (Endereço de destino e a mensagem)
pacote_destino = "192.168.0.11"
mensagem = "Olá, mundo das redes!"

print(f"--- Iniciando Difusão do Pacote para: {pacote_destino} ---")

# TAREFA 1: Implemente o loop de difusão (Broadcast)
# Para cada ip em dispositivos:
#   Se ip for igual ao pacote_destino: print "[V] Processado por", ip
#   Senão: print "[X] Descartado por", ip

# --- ESPAÇO PARA O SEU CÓDIGO (TAREFA 1) ---
for i in dispositivos:
  if i == pacote_destino:
    print("[V] Processador por: ", i)
  else:
    print("[X] Descartado por", i)


# TAREFA 2: Cálculo de Confiabilidade (QoS)
# Dados: O servidor operou 7200 horas (MTTF) e ficou parado 48 horas para reparo (MTTR).
mttf = 7200
mttr = 48

# Implemente a fórmula de disponibilidade aqui:
disponibilidade = mttf / (mttf+mttr) * 100

print(f"\nDisponibilidade da Rede: {disponibilidade:.2f}%")
