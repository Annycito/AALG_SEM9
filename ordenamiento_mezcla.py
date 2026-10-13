def mergesort(array):
    n = len(array)
    if n <= 1:
        return array
    # para dividir a la mitad 
    medio = n // 2
    arrayOne = array[:medio]
    arrayTwo = array[medio:]
    # Recursión
    arrayOne = mergesort(arrayOne)
    arrayTwo = mergesort(arrayTwo)
    return merge(arrayOne, arrayTwo)
#nuevo arreglo 
def merge(a, b):
    c = []  
    
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b[0])  
            b.pop(0)       
        else:
            c.append(a[0])  
            a.pop(0)        
            
    while len(a) > 0:
        c.append(a[0])     
        a.pop(0)            
        
    # while (b has elements)
    while len(b) > 0:
        c.append(b[0])      
        b.pop(0)            
        
    return c

arreglo_original = [14, 7, 3, 12, 9, 11, 6, 2]
print("Arreglo original:", arreglo_original)
#nuevo arreglo ordenado
arreglo_ordenado = mergesort(arreglo_original)
print("Arreglo ordenado:", arreglo_ordenado)
