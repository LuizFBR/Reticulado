# Reticulado
Um reticulado é uma estrutura discreta ordenada onde cada dois elementos possuem pelo menos um elemento maior que eles.

Esse repositório traz métodos gerais de reticulados. Em reticulado.py temos uma classe Reticulado que cria um reticulado(lista de adjacência) a partir de uma lista de pares que indicam as arestas de um diagrama de Hasse.

## generate(start,n)

_generate()_ é um método de reticulado que gera um reticulado probabilístico a partir de um conjunto {start,start+1,..., n-1, n} onde start <= n.

sendo que há uma ordem total <= tal que start <= start + 1 ( a mesma ordem dos inteiros).