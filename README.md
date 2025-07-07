# Agent_py
#### 🛠️ Tech Stack & Architecture
* This AI Agent is built using modern Python-based tools designed for building robust, modular, and extendable intelligent systems. The core components include:

#### 🔗 LangChain
* LangChain is the backbone of this AI Agent, providing the agent abstraction layer, memory management, and the ability to chain together LLM calls with tools, prompts, and knowledge retrieval mechanisms.

* Used to construct agent workflows such as tool calling, multi-step reasoning, and conversational memory.
* 📘 Learn more: https://docs.langchain.com/

#### 🤖 LLM Integration
* Supports integration with major LLMs such as OpenAI, Anthropic, or local models via LangChain's LLM wrappers.

* The agent’s logic and responses are driven by prompt engineering and LLM orchestration.
* API Docs:

    OpenAI: https://platform.openai.com/docs

    Anthropic (Claude): https://docs.anthropic.com/claude

    Hugging Face: https://huggingface.co/docs

#### 🧠 Memory and Tool Use
* Employs LangChain memory modules to maintain context across conversations.

* Custom tools can be defined and invoked dynamically by the agent to perform tasks like web search, calculations, or document analysis.

#### 📦 Python & Environment
* Written entirely in Python for flexibility and extensibility.

* Dependencies are managed via requirements.txt for easy setup in virtual environments.
* 🧪 Quick Setup:
```
conda activate env
pip install -r requirements.txt
```


#### Github Action
* added GitHub Action ```python-dependencies```
