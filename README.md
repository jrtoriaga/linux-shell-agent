# Linux Shell Agent

A conversational Python agent powered by **LangChain**, **LangGraph**, and **Gemini** that assists with Linux tasks.  
It responds with charm, wit, and a warm British accent—executing shell commands, managing files, and searching the web naturally.

## ✨ Features
- Conversational agent for Linux Mint
- Runs shell commands safely via `ShellTool`
- File creation & text file reading
- Web search with Tavily
- In-memory checkpointing for conversation continuity
- Graceful quit with `quit` or `exit`

## 🚀 Usage

First generate the Agent.py script:

```bash
jupyer nbconvert --to-script --no-prompt Agent.ipynb
```
Then, run the script with:

```bash
python agent.py
```
Type your commands, and the agent will respond as if it were your helpful assistant.

To exit, type `exit` or `quit`.

## 📦 Requirements

- Python 3.9+

- LangChain

- LangGraph

- Google Generative AI

- Tavily API key (for search)

- .env file with necessary credentials

```.env
GOOGLE_API_KEY=<YOUR-GOOGLE-API-KEY>
TAVILY_API_KEY=<YOUR-TAVILY-API-KEY>
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## ⚠️ Note

This agent executes shell commands. Commands are explained before running if risky.

Use in a safe environment.


## 📝 License
MIT
