# Progress log
## Environment set up 

cd langchain-fintech-learning
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install langchain_openai dotenv

# My First Steps with Azure OpenAI & LangChain: Progress Log
# jan 5 2026

**Today, I built my very first program** to talk to an AI (LLM) using **Microsoft Azure OpenAI** and **LangChain in Python** — a true *“Hello World”* moment!

### Setting Up
I started by creating a virtual environment and installing the basic packages I’d need — **langchain-openai** for the LLM connection, **python-dotenv** to securely handle my Azure keys and settings, and **openai** as the underlying API.

I put my **Azure credentials** *(endpoint, key, deployment name, and API version)* into a **.env** file. This kept things organized and safer than hardcoding secrets.

### Import Challenges
At first, I tried using the old way of importing with:
```python
from langchain.llms import AzureOpenAI
```

but quickly ran into “could not be resolved” errors. After some research, I learned the package had been updated, so I installed and switched to:
```python
from langchain_openai import AzureOpenAI
```

and for chat models, to:
```python
from langchain_openai import AzureChatOpenAI
```

### Solving Problems Along the Way
It wasn’t smooth sailing! I kept hitting errors about *“object not callable,”* and even some cryptic warnings about endpoint parameter names. Here’s how I solved them:

- **Deprecation & Import issues:** Changed import statements to match the latest LangChain structure.
- **Endpoint confusion:** Made sure to use `azure_endpoint` *(not `openai_api_base`)* everywhere, and updated my `.env` accordingly.
- **TypeError (object not callable):** Realized with newer LangChain versions, instead of calling the model like a function, I should use `.invoke()` — so I switched to:
```python
response = llm.invoke(prompt)
```

### 💡 What I Learned
- If an error pops up, there’s nearly always an answer in the docs or error message.
- Azure’s chat models need special handling *(don’t treat them like old text-only AI!)*
- LangChain and the open-source AI world move fast — reading deprecation warnings helped me future-proof my code.
- A simple idea (*“Hello World”*) is a great way to learn something new, even if you trip over a few Python errors.

### Overall
It took a little troubleshooting, but now I have a reliable way to interact with **Azure OpenAI** from my own Python code — and I’m excited to keep exploring!