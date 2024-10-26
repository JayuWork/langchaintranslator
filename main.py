import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

def getStarted():
    # PART1 Simplest way of using LLM, with stroutput
    # messages = [
    #     SystemMessage(content="Translate the following from English into Italian"),
    #     HumanMessage(content="hi!"),
    # ]
    # llm = ChatOpenAI(model="gpt-4", temperature=0)
    # parser = StrOutputParser()
    # chain =  llm | parser
    # response = chain.invoke(messages)
    # print(response)

    # PART2 Using LLM with prompt template
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    system_template = "Translate the following into {language}:"
    prompt_template = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", "{text}")]
        )
    chain = prompt_template | llm | StrOutputParser()
    response = chain.invoke({"language": "hindi", "text": "hi"})

    print(response)




if __name__ == "__main__":
    getStarted()
