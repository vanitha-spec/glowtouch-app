import os
from dotenv import load_dotenv
from smolagents import CodeAgent, LiteLLMModel

load_dotenv()

model = LiteLLMModel(
    model_id="gemini/gemini-3.5-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY"),
    # Key: increase thinking level, otherwise agent may terminate prematurely
    thinking_level="MEDIUM",
    # Note: 3.5-flash-lite does NOT support temperature, top_k, top_p customization
    # Do not pass these parameters, otherwise they will be ignored or throw errors 
)

from tools import list_products, check_stock, recommend_by_skin, place_order

agent = CodeAgent(
    tools=[list_products, check_stock, recommend_by_skin, place_order],
    model=model,
    max_steps=6
)