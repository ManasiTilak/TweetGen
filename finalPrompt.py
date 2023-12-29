import os
import re
import openai
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

load_dotenv()

# Secret keys from .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

RAW_TEXT_FILE = ("content-ideas.txt")

llm = ChatOpenAI(temperature=0.3,
                 openai_api_key=OPENAI_API_KEY,
                 model_name='gpt-3.5-turbo-0613',
                )

def generate_response(
    llm: ChatOpenAI, coding_topic: str, coding_explaination: str
) -> tuple[str, str]:
    """Generate AI Twitter Content for CodingAunty Twitter Account

    Parameters:
        - llm:  pre-trained ChatOpenAi large language model
        - coding_topic: Topic related to Python
        - coding_topic: Topic related to Python

    Returns:
        - tuple[long response,short reposonse]: Chat GPT long and short responses
    """
    # System Template for LLM to follow
    system_template = """
        You are an incredibly wise and smart coder and programmer that lives and breathes the world of Python Programming Language.
        Your goal is to writing short-form content for twitter given a `topic` in the area of Python programming  and a `explaination` from the user.

        % RESPONSE TONE:

        - Your response should be given in an active voice and be opinionated
        - Your tone should be serious w/ a hint of wit and sarcasm
        
        % RESPONSE FORMAT:
        
        - Be extremely clear and concise
        - Respond with phrases no longer than two sentences
        - Do not respond with emojis
     % RESPONSE CONTENT:

        - Include specific examples of where this is used in the programming space
        - If you don't have an answer, say, "Sorry, I'll have to ask the Python Programming Gods!"    

        
        % RESPONSE TEMPLATE:

        - Here is the response structure: 
            Tweet: A captivating engaging tweet, hooking the user and engaging him
            Hash Tags: 3 relevant hashtags
    
    """
    # system prompt template to follow
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

    # human template for input
    human_template = "topic to write about is {topic}, and the exolaination will be {explaination}. Keep the total response under 200 words total!"
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        human_template, input_variables=["topic", "explaination"]
    )

    # chat prompt template construction
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    # get a completed chat using formatted template with topic and title
    final_prompt = chat_prompt.format_prompt(
        topic=coding_topic, explaination=coding_explaination
    ).to_messages()

    # pass template through llm and extract content attribute
    first_response = llm(final_prompt).content

    # construct AI template, to pass back OpenAI response
    ai_message_prompt = AIMessagePromptTemplate.from_template(first_response)

     # additional prompt to remind ChatGPT of length requirement
    reminder_template = "This was good, but way too long, please make your response much more concise and much shorter! Make phrases no longer than 15 words in total. Please maintain the existing template."
    reminder_prompt = HumanMessagePromptTemplate.from_template(reminder_template)

    # chat prompt template construction with additional AI response and length reminder
    chat_prompt2 = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_template, ai_message_prompt, reminder_prompt]
    )

    # get a completed chat using formatted template with topic and title
    final_prompt = chat_prompt2.format_prompt(
        topic=coding_topic, explaination=coding_explaination
    ).to_messages()

    # pass template through llm and extract content attribute
    short_response = llm(final_prompt).content

    return first_response, short_response

    first_response, short_response = generate_response(
    llm, 
    coding_topic='List Comprehensions', 
    coding_explaination='How to use list comprehensions for more concise and readable code.'
    )