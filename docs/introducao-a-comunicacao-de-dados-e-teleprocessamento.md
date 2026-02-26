# RELATÓRIO TÉCNICO: INTRODUÇÃO À COMUNICAÇÃO DE DADOS E AO TELEPROCESSAMENTO

**Autor:** Eduardo Furlan Miranda  
**Data:** 1 de fevereiro de 2026  
**Referência:** Baseado em NUNES, S. E. *Redes de Computadores*. Londrina: EDE SA, 2017.

---

## 1. RESUMO

Este relatório apresenta uma síntese dos fundamentos da comunicação de dados, abordando sua evolução histórica desde a década de 1960 até os dias atuais.

O documento detalha a distinção técnica entre **sinais analógicos e digitais**, os **modos de transmissão** (*simplex, half-duplex e full-duplex*) e as características dos **meios de transmissão** guiados e não guiados.

Conclui-se que o entendimento desses pilares é essencial para o planejamento de infraestruturas que suportem serviços modernos como *streaming*, VoIP e e-commerce.

---

## 2. INTRODUÇÃO

A comunicação de dados evoluiu de pesquisas militares e acadêmicas para se tornar a espinha dorsal da sociedade digital contemporânea.

O marco inicial remete aos estudos de comutação de pacotes de Leonard Kleinrock e Paul Baran na década de 1960, culminando na criação da **Arpanet** em 1967.

Compreender os métodos de acesso e os equipamentos de rede permite que profissionais de TI garantam a disponibilidade e a qualidade dos serviços prestados.

---

## 3. DESENVOLVIMENTO

### 3.1 Evolução Histórica das Redes

- **Décadas de 1960 e 1970:**  
  Surgimento da Arpanet e do primeiro protocolo de comunicação, o **NCP** (1972). Desenvolvimento da ALOHAnet (Havaí) utilizando micro-ondas.

- **Década de 1980:**  
  Adoção oficial do protocolo **TCP/IP** em 1º de janeiro de 1983 e criação do sistema de nomes de domínios (**DNS**).

- **Década de 1990:**  
  Invenção da **World Wide Web (WWW)** no CERN, impulsionando o hipertexto, navegadores e o crescimento de empresas como Amazon e Google.

---

### 3.2 Sinais e Modos de Transmissão

A comunicação utiliza dois tipos principais de sinais:

- **Analógico:**  
  Ondas senoidais contínuas definidas por amplitude, frequência e fase (ex.: voz humana).

- **Digital:**  
  Valores discretos (0 e 1). Oferece maior imunidade a ruídos e facilidade de detecção de erros e processamento por software.

Quanto ao sentido das trocas de mensagens, os modos são classificados em:

- **Simplex:** Comunicação unidirecional (ex.: impressora).
- **Half-duplex:** Bidirecional, mas não simultânea (ex.: comunicação via hub).
- **Full-duplex:** Bidirecional e simultânea (ex.: comunicação via switch).

---

### 3.3 Meios de Transmissão

Os dados podem ser transportados por meios físicos distintos:

- **Guiados (Com fios):**  
  Incluem o par trançado (categorias CAT5e a CAT7), cabo coaxial (10Base2 e 10Base5) e a **fibra óptica**, que utiliza luz (lasers/LEDs) e atinge velocidades de Terabits por segundo.

- **Não Guiados (Sem fios):**  
  Utilizam ondas de rádio, micro-ondas (que exigem visada direta) e satélites (órbitas LEO, MEO e HEO).

---

## 4. CONCLUSÃO

A escolha do meio de transmissão e dos equipamentos (hub, switch ou roteador) deve considerar fatores como geografia, distância e viabilidade financeira.

Enquanto a fibra óptica oferece alta imunidade a interferências e grandes larguras de banda, os meios não guiados são vitais para conectividade onde a infraestrutura física é inviável.

O domínio desses conceitos fundamentais é o ponto de partida para a implementação de redes resilientes e eficientes.

---

## 5. REFERÊNCIAS BIBLIOGRÁFICAS

NUNES, Sergio Eduardo. **Redes de computadores**. Londrina: Editora e Distribuidora Educacional S.A., 2017. ISBN 978-85-522-0194-6.