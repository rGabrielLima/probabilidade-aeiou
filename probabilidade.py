import random

# separando as letras vogais e consoantes
vogais = ['A', 'E', 'I', 'O', 'U']
consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

# Definindo os pesos de cada
pesos = [0.3] * len(vogais) + [0.1] * len(consoantes)

# Combinação das vogais e consoantes em uma lista única para gerar pseudopalavras
letras = vogais + consoantes

# Número de palavras aleatórias que serão geradas
quantidade_palavras = 100000

# Geração das palavras aleatórias com base nos pesos
resultados = random.choices(letras, pesos, k=quantidade_palavras)

# Contagem das vogais e consoantes nos resultados
contagem_vogais = sum(1 for letra in resultados if letra in vogais)
contagem_consoantes = sum(1 for letra in resultados if letra in consoantes)

# Cálculo das probabilidades
probabilidade_vogais = contagem_vogais / quantidade_palavras
probabilidade_consoantes = contagem_consoantes / quantidade_palavras

# Impressão dos resultados
print(f"Probabilidade de cair vogais: {probabilidade_vogais * 100:.2f}%")
print(f"Probabilidade de cair consoantes: {probabilidade_consoantes * 100:.2f}%")


""""
Importei o módulo random para gerar números aleatórios.

Definimos a lista vogais contendo as vogais do alfabeto e a lista consoantes contendo as consoantes do alfabeto.

Definimos a lista pesos atribuindo o valor de 0.3 para cada vogal e o valor de 0.1 para cada consoante. Esses pesos indicam as probabilidades relativas de cada letra ser escolhida.

Criamos a lista letras combinando as listas de vogais e consoantes em uma única lista.

Definimos a variável quantidade_palavras para armazenar o número de palavras aleatórias que desejamos gerar.

Utilizamos a função random.choices para gerar as palavras aleatórias. Passamos a lista letras como opções, os pesos correspondentes em pesos e o valor de quantidade_palavras para definir o número de palavras a serem geradas. Os resultados são armazenados na lista resultados.

Usamos a função sum em uma expressão geradora para contar a quantidade de vogais e consoantes nos resultados. A expressão 1 for letra in resultados if letra in vogais gera um valor 1 para cada letra vogal encontrada nos resultados. Usamos a mesma lógica para contar as consoantes.

Calculamos as probabilidades dividindo as contagens pelas quantidade_palavras. Essas probabilidades são armazenadas nas variáveis probabilidade_vogais e probabilidade_consoantes.

Finalmente, imprimimos as probabilidades com duas casas decimais usando as instruções print.
"""