def int8_to_fp32(tupla_int8):
    # Valores mínimos y máximos para int8 y FP32
    int8_min = -128
    int8_max = 127
    fp32_min = -1.0
    fp32_max = 1.0

    # Convertir los valores int8 a FP32
    tupla_fp32 = tuple((valor_int8 - int8_min) * (fp32_max - fp32_min) / (int8_max - int8_min) + fp32_min for valor_int8 in tupla_int8)
    
    return tupla_fp32

# Ejemplo de uso
# tupla_int8 = (-88, 29, -80, -29)
tupla_int8 = (-50, 100, -20, 60)
tupla_fp32 = int8_to_fp32(tupla_int8)
print("Tupla en int8:", tupla_int8)
print("Tupla en FP32:", tupla_fp32)


def int8_to_positive_fp32(tupla_int8):
    # Valores mínimos y máximos para int8 y FP32
    int8_min = -128
    int8_max = 127
    fp32_min = 0.0
    fp32_max = 1.0

    # Convertir los valores int8 a FP32
    tupla_fp32 = tuple((valor_int8 - int8_min) * (fp32_max - fp32_min) / (int8_max - int8_min) + fp32_min for valor_int8 in tupla_int8)
    
    return tupla_fp32

# Ejemplo de uso
tupla_int8 = (-50, 100, -20, 60)
tupla_fp32_positive = int8_to_positive_fp32(tupla_int8)
print("Tupla en int8:", tupla_int8)
print("Tupla en FP32 (positivos):", tupla_fp32_positive)


import numpy as np

# Crear una matriz de 500x250x3 con números aleatorios entre 0 y 255
frame = np.random.randint(0, 256, (1080, 810, 3), dtype=np.uint8)
x,y,w,h = tupla_fp32_positive
# Coordenadas del punto (ejemplo)
x = int(x * frame.shape[1])
y = int(y * frame.shape[0])
# Dimensiones del rectángulo
width = int(w * frame.shape[1])
height = int(h * frame.shape[0])
print('Redim: ', (x, y, width, height), ' <> ', frame.shape)




