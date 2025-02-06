import os
from datetime import datetime

import agentops
import requests
from crewai import LLM, Agent, Crew, Process, Task
from crewai.tools import tool
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from yahoo_fin import stock_info

load_dotenv()
agentops.init()

# Initialize SerperDevTool for web scraping
search_tool = SerperDevTool()

# --- OpenRouter ---
# DEEPSEEK-R1
# AGENTOPS TRACE: 3fff57df-a05a-4183-8640-c0340bf825e5
# llm = LLM(
#     model="openrouter/deepseek/deepseek-r1",
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPEN_ROUTER_API_KEY"),
# )

# DEEPSEEK-V3
# AGENTOPS TRACE: FAILED
# llm = LLM(
#     model="openrouter/deepseek/deepseek-chat",
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPEN_ROUTER_API_KEY"),
# )

# CLAUDE 3.5 SONNET
# AGENTOPS TRACE: bcd82686-b4d0-47fc-9356-d76c3290b31c
llm = LLM(
    model="openrouter/deepseek/deepseek-chat",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER_API_KEY"),
)

# O3-MINI - REASONING EFFORT MEDIUM
# AGENTOPS TRACE: 53a60ff3-e482-4e93-bd38-72eb39fbc46e
# llm = LLM(
#     model="o3-mini",
#     api_key=os.getenv("OPENAI_API_KEY"),
# )

# gpt-4o
# AGENTOPS TRACE: ce46ce94-ae4e-4e24-81c3-ad7719849d68
# llm = LLM(
#     model="gpt-4o",
#     api_key=os.getenv("OPENAI_API_KEY"),
# )


# Define tools
@tool
def get_current_date():
    """Get the current date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")


@tool
def get_current_weather():
    """Fetch the current weather in New York (change location if needed)."""
    response = requests.get("https://wttr.in/?format=%t")
    return f"The current temperature is {response.text}."


@tool
def get_nvidia_stock():
    """Fetch the current stock price of NVIDIA (NVDA) using Yahoo Finance."""
    try:
        price = stock_info.get_live_price("NVDA")
        return f"NVIDIA stock price is ${price:.2f}"
    except Exception as e:
        return f"Failed to fetch stock price. Error: {str(e)}"


@tool
def square_numbers(number: int):
    """Calculate the square of a given numbers."""
    temp_value = int("".join(filter(str.isdigit, str(number))))
    return f"The square of the temperature ({temp_value}°C) is {temp_value ** 2}."


# Define the agent
data_maestro = Agent(
    role="The Data Maestro",
    goal="Collect various pieces of data and transform it into a song.",
    backstory=(
        "You are a highly creative and analytical AI that thrives on transforming raw data "
        "into a musical masterpiece. Today, your challenge is to take real-world information "
        "and turn it into a song in the style of 'Twinkle Twinkle Little Star'."
    ),
    tools=[
        get_current_date,
        get_current_weather,
        get_nvidia_stock,
        search_tool,
        square_numbers,
    ],
    llm=llm,
    verbose=True,
)

# Define the task
data_to_song_task = Task(
    description=(
        "1. Fetch the current date. \n"
        "2. Get the current weather (temperature). \n"
        "3. Retrieve NVIDIA's stock price. \n"
        "4. Search for the latest news on Elon Musk. \n"
        "5. Calculate the square of the temperature. \n"
        "6. Use all this information to write a song with the theme of 'Twinkle Twinkle Little Star'."
    ),
    expected_output="A full song, with multiple verses, based on the retrieved data.",
    agent=data_maestro,
)

# Create the crew
crew = Crew(
    agents=[data_maestro], tasks=[data_to_song_task], process=Process.sequential
)

# Execute the crew
result = crew.kickoff()
print(result.raw)
