'''
Implemente um método que inverta um array, não utilize métodos nativos do array. Entrada do método ([1,2,3,4]), Resultado do método: [4,3,2,1]
'''

#modo simples
array = [1,2,3,4]
print(array[: : -1])

novo_array = []

#utilizando for para varrer o array, range para determinar quantas vezes o for irá rodar.
for i in range(len(array)-1, -1, -1):
    novo_array.append(array[i])

print(novo_array)
