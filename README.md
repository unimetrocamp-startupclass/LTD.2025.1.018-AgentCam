# 👁️ AgentCam – Monitoramento Inteligente com IA

**AgentCam** é um sistema de monitoramento de câmeras com suporte a múltiplas fontes e integração com inteligência artificial, utilizando OpenCV para reconhecimento em tempo real.

---

## 📌 O que é o AgentCam?

O AgentCam é um projeto modular e adaptável que visa integrar visão computacional com agentes inteligentes, permitindo reações automáticas com base em eventos captados por vídeo.

- Suporte a múltiplas fontes de vídeo (IP, USB etc.)
- Reconhecimento de pessoas com OpenCV
- Projetado para funcionar com agentes de IA
- Flexível e personalizável

---

## 🎯 Objetivo do Projeto

> Dar “olhos” e “interpretação” em tempo real para agentes inteligentes.

- Criar um sistema autônomo de vigilância com base em IA
- Integrar captura de vídeo com tomada de decisão automatizada
- Explorar diferentes arquiteturas de captura e análise de imagens

---

## 🧪 Abordagens em Estudo

### ✅ Opção 1 – Análise em Tempo Real
- Agentes analisam os frames diretamente via OpenCV
- Resposta imediata a eventos
- Maior complexidade de integração

### ⏳ Opção 2 – Processamento por Lotes
- Vídeos capturados e enviados para análise posterior
- Implementação mais simples
- Introduz delay nas reações dos agentes

## 🛠️ Tecnologias utilizadas

- Python 3.12
- OpenCV
- Framework CrewAI
- Outros pacotes listados em requirements.txt

## Como executar

> Instalar as dependências e executar o script principal.

### Requisitos

- Python 3.12 instalado

- Chave API (OpenAI ou outro provider).

### Instalação

```bash
# Clone o repositório
git clone https://github.com/unimetrocamp-startupclass/LTD.2025.1.018-AgentCam

# Acesse a pasta do projeto
cd LTD.2025.1.018-AgentCam

# Instale as dependências
pip install -r requirements.txt

# Execute o sistema
python main.py