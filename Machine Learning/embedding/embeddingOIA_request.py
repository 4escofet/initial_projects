import os
import openai
from config import OAI_client_id, OAI_client_secret

openai.api_key = OAI_client_secret
openai.Embedding.create(
  model="text-embedding-ada-002",
  input="The food was delicious and the waiter..."
)