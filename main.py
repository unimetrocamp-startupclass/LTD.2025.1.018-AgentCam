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
    temperature= 0.1
)


cam = 'http://72.43.190.171:81/mjpg/video.mjpg?size=1'
video_tool = VideoTool(max_frames=50)

agentcam = Agent(
    role='Agente de segurança experiente',
    goal='Avalia a filmagem da camera de segurança.',
    backstory=(
        'Agente com anos de experiencia em segurança patrimonial.'
        'Sempre avalia com expertiese as filmagens, contando quantas pessoas'
        'foram identificadas.'
    ),
    tools=[video_tool],
    llm=ds_llm,
    auto_invoke=True
)

agent_task = Task(
    description=(
        'Irá avaliar as filmagens e contar quantas pessoas apareceram.'
        'Deve fazer analise cautelosa dos videos e fazer a contagem das pessoas.'
        'Deve obrigatóriamente usar a ferramenta video_tool'
        'para monitorar a camera do URL: {cam}'
        #'para monitorar o video salvo em: ./saida.mp4'
    ),
    expected_output='A contagem de quantas pessoas apareceram',
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