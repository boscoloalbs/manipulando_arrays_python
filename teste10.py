'''
Implemente um método que encontre os valores comuns entre dois arrays. Entrada do método ([6, 8], [8, 9]), Resultado do método: [8]
'''

array1 = [6,8]
array2 = [8,9]
array3 = []

for item in array1: #for para varrer o array1, pegando um elemento por vez
    if item in array2: #condiÇão para verificar se o elemento x de for está dentro da array2
        array3.append(item) #se verdadeiro, esse elemento vai ser adicionado em um novo array.

print(array3)
