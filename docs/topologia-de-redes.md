# RELATÓRIO TÉCNICO: TOPOLOGIAS E EQUIPAMENTOS DE INFRAESTRUTURA DE REDES


**Data:** 1 de fevereiro de 2026  
**Referência:** Baseado em NUNES, S. E. *Redes de Computadores*. Londrina: EDE SA, 2017.

---

## 1. RESUMO

Este relatório analisa os componentes essenciais e as formas de organização das redes de computadores. O estudo abrange a identificação de hardwares críticos como **roteadores**, **switches**, **bridges** e **gateways**, detalhando suas funções lógicas e físicas.

Além disso, descreve as principais topologias de rede — **malha, estrela, barramento, anel e híbrida** — avaliando suas vantagens, desvantagens e aplicações práticas. Por fim, classifica as redes quanto ao seu nível de abrangência geográfica, variando de redes pessoais (**PAN**) a redes mundiais (**WAN**).

---

## 2. INTRODUÇÃO

As redes de computadores constituem uma infraestrutura imperceptível ao usuário final, mas essencial para a comunicação global independente da localização geográfica.

Para o correto planejamento de uma rede, é necessário identificar os equipamentos de hardware adequados e definir o mapa da rede (topologia) que melhor atenda às necessidades de desempenho e redundância do sistema.

---

## 3. DESENVOLVIMENTO

### 3.1 Equipamentos de Infraestrutura

Os dispositivos de rede possuem inteligência própria para gerenciar o tráfego de dados:

- **Roteador:**  
  Contém microprocessador e sistema operacional. Analisa o endereçamento lógico (**TCP/IP**) e mantém tabelas de rotas atualizadas via protocolos como **ICMP, ARP e RARP**.

- **Switch:**  
  Utilizado para interconectar múltiplos dispositivos. Ao contrário do hub, o switch lê o endereço de destino no cabeçalho e envia a mensagem apenas para a porta correta, possuindo domínios de colisão separados em cada interface.

- **Bridge (Ponte):**  
  Conecta duas redes distintas (LANs), possuindo funcionamento similar ao switch, mas com configuração geralmente mais simples.

- **Gateway:**  
  Conhecido como **"borda de rede"**, é o ponto de saída para a Internet. Pode desempenhar funções de **proxy** (controle de acesso) e **firewall** (segurança e bloqueio de portas).

---

### 3.2 Topologias Físicas

A topologia define a representação geométrica dos links entre os dispositivos:

- **Malha (Mesh):**  
  Possui links dedicados e redundantes entre todos os nodos.  
  O número de links é calculado pela fórmula:
