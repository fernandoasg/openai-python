from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

response = client.chat.completions.create(
  model="gpt-5",
  messages=[
    {
        "role": "system",
        "content": """
        Classifique o produto abaixo em uma das categorias: Higiene Pessoal, Moda ou Case e de uma descrição da categoria.
        """
    },
    {
        "role": "user",
        "content": """
        Escova de dentes de bambu
        """
    }
  ],
  temperature = 0,
  max_tokens = 200,
  n = 3
)

for contador in range(0, 3):
    print(response.choices[contador].message.content)
