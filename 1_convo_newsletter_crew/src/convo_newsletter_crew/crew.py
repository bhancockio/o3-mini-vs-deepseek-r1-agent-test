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

    # Using OpenRouter
    llm = LLM(
        model="openrouter/deepseek/deepseek-r1",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPEN_ROUTER_API_KEY"),
    )

    # llm = LLM(
    #     model="openrouter/openai/o3-mini",
    #     base_url="https://openrouter.ai/api/v1",
    #     api_key=os.getenv("OPEN_ROUTER_API_KEY"),
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
