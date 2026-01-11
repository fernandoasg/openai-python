from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)
model="gpt-5-mini"

system_prompt = """"
Você é um categorizador de produtos.
Você deve assumir as categorias presentes na lista abaixo.

# Lista de Catagorias Válidas
- Moda Sustentável
- Produtos para o Lar
- Beleza Natural
- Eletrônicos Verdes

# Formato da Saída
Produto: Nome do Produto
Categoria: apresente a categoria do produto

# Exemplo de Saída
Produto: Escova elétrica com recarga solar
Categoria: Eletrônicos Verdes
"""

user_prompt = input("Apresente o nome de um produto: ")


response = client.chat.completions.create(
  model=model,
  messages=[
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": user_prompt
    }
  ],
  temperature = 0,
  max_tokens = 200
)

print(response.choices[0].message.content)
