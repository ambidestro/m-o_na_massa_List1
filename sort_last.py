"""
Dada uma lista de tuplas NÃO VAZIAS, retorne uma lista ordenada
em ordem crescente pelo último número de cada tupla.
Exemplo [(1, 7), (1, 3), (3, 4, 5), (2, 2)] retornará
[(2, 2), (1, 3), (3, 4, 5), (1, 7)]
Dica: use uma função como chave de busca (key) para extrair o último elemento de cada tupla.

Podemos usar duas funções aninhadas para resolver este problema,
mas apenas depois de estudar tuplas e funções lambda por duas horas
é que fui entender o que estava sendo feito e como era feito.

Confesso que o conceito de LAMBDAS em python é algo do caralho
é uma função simplificada e pode entrar como parâmetro de outras funções
como a SORTED, que será usada nesta resolução.

Um exemplo da estrutura de como o LAMBDA funciona:
primeiro vamos criar uma função def(): que soma dois números

def soma(a, b):
	return a + b

Uma LAMBDA para fazer a mesma coisa seria:

lambda a, b: a + b

E ainda podemos atribuir uma variavel com nome sugestivo a esta função lambda

soma_dois_numeros = lambda a, b: a + b

Assim, o comando print soma_dois_numeros(3, 7) teria a saída 10 no terminal.

Com esse conceito em mente, vamos às resoluções.

"""


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

### Primeiro com duas funções def (): aninhadas

def last(a): # primeiro criamos uma função auxiliar, para definir o último elemento de cada tupla
	return a[-1] # a será a ultima posição de cada tupla da lista
def sort_last(tuples): # criamos a função para ordenar tuplas já com a chave que é a função def last(a)
	return sorted(tuples, key=last) # retornamos as tuplas ordenadas pela key

#print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])) """linha para teste. Basta retirar os #"""

### Segunda solução. Criando LAMBDA e mandando pra uma variável que será usada como chave (key) da função SORTED

ultimo_item_da_tupla = lambda a: a[-1]
def sort_last(tuples):
	return sorted(tuples, key=ultimo_item_da_tupla)
#print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))

"""linha acima para teste. Basta retirar o comentário"""

### Terceira solução: com a LAMBDA direto no argumento key

def sort_last(tuples):
	# aqui retornamos ordenado(sorted) a variável tuplas,
	# pela chave de ordenação (key) que recebe a função lambda diretamente
	# onde o parêmetro a será cada tupla da lista por sua última posição 
	return sorted(tuples, key=lambda a: a[-1])

print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])) 

"""linha acima para teste. Basta retirar o comentário"""
