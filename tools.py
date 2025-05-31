# basic "control logic / work flow" for agent
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


search = DuckDuckGoSearchRun()
search_tool = Tool(
    name= "search",
    func= search.run,
    description= "Search the web for information"
)

api_wapper = WikipediaAPIWrapper(top_k_result = 1, doc_content_chars_max=200)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wapper)

def save_to_file(data:str, filename: str = "search_result.txt"):
    timestemp = datetime.now()
    formatted_text = f"--- Research Output ---\nTimestamp: {timestemp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

save_tool = Tool(
    name= "Save_file",
    func= save_to_file,
    description= "save output to file"
)

