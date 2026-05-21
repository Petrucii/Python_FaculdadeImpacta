import numpy as np
 
array = np.array([5, 12, 3, 18, 7, 25, 10, 15])
 
mascara = array > 10
resultado = array[mascara]
 
print(resultado)