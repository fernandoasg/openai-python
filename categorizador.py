from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)
model="gpt-4.1"

def categoriza_produto(nome_produto, lista_categorias_possiveis):
  system_prompt = f""""
  Você é um categorizador de produtos.
  Você deve assumir as categorias presentes na lista abaixo.

  # Lista de Catagorias Válidas
  {lista_categorias_possiveis.split(',')}

  # Formato da Saída
  Produto: Nome do Produto
  Categoria: apresente a categoria do produto

  # Exemplo de Saída
  Produto: Escova elétrica com recarga solar
  Categoria: Eletrônicos Verdes
  """

  response = client.chat.completions.create(
    model=model,
    messages=[
      {
          "role": "system",
          "content": system_prompt
      },
      {
          "role": "user",
          "content": nome_produto
      }
    ],
    temperature = 0,
    max_tokens = 200
  )

  return response.choices[0].message.content


categorias_validas = input("Informe as categorias validas separadas por vírgula: ")

while True:
  nome_produto = input("Informe o nome do produto: ")
  texto_resposta = categoriza_produto(nome_produto, categorias_validas)
  print(texto_resposta)