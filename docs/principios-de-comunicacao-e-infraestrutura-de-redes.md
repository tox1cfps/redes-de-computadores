# RELATÓRIO TÉCNICO: PRINCÍPIOS DE COMUNICAÇÃO E INFRAESTRUTURA DE REDES

**Referência:** Baseado em NUNES, S. E. *Redes de Computadores*. Londrina: EDE SA, 2017.

---

## 1. RESUMO

Este relatório apresenta uma análise estruturada dos princípios fundamentais de comunicação de dados, focando na infraestrutura necessária para a conectividade corporativa.

O documento diferencia **intranet** e **extranet**, avalia métricas de desempenho (*vazão, latência e jitter*) e discorre sobre tecnologias de link e hardware.

Adicionalmente, apresenta ferramentas computacionais em **Python** para o cálculo de disponibilidade e métricas de falhas, visando auxiliar a administração proativa da rede.

---

## 2. INTRODUÇÃO

As redes de computadores são sistemas complexos que exigem planejamento rigoroso para garantir a continuidade das aplicações.

O papel do administrador de redes é fundamental para gerir recursos compartilhados, como impressoras e repositórios de arquivos, otimizando processos e garantindo a **Qualidade de Serviço (QoS)**.

---

## 3. DESENVOLVIMENTO TEÓRICO

### 3.1 Ambientes de Acesso: Intranet e Extranet

- **Intranet:**  
  Rede privada de uso interno restrito a uma organização, utilizando protocolos de Internet para compartilhar recursos entre membros.

- **Extranet:**  
  Extensão da rede privada que permite acesso externo controlado a usuários autorizados.

---

### 3.2 Métricas de Desempenho e Confiabilidade

A eficácia da rede é medida por indicadores técnicos:

- **Vazão (Throughput):** Volume de dados transferidos.
- **Latência:** Tempo de tráfego entre dispositivos.
- **Jitter:** Variação irregular no tempo de entrega dos pacotes.
- **Confiabilidade:** Frequência de falhas e tempo de recuperação do sistema.

---

### 3.3 Hardware Básico de Rede

- **Placa de Rede (NIC):** Interface de entrada/saída responsável pelo endereçamento lógico.
- **Modem (Transceptor):** Realiza a modulação e demodulação para adequação ao meio físico.
- **Hub:** Repetidor que replica mensagens para todas as portas; seu uso excessivo (*cascateamento*) degrada a rede.

---

## 4. FERRAMENTAS DE CÁLCULO E SIMULAÇÃO (CÓDIGO PYTHON)

Para auxiliar na gerência de infraestrutura, foram desenvolvidas funções em Python baseadas nos conceitos de Nunes (2017).

### 4.1 O Código

```python
# --- Calculadora de Métricas de Redes de Computadores ---

def calcular_disponibilidade(mttf, mttr):
    """Calcula a disponibilidade (D) da rede."""
    disponibilidade = mttf / (mttf + mttr)
    return disponibilidade * 100

def calcular_links_malha(n):
    """Calcula o número de links para topologia em malha."""
    links = (n * (n - 1)) / 2
    return int(links)

def calcular_mtbf_mttr(tempo_total_operacao, tempo_total_parada, num_falhas):
    """Calcula o MTBF e o MTTR."""
    mtbf = (tempo_total_operacao - tempo_total_parada) / num_falhas
    mttr = tempo_total_parada / num_falhas
    return mtbf, mttr

# Exemplo Prático:
# 8000h de MTTF e 36h de MTTR
disp = calcular_disponibilidade(8000, 36)
print(f"Disponibilidade: {disp:.2f}%")