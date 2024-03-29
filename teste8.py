'''
 Implemente um método que remova os aninhamentos de um array de arrays para um array unico. Entrada do método ([1, 2, [3], [4, 5]]), Resultado do método: [1, 2, 3, 4, 5]
'''
#Biblioteca itertools para desaninhamento o array.
from itertools import chain

#Converte cada elemento do array arrays para string.
def converter_para_string(arrays):
    return [str(item) for item in arrays]

#Desaninha o array arrays e retorna um único array com todos os elementos concatenados.
def desaninhamento(arrays):
    return list(chain(*arrays))

#Converte cada elemento do array novo_array para inteiro.
def converter_para_inteiro(novo_array):
    return  list(map(int, novo_array))

arrays = [1,2,[3],[4,5]] #O array original que contém arrays aninhados.
arrays = converter_para_string(arrays) 
array = desaninhamento(arrays) #O array desaninhado com elementos em string.
novo_array = [] #O array final com os elementos convertidos para inteiro.

for item in array: #Um loop for é usado para iterar sobre o array (desaninhado).
    if item and item != "[" and item != "]" and item != "," and item != " ": #Se o elemento não for vazio, um espaço em branco, "[" ou "]", ele é adicionado ao array novo_array.
        novo_array.append(item)

novo_array = converter_para_inteiro(novo_array) #A função converte cada elemento do array novo_array para inteiro usando a função map.

print(novo_array)