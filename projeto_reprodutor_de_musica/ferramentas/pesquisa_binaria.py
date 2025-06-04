def pesquisa_binaria(lista, alvo: str) -> int:
    # garante que a busca feita sempre vai ser pelo nome do arquivo
    inicio = 0
    fim = len(lista)

    while inicio < fim:
        meio = (inicio + fim) // 2
        nome_atual = lista[meio].nome.lower()

        if nome_atual == alvo.lower():
            return meio
        elif nome_atual > alvo.lower():
            fim = meio
        else:
            inicio = meio + 1

    print("Elemento não encontrado")
    return -1

def ordenar_por(lista: list[object], chave: str) -> list:
    # python usa timSort por padrão, algoritmo de ordenação eficiente
    return sorted(lista, key=lambda x: x.__dict__[chave])