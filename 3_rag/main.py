import os

import agentops
from crewai import LLM, Agent, Crew, Process, Task
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()
agentops.init()

# --- OpenRouter ---
# DEEPSEEK-R1
# AGENTOPS TRACE: 5dbf1ed8-80d1-47e9-b61c-bd5de33fbbfe
llm = LLM(
    model="openrouter/deepseek/deepseek-r1",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER_API_KEY"),
)

# DEEPSEEK-V3
# AGENTOPS TRACE: 561ccbfa-872c-4b97-82eb-997e68f120ae
# llm = LLM(
#     model="openrouter/deepseek/deepseek-chat",
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPEN_ROUTER_API_KEY"),
# )

# CLAUDE 3.5 SONNET
# AGENTOPS TRACE: 662bd699-10c6-4e03-a3db-b525f391409e
# llm = LLM(
#     model="openrouter/anthropic/claude-3.5-sonnet",
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPEN_ROUTER_API_KEY"),
# )

# O3-MINI - REASONING EFFORT MEDIUM
# AGENTOPS TRACE: 2e261a85-404c-4d3d-a50a-606137ec8c8d
# llm = LLM(
#     model="o3-mini",
#     api_key=os.getenv("OPENAI_API_KEY"),
# )

# gpt-4o
# AGENTOPS TRACE: 8cc941cc-731d-4e16-bb91-bacf582edd47
# llm = LLM(
#     model="gpt-4o",
#     api_key=os.getenv("OPENAI_API_KEY"),
# )


# Define tools
@tool
def get_data():
    """
    Search through the local knowledge base for relevant information.
    Args:
        query (str): The search query to look for in the knowledge base
    """
    try:
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, "data", "knowledge_base_59k.txt")

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return content

    except FileNotFoundError:
        return "Error: Knowledge base file not found."


# Define the research agent
research_agent = Agent(
    role="Research Analyst",
    goal="Analyze provided data and answer research queries accurately",
    backstory="""You are an expert research analyst with a keen eye for detail 
    and the ability to synthesize information from various sources. Your expertise 
    lies in finding relevant information and providing comprehensive, well-reasoned 
    answers to complex queries.""",
    tools=[get_data],  # Keeping SerperDevTool for web searches
    llm=llm,
    verbose=True,
)

# Define the research task
research_task = Task(
    description="""
    Analyze the following query and provide a comprehensive answer:
    'What is Brandon Hancock's favorite thing?'
    
    Steps to follow:
    1. Search the local knowledge base for relevant information
    2. Synthesize the information into a clear, well-structured response
    """,
    expected_output="""A detailed analysis answering the query, including:
    - Main points from the knowledge base
    - Well-structured conclusions
    """,
    agent=research_agent,
)

# Create the crew
crew = Crew(agents=[research_agent], tasks=[research_task], process=Process.sequential)

# Execute the crew
result = crew.kickoff()
print("\nResearch Results:")
print(result.raw)
