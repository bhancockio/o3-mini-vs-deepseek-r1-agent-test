import os

import agentops
from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from convo_newsletter_crew.tools.word_counter_tool import WordCounterTool

agentops.init()


@CrewBase
class ConvoNewsletterCrew:
    """ConvoNewsletterCrew crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # --- OpenRouter ---
    # DEEPSEEK-R1
    # AGENTOPS TRACE: 9e5e4409-7602-4eec-8f0d-7b318f80f501
    # llm = LLM(
    #     model="openrouter/deepseek/deepseek-r1",
    #     base_url="https://openrouter.ai/api/v1",
    #     api_key=os.getenv("OPEN_ROUTER_API_KEY"),
    # )

    # DEEPSEEK-V3
    # AGENTOPS TRACE: e0c57b3b-5961-4b3b-bae5-73e5bae6dc4d
    # llm = LLM(
    #     model="openrouter/deepseek/deepseek-chat",
    #     base_url="https://openrouter.ai/api/v1",
    #     api_key=os.getenv("OPEN_ROUTER_API_KEY"),
    # )

    # CLAUDE 3.5 SONNET
    # AGENTOPS TRACE: ec8b3ffb-a32e-415e-b0d2-58fe5dafba7b
    llm = LLM(
        model="openrouter/deepseek/deepseek-chat",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPEN_ROUTER_API_KEY"),
    )

    # O3-MINI - REASONING EFFORT MEDIUM
    # AGENTOPS TRACE: 299c6e7d-78dc-4d35-8b6b-81987c3f4471
    # llm = LLM(
    #     model="o3-mini",
    #     api_key=os.getenv("OPENAI_API_KEY"),
    # )

    # gpt-4o
    # AGENTOPS TRACE: b98e3850-2e9b-4d26-81e2-37949a222a31
    # llm = LLM(
    #     model="gpt-4o",
    #     api_key=os.getenv("OPENAI_API_KEY"),
    # )

    @agent
    def synthesizer(self) -> Agent:
        return Agent(
            llm=self.llm, config=self.agents_config["synthesizer"], verbose=True
        )

    @agent
    def newsletter_writer(self) -> Agent:
        return Agent(
            llm=self.llm,
            config=self.agents_config["newsletter_writer"],
            tools=[WordCounterTool()],
            verbose=True,
        )

    @agent
    def newsletter_editor(self) -> Agent:
        return Agent(
            llm=self.llm,
            config=self.agents_config["newsletter_editor"],
            tools=[WordCounterTool()],
            verbose=True,
        )

    @task
    def generate_outline_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_outline_task"],
        )

    @task
    def write_newsletter_task(self) -> Task:
        return Task(
            config=self.tasks_config["write_newsletter_task"],
            output_file="newsletter_draft.md",
        )

    @task
    def review_newsletter_task(self) -> Task:
        return Task(
            config=self.tasks_config["review_newsletter_task"],
            output_file="final_newsletter.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ConvoNewsletterCrew crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
