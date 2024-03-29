'''
Implemente um método que a partir de um array de arrays, converta em um objeto com chave e valor. Entrada do método ([["c",2],["d",4]]), Resultado do métdodo: {c:2, d:4}
'''

array = [["c", 2], ["d", 4]]
dicionario = {}

for item in array:
    dicionario[item[0]] = item[1]

print(dicionario)