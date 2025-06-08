import os
from crewai import Agent, Task, Crew, LLM
from custom_tools import VideoTool
from dotenv import load_dotenv

load_dotenv()


os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')


ds_llm = LLM(
    model = 'openrouter/deepseek/deepseek-chat',
    base_url = 'https://openrouter.ai/api/v1',
    api_key = os.getenv('OPENAI_API_KEY'),
    temperature= 0
)


cam = 'http://108.30.103.58:8082/mjpg/video.mjpg?size=1'
cam = 0
video_tool = VideoTool(max_frames=50)

agentcam = Agent(
    role='Agente de segurança experiente',
    goal='Avalia a filmagem da camera de segurança.',
    backstory=(
        'Agente com anos de experiencia em segurança patrimonial.'
        # 'Sempre avalia com expertiese as filmagens, contando quantas pessoas'
        #1. 'foram identificadas.'
        #2. 'Descreve exatamente tudo que esta vendo na filmagem'
        'Descreve os gestos que o usuaria esta fazendo durante o video'
    ),
    tools=[video_tool],
    llm=ds_llm,
    auto_invoke=True
)

agent_task = Task(
    description=(
        # 'Irá avaliar as filmagens e contar quantas pessoas apareceram.'
        # 'Deve fazer analise cautelosa dos videos e fazer a contagem das pessoas.'
        'Deve obrigatóriamente usar a ferramenta video_tool'
        # 'para monitorar a camera do URL: {cam}'
        'Deve descrever exatamente o que ve na filmagem, objetos, cores das paredes e etc.'
        'Deve descrever quais os gestos que o usuario do video faz'
        'e qual sua expressão facial.'
        #'Deve descrever detalhadamente a aparencia das pessoas que aparecem na filmagem.'
        #'para monitorar o video salvo em: ./saida.mp4'
    ),
    expected_output= ('Descrever exatamente o que esta vendo na filmagem e a caracatristica do usuario.'),
    #'A contagem de quantas pessoas apareceram e suas caracteristicas fisicas.',)
    agent=agentcam,
    #context=[cam]
)

crew = Crew(
    agents=[agentcam],
    tasks=[agent_task],
    verbose=True
)

result = crew.kickoff(inputs={
    'cam': cam
})
print('\n===== RESULTADO =====\n')
print(result)