'''
 Implemente um método que retorne um array, sem os itens passados por parâmetro depois do array de entrada. Entrada do método ([5,4,3,2,5], 5,3), Resultado do método: [4,2]
'''

array = [5,4,3,2,5]
remover = (5,3)
novo_array = []

for item in array:
    if item not in remover:
        novo_array.append(item)

print(novo_array)
