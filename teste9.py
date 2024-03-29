'''
Implemente um método divida um array por uma quantidade passada por parâmetro. Entrada do método ([1, 2, 3, 4, 5], 2), Resultado do método: [[1, 2], [3, 4], [5]]
'''

def dividir_array(array, tamanho):
  
  subarrays = []
  for i in range(0, len(array), tamanho):
    subarrays.append(array[i:i + tamanho])

  return subarrays

array = [1, 2, 3, 4, 5]
tamanho = 2

subarrays = dividir_array(array, tamanho)

print(subarrays)
