def operacoes_conjuntos(arquivo):
    x = open(arquivo, 'r')
    texto = x.readlines()
    matriz_texto = []
    for elemento in texto:
        if " \n" not in elemento:
            matriz_texto.append(elemento.replace('\n', ''))
        else:
            matriz_texto.append(elemento.replace(' \n', ''))

    # Nao remover
    numero_operacoes = int(matriz_texto.pop(0))

    indice_lista = 0
    matriz_final = []
    for i in range(0, len(matriz_texto), 3):
        vetor = []
        for j in range(3):
            vetor.append(matriz_texto[indice_lista])
            indice_lista += 1
        matriz_final.append(vetor)

    def uniao(a, b):
        resultado = []
        for i in a:
            resultado.append(i)
        for i in b:
            if i not in resultado:
                resultado.append(i)
        return f"União: conjunto 1 {a}, conjunto 2 {b}. Resultado: {resultado}  "

    def intersecao(a, b):
        resultado = []
        for elemento in a:
            if elemento in b:
                resultado.append(elemento)
        return f"Interseção: conjunto 1 {a}, conjunto 2 {b}. Resultado: {resultado}  "

    def diferenca(a, b):
        resultado = []
        for elemento in a:
            if elemento not in b:
                resultado.append(elemento)
        return f"Diferença: conjunto 1 {a}, conjunto 2 {b}. Resultado: {resultado}  "

    def cartesiano(a, b):
        resultado = []
        for i in a:
            for j in b:
                if (i, j) not in resultado:
                    resultado.append((i, j))
        return f"Produto Cartesiano: conjunto 1 {a}, conjunto 2 {b}. Resultado: {resultado}  "

    for elemento in matriz_final:
        operacao = elemento[0] 
        a = elemento[1].split(',')
        b = elemento[2].split(',')
        conjunto_1 = []
        for i in a:
            conjunto_1.append(i.replace(' ', ''))
        conjunto_2 = []
        for j in b:
            conjunto_2.append(j.replace(' ', ''))

        if operacao.lower() == "u":
            print(uniao(conjunto_1, conjunto_2))
        elif operacao.lower() == "i":
            print(intersecao(conjunto_1, conjunto_2))
        elif operacao.lower() == "d":
            print(diferenca(conjunto_1, conjunto_2))
        elif operacao.lower() == "c":
            print(cartesiano(conjunto_1, conjunto_2))

# Para testar o código chame a função operacoes_conjuntos() e passe o nome do arquivo de texto como parametro
operacoes_conjuntos('teste1.txt')
#operacoes_conjuntos('teste2.txt')
#operacoes_conjuntos('teste3.txt')