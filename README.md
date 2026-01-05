# LangChain + Azure OpenAI Fintech Learning Series

Welcome to my personal learning repo exploring large language models (LLMs) in Python, powered by **LangChain** and **Azure OpenAI**—with a special focus on fintech use cases.  
This is a living, growing series that documents my progress from initial setup through more advanced experiments, with real troubleshooting notes and practical insights.

---

## About This Repo

This repo is my technical playground for:
- Building and running LLM-powered applications
- Testing how Azure OpenAI models work with LangChain
- Tackling common developer struggles (and sharing the fix!)
- Logging every step, challenge, and learning moment for future reference

You’ll find scripts, environment configs, logs, and markdown summaries for every major milestone.

---

## Repo Structure

- `/tasks/` – Individual experiments and mini-projects (Hello World, chains, agents, fintech examples)
- `/logs/`  – Progress journals and troubleshooting notes for each milestone
- `/env-samples/` – Example `.env` and config files
- `README.md` – This log and getting-started guide

---

## Getting Started: Environment Setup

1. **Clone this repo:**
    ```bash
    git clone <your-repo-url>
    cd langchain-fintech-learning
    ```

2. **Create and activate your Python environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate      # Or .\venv\Scripts\activate for Windows
    pip install -r requirements.txt
    ```

3. **Add your Azure keys/settings to `.env`:**
    ```
    OPENAI_API_KEY=your-azure-key
    AZURE_OPENAI_ENDPOINT=https://<your-resource>.azure.com/
    OPENAI_DEPLOYMENT_NAME=<your-deployment>
    OPENAI_API_VERSION=<version>
    ```

---

## Progress Log & Key Learnings

### Week 1: First Steps & “Hello World”
- Set up Azure OpenAI, LangChain, and Python environment
- Learned the difference between completion and chat models
- Navigated package deprecations and API parameter changes
- Beat a string of errors with careful reading and community help


### Troubleshooting Highlights
- Always check for library updates—LangChain changes quickly!
- Azure chat models require message lists (not raw strings)
- Use the right endpoints (`azure_endpoint`, not legacy names)
- Error messages often point directly to the fix

---

## Goals for This Repo
- To document every major step and provide “real developer” insights
- To help others get started with Azure OpenAI + LangChain in a practical way
- To build a fintech feature demo with LLMs as a long-term capstone

---

## Contributions & Sharing
Feel free to fork, clone, and try these scripts yourself!  
PRs, issues, and commentaries are welcome—especially if you hit different errors and want help troubleshooting.

---

## Further Reading
- [LangChain Docs](https://python.langchain.com/)
- [Azure OpenAI Docs](https://learn.microsoft.com/en-us/azure/ai-services/openai/)

---

**Thanks for following along as I learn, build, and debug—one task at a time!**