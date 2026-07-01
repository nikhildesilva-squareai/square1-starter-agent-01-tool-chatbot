# Tool-Using Chatbot — Square 1 AI starter

**Part of [Square 1 AI](https://square1-tutor.vercel.app) · LLM Agent Architect · Project 1.**

🤖 **Agent project.** This repo provides the project scaffold, function stubs, and contract tests. Read the full brief on Square 1 for guidance.

MIT licensed — fork it, build on it, put it in your portfolio.

---

# P1: Tool-Using Chatbot

Build a conversational AI agent that can use external tools (calculator, weather lookup, web search) to answer user questions. The agent decides when a tool is needed, calls it, and incorporates the result into its response.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # Add your ANTHROPIC_API_KEY
```

## Usage

```bash
python -m src.cli
```

## Project Structure

```
src/
  tools.py       - Tool definitions and execution logic
  agent.py       - ToolAgent class that orchestrates tool use
  cli.py         - Interactive command-line interface
tests/
  test_agent.py  - Contract tests for agent behaviour
```
