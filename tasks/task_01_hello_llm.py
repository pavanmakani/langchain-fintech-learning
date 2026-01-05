import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")      
deployment_name = os.getenv("OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("OPENAI_API_VERSION")

if not all([api_key,deployment_name, api_version]):
    raise ValueError("Some Azure OpenAI env variables are missing!")

# Initialize the LLM - I am using chat model and therefore using AzureChatOpenAI
llm = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    deployment_name=deployment_name,
    api_version=api_version,
)

# Sample fintech prompt
prompt = "Hello, LLM! I'm 'Hello World'—my very first program to interact with an AI model. Could you please welcome me and share some tips or encouragement for beginners learning to use language models?"

response = llm.invoke(prompt)

print(f"\n--- Azure ChatGPT Response ---\n{response.content}")



"""
Output:
--- Azure ChatGPT Response ---
Welcome, *Hello World*! 🎉  

That’s a fantastic milestone—writing your first program to interact with a language model means you’re stepping into an exciting world of creativity, exploration, and problem‑solving. Here are a few tips and bits of encouragement as you get started:

1. **Experiment Freely**  
   Try different kinds of prompts—ask questions, request explanations, generate creative text, or have the model summarize something. This helps you understand how prompt phrasing influences the quality of responses.

2. **Be Specific**  
   The more context you provide, the better the results. Instead of “Tell me about code,” try “Explain how a for loop works in Python with a short example.”

3. **Iterate and Refine**  
   Think of prompt design like debugging—when a response isn’t quite right, tweak your input. Small wording changes can make a big difference.

4. **Learn the Model’s Strengths and Limits**  
   Language models are great for reasoning, brainstorming, and learning new concepts, but they don’t have real‑time awareness or guaranteed factual accuracy. Use them as an assistant, not an oracle.

5. **Keep a Curious Mindset**  
   Every prompt you try teaches you something new about how both *you* and the model think. Stay playful and curious—learning is most effective (and fun) that way!

Congratulations again on your first step into AI programming—each experiment from here is a chance to create something amazing. What kind of project are you thinking about building next?
"""