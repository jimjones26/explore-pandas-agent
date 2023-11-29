# ------------------------------------------------------------------
# Import Libraries
# ------------------------------------------------------------------
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import (
    load_tools,
    initialize_agent,
    Tool,
    AgentType,
)
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd

# ------------------------------------------------------------------
# Load the OpenAI and Google Serp API tokens from .env file
# ------------------------------------------------------------------
load_dotenv(find_dotenv())

# ------------------------------------------------------------------
# Use SerpAPI tool to ask question
# ------------------------------------------------------------------
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(
    tools, llm, AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.run(
    "What is the median salary of senior data scientists in 2023? What is the figure given there is a 10% increment?"
)

# ------------------------------------------------------------------
# Load the data set
# ------------------------------------------------------------------
df = pd.read_csv("../data/raw/ds_salaries.csv")

# ------------------------------------------------------------------
# Initialize Pandas data frame agent
# ------------------------------------------------------------------
agent = create_pandas_dataframe_agent(llm, df, verbose=True)
