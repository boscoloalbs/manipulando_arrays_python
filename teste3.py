'''
Implemente um método que limpe os itens desnecessários de um array (false, undefined, strings vazias, zero, null). Entrada do método ([1,2,'', undefined]), Resultado do método: [1,2]
'''

array = [1, 2, '', None]
novo_array = []

for item in array:
    if item and item != "" and item != 0 and item != None:
        novo_array.append(item)

print(novo_array)