import os
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq

# 1. CONFIGURACIÓN DEL MOTOR (LLM)
# La plataforma leerá la clave desde las variables de entorno que configures
llm = ChatGroq(
    model_name="llama3-70b-8192",
    groq_api_key=os.environ.get("GROQ_API_KEY")
)

# 2. DEFINICIÓN DE AGENTES
# Agente Manager para supervisar y detectar si faltan especialistas
manager = Agent(
    role='Director de Proyectos de Automatización',
    goal='Coordinar la colmena y asegurar que cada tarea tenga al experto adecuado.',
    backstory='Eres un estratega experto en consultoría tecnológica. Si detectas que una tarea requiere un perfil que no está presente, debes reportarlo.',
    llm=llm,
    verbose=True,
    allow_delegation=True
)

# Agente operativo especializado en tu nicho
consultor = Agent(
    role='Especialista en Integraciones n8n y Make',
    goal='Diseñar arquitecturas de automatización eficientes para clientes.',
    backstory='Experto técnico con enfoque en soluciones escalables. Dominas el uso de webhooks y APIs.',
    llm=llm,
    verbose=True
)

# 3. DEFINICIÓN DE LA TAREA
# Aquí puedes cambiar la descripción según el proyecto (Bajakey, Libro Club, etc.)
tarea_analisis = Task(
    description='Analizar la viabilidad técnica de conectar WhatsApp con n8n para prospección inmobiliaria.',
    expected_output='Un documento con los 5 pasos técnicos clave y los perfiles adicionales necesarios.',
    agent=consultor
)

# 4. ORQUESTACIÓN DE LA COLMENA
def run():
    colmena = Crew(
        agents=[consultor], # El manager se añade automáticamente en proceso jerárquico
        tasks=[tarea_analisis],
        process=Process.hierarchical,
        manager_agent=manager,
        verbose=True
    )
    
    return colmena.kickoff()

if __name__ == "__main__":
    resultado = run()
    print("\n\n########################")
    print("## RESULTADO FINAL ##")
    print("########################\n")
    print(resultado)
