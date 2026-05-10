import os
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq

# Usamos el nombre de la variable que pusiste en la plataforma
api_key = os.environ.get("GROQ_API_KEY")

# Definimos el modelo
llm = ChatGroq(
    model_name="llama3-70b-8192",
    groq_api_key=api_key
)

# Definimos al Agente
consultor = Agent(
    role='Consultor de Automatización',
    goal='Optimizar procesos para Inmobiliaria Bajakey',
    backstory='Experto en n8n y Make en Tijuana.',
    llm=llm, # <--- Esto es lo que causaba el ValidationError
    verbose=True
)

# Definimos la Tarea
tarea = Task(
    description='Pasos para conectar WhatsApp con n8n.',
    expected_output='Guía técnica de 5 pasos.',
    agent=consultor
)

# Creamos la Crew
def run():
    colmena = Crew(
        agents=[consultor],
        tasks=[tarea],
        verbose=True
    )
    return colmena.kickoff()

if __name__ == "__main__":
    run()
