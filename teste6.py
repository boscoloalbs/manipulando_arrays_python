'''
 Implemente um método que retorne um array, sem valores duplicados. Entrada do método ([1,2,3,3,2,4,5,4,7,3]), Resultado do método: [1,2,3,4,5,7]
'''

array = [1,2,3,3,2,4,5,4,7,3]
array_novo = []

array_novo = set(array)

print(array_novo)