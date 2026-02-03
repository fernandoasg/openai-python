import tiktoken

modelo = "gpt-4"
codificador = tiktoken.encoding_for_model(modelo)
lista_tokens = codificador.encode("Você é um catagorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantos tokens temos: ", len(lista_tokens))
print(f"Custo para o modelo {modelo} é de ${len(lista_tokens) / 1000 * 0.03:.2f}")

modelo = "gpt-3.5-turbo"
codificador = tiktoken.encoding_for_model(modelo)
lista_tokens = codificador.encode("Você é um catagorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantos tokens temos: ", len(lista_tokens))
print(f"Custo para o modelo {modelo} é de ${len(lista_tokens) / 1000 * 0.002:.2f}")