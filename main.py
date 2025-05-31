from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor

load_dotenv()
# testing 
# response = llm.invoke("What is the meaning of life")
# print(response)

# prompt template setup
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOpenAI(model = "gpt-4o-mini")
parser = PydanticOutputParser(pydantic_object = ResearchResponse)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions = parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm= llm,
    prompt=prompt,
    tools=[]
)

# testing agent
# verbose=True to see the thought process of the agent
agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
raw_response = agent_executor.invoke({"query" : "introduce yourself."})
print(raw_response)

# formate the output : use parser to parse the content
try:
    structured_response = parser.parse(raw_response.get("output"))
except Exception as error:
    print("Error parsing response:", error, "The raw response is: ", raw_response)

