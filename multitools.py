import os
os.environ['COHERE_API_KEY'] = "AQWILHeT6TLrmqR94NrY4xDqAZSwUp1MmjsSPqV8"
from langchain_cohere.chat_models import ChatCohere
chat = ChatCohere(model="command-r-plus", temperature=0.3)
from langchain_community.tools.tavily_search import TavilySearchResults

os.environ['TAVILY_API_KEY'] = "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"

internet_search = TavilySearchResults()
internet_search.name = "internet_search"
internet_search.description = "Returns a list of relevant document snippets for a textual query retrieved from the internet."

def multi_tool(user_input):
    from langchain_core.pydantic_v1 import BaseModel, Field
    class TavilySearchInput(BaseModel):
        query: str = Field(description="Query to search the internet with")
    internet_search.args_schema = TavilySearchInput



    from langchain_community.tools import YouTubeSearchTool
    tool = YouTubeSearchTool()
    

    from langchain_community.tools.google_finance import GoogleFinanceQueryRun
    from langchain_community.utilities.google_finance import GoogleFinanceAPIWrapper


    

    os.environ["SERPAPI_API_KEY"] = "b0d557ad9098b11faee2a632271e724005c5c98d7548baac1bb2d441adb77640"
    tool1 = GoogleFinanceQueryRun(api_wrapper=GoogleFinanceAPIWrapper())
    from langchain.agents import AgentExecutor
    from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
    from langchain_core.prompts import ChatPromptTemplate

    prompt = ChatPromptTemplate.from_template("{input}")



    agent = create_cohere_react_agent(
        llm=chat,
        tools=[internet_search, tool,tool1],
        prompt=prompt,
    )
    agent_executor = AgentExecutor(agent=agent, tools=[internet_search, tool,tool1], verbose=True)
    a=agent_executor.invoke({
        "input": user_input,
    })
    return a