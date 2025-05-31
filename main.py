from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
# from langchain_core prompts import 

load_dotenv()
llm = ChatOpenAI(model = "gpt-4o-mini")

# testing 
# response = llm.invoke("What is the meaning of life")
# print(response)

# prompt template setup
