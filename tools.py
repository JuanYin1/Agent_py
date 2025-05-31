# basic "control logic / work flow" for agent
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper, DataheraldAPIWrapper
from langchain.tools import Tool
from datetime import datetime


search = DuckDuckGoSearchRun()
search_tool = Tool(
    name= "search",
    func= search.run,
    description= "Search the web for information"
)

api_wapper = WikipediaAPIWrapper(top_k_result = 1, doc_content_chars_max=200)