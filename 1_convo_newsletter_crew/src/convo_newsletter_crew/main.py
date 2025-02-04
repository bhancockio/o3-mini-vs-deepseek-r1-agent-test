#!/usr/bin/env python
import sys
import warnings

from convo_newsletter_crew.crew import ConvoNewsletterCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "brain_dump": """
            - I need your help writing a news letter for my AI Developer audience. The main topic I want to talk about is how there are 4 types of luck:
            - **Blind luck**
                - Completely random and out of our control
                    - We can't do anything to attract it
            - **Luck from motion**
                - Occurs when we create motion and collisions through hustle and energy
                - More under our control than blind luck
                - More under our control than blind luck
            - **Luck from awareness**
                - About being present, observant, and receptive to the world around us
                - About being present, observant, and receptive to the world around us
                - Recognizing opportunities when they arise
                - Recognizing opportunities when they arise
            - **Luck from uniqueness**
                - Occurs when our unique set of attributes attracts specific opportunities to us
                - Occurs when our unique set of attributes attracts specific opportunities to us
                - Luck finds us, rather than us seeking it out
                - Luck finds us, rather than us seeking it out
        - In the news letter, I want to talk about how each type of luck relates to the core tenants of building an AI Personal Brand.
        - There is nothing we can do about blind luck except hope that it happens to us.
        - `Luck from motion` happens when you build an AI Personal brand because each week you are taking action by building new AI apps, testing new AI technologies, building more automations to solve real world problems. Through large amounts of actions we can stumble upon luck. The core lesson here is to take insane amount of action and eventually the universe gives in and give you the rewards you’ve earned.
        - `Luck from awareness` The AI space is moving so fast so by having your finger on the pulse of the market you know what’s going on before the rest of the world has a chance to react. You can win multiple ways here: investing in a company, joining a start up, building an app because you notice a gap in the market. For example, if you were tracking AI in February 2024, you’ll notice that Google’s Gemini was a flop and was overly ‘woke’. As a result, the stock started to tank. But, if you were aware of the rate of change of AI, you knew that this would eventually be resolved and Google would go on to create great AI products and services. So by by being aware, you would have invested and now you’d be up 50%. Very glad I made this trade last year!
        - `Luck from uniqueness` by building an AI Personal brand you are constantly posting Valuable YouTube videos to bring awareness to your skills and talents. This is my favorite one because you are opening yourself up to endless opportunities by publishing content on YouTube. You will be shocked with the number of people and business who reach out to you to build something for their business. The best part is they come to you. As you build a personal brand, you will go through the transition of “man, no one is hiring me” to “man, I have too many opportunities, I’m struggling to pick which is the right one”
        """
    }

    try:
        ConvoNewsletterCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "brain_dump": """
            - I need your help writing a news letter for my AI Developer audience. The main topic I want to talk about is how there are 4 types of luck:
            - **Blind luck**
                - Completely random and out of our control
                    - We can't do anything to attract it
            - **Luck from motion**
                - Occurs when we create motion and collisions through hustle and energy
                - More under our control than blind luck
                - More under our control than blind luck
            - **Luck from awareness**
                - About being present, observant, and receptive to the world around us
                - About being present, observant, and receptive to the world around us
                - Recognizing opportunities when they arise
                - Recognizing opportunities when they arise
            - **Luck from uniqueness**
                - Occurs when our unique set of attributes attracts specific opportunities to us
                - Occurs when our unique set of attributes attracts specific opportunities to us
                - Luck finds us, rather than us seeking it out
                - Luck finds us, rather than us seeking it out
        - In the news letter, I want to talk about how each type of luck relates to the core tenants of building an AI Personal Brand.
        - There is nothing we can do about blind luck except hope that it happens to us.
        - `Luck from motion` happens when you build an AI Personal brand because each week you are taking action by building new AI apps, testing new AI technologies, building more automations to solve real world problems. Through large amounts of actions we can stumble upon luck. The core lesson here is to take insane amount of action and eventually the universe gives in and give you the rewards you’ve earned.
        - `Luck from awareness` The AI space is moving so fast so by having your finger on the pulse of the market you know what’s going on before the rest of the world has a chance to react. You can win multiple ways here: investing in a company, joining a start up, building an app because you notice a gap in the market. For example, if you were tracking AI in February 2024, you’ll notice that Google’s Gemini was a flop and was overly ‘woke’. As a result, the stock started to tank. But, if you were aware of the rate of change of AI, you knew that this would eventually be resolved and Google would go on to create great AI products and services. So by by being aware, you would have invested and now you’d be up 50%. Very glad I made this trade last year!
        - `Luck from uniqueness` by building an AI Personal brand you are constantly posting Valuable YouTube videos to bring awareness to your skills and talents. This is my favorite one because you are opening yourself up to endless opportunities by publishing content on YouTube. You will be shocked with the number of people and business who reach out to you to build something for their business. The best part is they come to you. As you build a personal brand, you will go through the transition of “man, no one is hiring me” to “man, I have too many opportunities, I’m struggling to pick which is the right one”
        """
    }
    try:
        ConvoNewsletterCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ConvoNewsletterCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        ConvoNewsletterCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
