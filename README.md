# LTD.2025.1.018-AgentCam

# AgentCam

O *AgentCam* é um sistema de monitoramento inteligente que utiliza *Python* e a biblioteca *OpenCV* para capturar vídeos de câmeras públicas, analisar detecções de pessoas e preparar essas informações para avaliação automatizada por agentes de IA.

## Objetivo

Substituir o trabalho manual de vigilantes humanos utilizando agentes de inteligência artificial capazes de analisar câmeras de segurança e avaliar eventos com precisão, agilidade e autonomia.

## Funcionalidades atuais

- Captura de vídeos de câmeras públicas em tempo real
- Armazenamento dos vídeos em takes organizados
- Detecção de pessoas nos vídeos usando OpenCV
- Avaliação inicial das câmeras com base no movimento de pessoas

## Próximos passos

- Implementar sistema de monitoramento em blocos de 5 minutos
- Enviar takes para agentes analisarem os frames dos vídeos
- Integração com o *CrewAI* para orquestração entre agentes
- Criação de uma pipeline autônoma onde os agentes substituem a figura do vigilante humano

## Tecnologias utilizadas

- Python 3.12
- OpenCV
- Framework CrewAI (em desenvolvimento)
- Outros pacotes listados em requirements.txt

## Como executar

> Ainda em desenvolvimento. No momento, é necessário apenas instalar as dependências e executar o script principal.

### Requisitos

- Python 3.12 instalado

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/agentcam.git

# Acesse a pasta do projeto
cd agentcam

# Instale as dependências
pip install -r requirements.txt

# Execute o sistema
python nome_do_arquivo_principal.py
